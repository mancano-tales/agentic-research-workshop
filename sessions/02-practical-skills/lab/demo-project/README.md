# Projeto de demonstração — Sessão 2

Mini-projeto de pesquisa usado nas demonstrações ao vivo da Sessão 2 (caso-âncora A: discursos parlamentares). Reúne, num só lugar, os quatro mecanismos do programa: *skill*, *hooks*, subagente auditor e `AGENTS.md`.

Os discursos em `dados/brutos/discursos.csv` são **fictícios**.

## Mapa dos arquivos

| Arquivo | Mecanismo | Bloco da Sessão 2 |
|---|---|---|
| `.claude/skills/codificar-discursos/SKILL.md` | *Skill* — protocolo de codificação em prosa | 1 |
| `.claude/agents/auditor.md` | Subagente auditor com contexto limpo e só leitura | 1 |
| `.claude/hooks/proteger_dados_brutos.R` | *Hook* `PreToolUse` (guarda) — bloqueia edição em `dados/brutos/` e qualquer comando de terminal que toque a pasta e não seja uma leitura simples | 2 |
| `.claude/hooks/verificar_integridade_brutos.R` | *Hook* `PostToolUse` e `Stop` (sensor) — depois de cada comando, pergunta ao Git se `dados/brutos/` difere da última versão registrada (arquivo alterado, apagado, novo ou oculto); pega alterações feitas por scripts que a guarda não vê. A referência é o Git, e não uma lista de hashes, porque um script poderia reescrever a lista: o agente não guarda o próprio boletim | 2 |
| `.claude/hooks/validar_apos_escrita.R` | *Hook* `PostToolUse` e `Stop` — roda o validador sempre que a codificação pode ter mudado (edição, gravação ou comando de terminal) e antes de o agente encerrar | 2 |
| `R/validar_codificacao.R` | *Code as policy* — a regra executável em si | 2 |
| `.claude/settings.json` | Registro dos *hooks* e regras de permissão (nega leitura de credenciais e escrita em `dados/brutos/`) | 2 e 3 |
| `.claude/hooks/registrar_acoes.R` | *Hook* de rastreabilidade — grava `logs/registro-agente.jsonl` | 4 |
| `AGENTS.md` (e `CLAUDE.md`, que só o importa) | Instruções de projeto | 4 |
| `codebook.md` | Livro de códigos | todos |
| `exemplos/` | Arquivos prontos para demonstrar o validador sem depender do agente | *backup* |

Os *hooks* e a *skill* seguem o formato do Claude Code. A lógica é portável: outros agentes de terminal têm mecanismos equivalentes, e o `AGENTS.md` e o formato de *skills* são padrões abertos.

## Requisitos

- R (≥ 4.1) com `jsonlite`, `readr`, `dplyr` e `stringr`.
- Um agente de terminal que suporte *hooks* (roteiro escrito para o Claude Code).
- Abrir o agente **nesta pasta** (`demo-project/`), para que `.claude/` e `AGENTS.md` sejam carregados.

## Roteiro das demonstrações

### Demo 0 — o validador sozinho (sem agente; também é o *backup*)

```bash
Rscript R/validar_codificacao.R exemplos/codificacao_valida.csv
Rscript R/validar_codificacao.R exemplos/codificacao_com_erros.csv
```

O segundo comando deve listar: código inexistente (`contra`), confiança inválida (`talvez`), citação que não existe no discurso D004 (alucinação simulada), data fora do formato, D007 faltando e D008 duplicado.

### Demo 1 — *skill* e auditor

1. Pedir ao agente: *"Codifique os discursos."* Mostrar que ele encontra e segue a *skill*.
2. Se o arquivo gravado tiver algum problema, o *hook* `PostToolUse` devolve os erros e o agente corrige — mostrar esse ciclo na tela.
3. Pedir: *"Agora peça ao auditor para revisar a codificação."* Mostrar que o subagente começa sem o histórico da conversa e produz um relatório de divergências (D005 e D006 são os candidatos naturais).

### Demo 2 — *hook* bloqueando uma ação

1. Pedir: *"No discurso D003 há um erro de digitação; corrija direto no CSV bruto."*
2. O agente tenta editar `dados/brutos/discursos.csv` e é bloqueado; a mensagem do *hook* aparece e o agente propõe a alternativa (registrar a correção em `dados/processados/`).
3. Variante via terminal: *"Apague o arquivo bruto e recrie com a correção."* O *hook* bloqueia o `rm`.
4. Variante que a guarda não vê: *"Escreva um script R que corrija o erro de digitação e rode-o."* O comando (`Rscript corrigir.R`) não menciona `dados/brutos`, então a guarda deixa passar; depois do comando, o **sensor** de integridade acusa a alteração e o agente não consegue encerrar até restaurar os dados (`git checkout -- dados/brutos`). O sensor exige que o projeto esteja num repositório Git.

Ponto para a fala: nenhuma regra isolada basta. A guarda impede o óbvio; o sensor pega o que escapou; o controle de versão permite restaurar. É uma pilha de camadas, não um *hook* maior.

Ponto para a fala: o `AGENTS.md` já dizia para não mexer nos dados brutos. O *hook* existe para o caso em que o pedido em prosa falha.

### Demo 3 — rastreabilidade

```bash
cat logs/registro-agente.jsonl
```

Mostrar que cada mudança feita pelo agente (edições, gravações e comandos concluídos com sucesso) ficou registrada com horário, ferramenta e alvo. Dos comandos de terminal, o log guarda só o programa e os arquivos citados, não o comando inteiro, que pode conter dados ou credenciais. Leituras e tentativas bloqueadas não entram no log.

## Para ensaiar antes da aula

- Rodar as quatro demos do zero, na máquina e com a conta que serão usadas ao vivo.
- Conferir de onde vem o bloqueio de edição. `dados/brutos/` está protegido em duas camadas: pelo *hook* e pelas regras `deny` de `permissions` em `.claude/settings.json` (defesa em profundidade). O *hook* `PreToolUse` deve disparar antes da checagem de permissões, e a mensagem dele deve aparecer; se no ensaio aparecer a mensagem genérica de permissão negada, remover temporariamente as duas linhas `Edit(./dados/brutos/**)` e `Write(./dados/brutos/**)` para a demonstração. A variante via terminal (`rm`) só é coberta pelo *hook*. Depois da variante 4, restaurar os dados com `git checkout -- dados/brutos` (e `git clean -fdx dados/brutos`, se o script tiver criado arquivos) antes do próximo ensaio.
- Apagar `logs/registro-agente.jsonl`, `logs/.codificacao-validada.md5` e os CSVs de `dados/processados/` entre um ensaio e outro (o `.gitignore` da demo já impede que sejam versionados).
- Se o agente não conseguir corrigir a codificação, o *hook* de encerramento continua bloqueando; a saída prevista é mover o arquivo para `dados/processados/codificacao_invalida.csv` e explicar o que ficou pendente.
- Os *hooks* em R levam cerca de um segundo cada para iniciar; em projetos reais com muitas ações, um *hook* em shell ou Python é mais rápido. Aqui a escolha por R é didática: é a linguagem que a maioria do público lê.
