# Plano de preparação das aulas — pesquisa, decisões e pauta (2026-10-06)

Issue: #3. Complementa o [plano geral](plano-geral.md), que continua valendo para o fio condutor, os casos-âncora e o checklist da semana da aula. Este documento reúne o que a pesquisa exploratória de outubro de 2026 mudou, as decisões que propomos e a pauta da reunião dos ministrantes de quinta-feira, 2026-10-08.

Pesquisas completas, com fontes e datas:

- [Cursos e workshops sobre agentes](../research/2026-10-05_cursos-sobre-agentes.md): 25 cursos da indústria, de universidades e para pesquisadores, comparados por tópico.
- [Code as policy, modelos e harnesses](../research/2026-10-05_code-as-policy-modelos-harness.md): hooks e permissões em oito harnesses, o GitHub como camada de política, modelos e preços de outubro de 2026, custos de tarefas típicas.
- [Scott Cunningham](../research/2026-10-06_scott-cunningham.md): o que ele publicou sobre agentes na pesquisa empírica.

---

## 1. O que a pesquisa mostrou

### 1.1 Onde o minicurso se situa

- **Os cursos da indústria** (DeepLearning.AI, Anthropic Academy, Hugging Face, Microsoft, Kaggle, OpenAI, Berkeley, Stanford) concordam no núcleo: o laço do agente com ferramentas, MCP, gestão de contexto (que virou tema próprio em 2026), multiagente e avaliação. Quase todos ensinam a *construir* agentes com *frameworks*, o que não serve ao nosso público.
- **Os cursos para pesquisadores** usam um *harness* pronto (Claude Code, Codex). O mais próximo da nossa ementa é o de Gießen (Gärtner, outubro de 2026, quatro dias): harness, Docker, hooks, permissões e git como camada de proveniência, com cerca de dez vezes a nossa carga horária. Seguem Harvard Bok (sessão avançada de 1h30 com praticamente a lista da nossa Sessão 2), HKS (Svoronos), Princeton (Kenny, o único em ciência política que cita `AGENTS.md`), Konstanz, Ohio State e EUI.
- **Nenhum curso encontrado organiza a aula em torno de "prosa vs. regra determinística".** O que mais se aproxima é o *Claude Code in Action*, da Anthropic, que fala em hooks como "enforcement rules". Esse é o principal diferencial possível do minicurso.
- **Não há curso acadêmico brasileiro, nem em português, sobre agentes de código para pesquisa.** Um texto de divulgação de julho de 2026 fala em "quase silêncio absoluto" da academia brasileira sobre o tema. Público lusófono, dados brasileiros e custos em reais são diferenciais concretos.

### 1.2 Tópicos raros, que vale reforçar

| Tópico | Quem cobre | Situação na nossa ementa |
|---|---|---|
| Modelos e custos comparados | EUI, Blattman, Gießen, Essex | Já previsto (S1, bloco 3); falta atualizar números |
| Harness, sandbox, containerização | Gießen, Konstanz | Já previsto (S1, bloco 4) |
| Segurança e *prompt injection* | Microsoft, Berkeley, Stanford, Gießen; quase nenhum curso para pesquisadores | Previsto como conceito (tríade letal); falta demonstração |
| Deriva de versão do modelo durante o projeto | EUI | Implícito (Barrie, Palmer e Spirling); vale nomear |
| Git como proveniência | Gießen, OSU, HKS, Sant'Anna | Fraco: a ementa trata git só como analogia |
| LLM como instrumento de medida validado contra humano | HKS, EUI, Essex, GESIS | Previsto (amostra de validação da *skill*) |

### 1.3 *Code as policy*: o que muda no conteúdo

- **O termo tem dois sentidos.** Em Liang et al. (2022, robótica), o LLM *gera* o código que controla o robô. No uso atual, próximo de *policy as code*, nós *escrevemos* em código as regras que limitam o agente. O que une os dois: a regra que vale é a que roda. Um slide curto desfaz a confusão, já que quem procurar o termo vai cair no artigo de 2022.
- **A documentação do Claude Code diz isso com todas as letras:** as regras de permissão são impostas pela ferramenta, não pelo modelo. Instrução em `CLAUDE.md` ou `AGENTS.md` muda o que o agente *tenta*, não o que o *harness* permite.
- **Determinístico não é infalível.** Uma regra `deny` de edição não pega um script R que abre o arquivo por conta própria. O sandbox do Claude Code não funciona no Windows nativo (só com WSL2). Um git hook local se pula com `--no-verify`. A lição é defesa em camadas.
- **O GitHub é a camada que não se contorna localmente:** CI, *rulesets* com checks obrigatórios, CODEOWNERS, *push protection* de segredos e revisão obrigatória por outro agente ou pessoa. A revisão por IA é inferencial; o que a torna política é a regra que a exige. O próprio repositório do minicurso é um exemplo vivo: trailer `Agent:` conferido por hook e por CI, e "quem escreve não revisa" (este plano passou por `@codex review`).
- **Vocabulário útil (Böckeler, martinfowler.com, abril de 2026):** *guides* orientam antes da ação, *sensors* observam depois, e cada um pode ser computacional (determinístico: testes, validadores) ou inferencial (revisão por IA). O livro de códigos é um *guide*; o validador é um *sensor* computacional; o auditor é um *sensor* inferencial.

### 1.4 Modelos e custos (outubro de 2026; reconferir na semana da aula)

- Anthropic: Fable 5.1 (US$ 10/50 por milhão de tokens de entrada/saída), Opus 5.5 (4/20, lançado em 22/09), Sonnet 5.5 (2/10), Haiku 4.5 (1/5, aposentadoria possível a partir de 15/10).
- OpenAI: GPT-6 Astra (10/50), GPT-6.1 Sol (2/10), GPT-6 Luna (0,10/0,50). O GPT-5.5 sai do ChatGPT e do Codex em 14/10.
- Google: Gemini 3.8 Flash (0,75/3,75); 3.1 Pro ainda em *preview*.
- Abertos: DeepSeek V4 (MIT), Qwen3.8, Kimi K3, Mistral.
- Assinaturas: Claude Pro (US$ 20) inclui o Claude Code; o Codex está em todos os planos do ChatGPT.
- **Ordem de grandeza:** classificar 1.000 documentos custa de cerca de US$ 0,30 (GPT-6 Luna) a US$ 30 (GPT-6 Astra); transcrever 10 h de áudio, de US$ 1,80 a 3,60 via API, ou zero com Whisper local. **O custo dominante é a validação humana, não a API.**

### 1.5 Scott Cunningham

Leitura integral de cerca de 45 posts da série "Claude Code" (dez. 2025 a mai. 2026) e do repositório MixtapeTools; os posts de jun. a out. de 2026 estão atrás de *paywall* e foram lidos só pelo título e trecho aberto.

- **A tese dele coincide com a nossa**: "The bottleneck in science is no longer production. It is verification." (abr. 2026). E só quem tem expertise detecta os erros: o modelo afirma o erro "with exactly the same confidence" que o acerto.
- **A trajetória dele é o arco "prosa vs. regra" em um caso só.** Em fevereiro, `data/raw` era somente leitura "por convenção" (prosa no `CLAUDE.md`). Em abril, um "disjuntor" escrito numa *skill* (parar depois de três tentativas) não impediu um laço que esgotou os *tokens*. Em agosto, o primeiro *hook* — e a constatação de que um script contorna o *hook*, o que o levou a uma pilha: *hook* + trava do sistema operacional + impressão digital SHA-256 ("The fix is not a bigger hook. It is a stack."). A frase "Prose is not constraints" ele atribui a uma palestra de Paul Goldsmith-Pinkham no NBER (jul. 2026). Esse arco entrou nos slides das duas sessões, e a mesma pilha (guarda + sensor de integridade) entrou no projeto de demonstração.
- **Caso pronto para ciência política**: a reclassificação dos 305 mil discursos do Congresso dos EUA sobre imigração (*PNAS*) por cerca de US$ 11, com 69% de concordância individual e tendências agregadas iguais. Junto com Ludwig, Mullainathan e Rambachan, justifica a amostra de validação humana da *skill* de demonstração.
- **O contexto é uma política implícita**: em 300 agentes, um resumo enviesado da literatura posto no contexto mudou estimador, painel e o tom das conclusões, apesar de um aviso explícito. O que se deixa na pasta orienta o agente.
- **Tensão para a turma de pós-graduação**: a IA ajuda mais os menos experientes, mas só os experientes verificam; ele proibiu IA nos próprios cursos de 2026.
- **Lição de formato de demonstração**: gerar ao vivo algo verificável na hora (um *deck* sobre um artigo conhecido) convence mais do que "a IA escreveu um artigo".
- **Correções à bibliografia**: não há livro *AI Agents for Research Workers* (é o título da palestra no Fed, segundo a Forbes); "harness", no uso dele, é um painel de checagem da pesquisa, não o *harness* do agente — convém avisar a turma.

---

## 2. Decisões propostas (para validar na quinta)

1. **Tese central explícita: "prosa orienta, regra garante".** Ela já está no bloco 5 da Sessão 1 e no bloco 2 da Sessão 2; propomos que vire o título do curso nos slides e o eixo da divulgação, já que é o diferencial que nenhum outro curso tem.
2. **Acrescentar a camada GitHub à Sessão 2** (dentro do bloco 4, "`AGENTS.md` e reprodutibilidade", sem tópico novo na ementa): git como proveniência, CI e checks obrigatórios, "quem escreve não revisa". Demonstração com este próprio repositório. Mantém a decisão de não exigir git dos participantes: mostra-se o mecanismo, não se ensina o comando.
3. **Demonstração "pedir vs. travar"** como abertura do bloco de hooks: a mesma ordem, primeiro só com o `AGENTS.md`, depois com o hook. Já é possível com o projeto de demonstração.
4. **Demonstração de *prompt injection* inofensiva** no bloco de segurança: um PDF com uma instrução escondida, lido pelo agente. Precisa ser preparada e ensaiada (item novo do checklist).
5. **Agnosticismo de harness**: mostrar ao menos uma vez a mesma tarefa no Codex, além do Claude Code, com o `AGENTS.md` como contrato portável. Responde à decisão em aberto 1 do plano geral.
6. **Custos em reais**: converter a tabela de custos na semana da aula e compará-la com o valor de uma bolsa CAPES de mestrado.
7. **Cortar**: construção de agentes com *frameworks*, construção de servidor MCP, *deploy*. Ficam como trilha pós-curso (Hugging Face, Microsoft, Korinek).
8. **Folha de saída ("build kit")**: além do *checklist* já previsto, um modelo de `AGENTS.md` e de *skill* que cada participante adapta à própria pesquisa.
9. **Slides em Quarto Reveal.js**, um arquivo por sessão (`aulas/0X-*/slides.qmd`), renderizados para `docs/`. Primeira versão nesta mesma rodada de trabalho.

## 3. Pauta da reunião de quinta (2026-10-08)

1. **Data, local e formato da aula** — ainda não registrados no repositório. Presencial ou remoto? Os participantes terão internet?
2. **Divisão de blocos e papéis** (fala e operação do terminal), a partir do cronograma do plano geral.
3. **Validar as decisões 1 a 9** acima.
4. **Qual agente e qual conta usar ao vivo** (decisão em aberto 1 do plano geral), e quem ensaia as demonstrações.
5. **Revisão dos slides** (primeira versão no repositório): o que cortar, o que falta, estilo.
6. **Lista de leituras na ementa** (decisão em aberto 2 do plano geral) e se a ementa precisa ser recompilada.
7. **Próximos passos e prazos** até a aula.

## 4. Cronograma de preparação (a ajustar quando a data da aula for definida)

| Quando | O quê | Quem |
|---|---|---|
| até 2026-10-07 | Pesquisa, plano, roteiros atualizados e primeira versão dos slides no repositório | Tales, com agentes |
| 2026-10-08 | Reunião: decisões e divisão de blocos | os três |
| semana seguinte | Ajustar slides às decisões; preparar a demo de *prompt injection* e a demo no Codex | a definir |
| semana da aula | Reconferir modelos e preços; ensaio completo das demos numa máquina limpa; gravar *backup*; folha de saída | a definir |

## 5. Riscos

- **Números envelhecem em semanas.** Modelos e preços dos slides levam a data "out/2026" e precisam ser reconferidos na véspera.
- **Demonstração ao vivo trava.** Mitigação já prevista: *backup* gravado e a Demo 0, que roda sem agente.
- **Máquina Windows na demonstração.** O sandbox do Claude Code não funciona no Windows nativo; usar WSL2, ou mostrar o sandbox no Codex.
- **Parecer propaganda de fornecedor.** Mitigação: decisão 5 (dois harnesses) e ênfase nos padrões abertos.
