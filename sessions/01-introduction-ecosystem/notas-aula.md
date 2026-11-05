# Sessão 1: Introdução aos Agentes de IA — Conceitos, Modelos e Ecossistema

Roteiro do instrutor para a primeira sessão expositiva (1h30). Formato: bloco por tópico, com cues de tempo, pontos de ênfase, exemplos para apoio da fala e perguntas de engajamento. Alinhado a [llm-agents-for-research-syllabus.qmd](../../llm-agents-for-research-syllabus.qmd), Seção 4, Sessão 1 (os blocos 1 a 5 correspondem aos itens 1 a 5 da ementa). Sessão estritamente conceitual — nenhuma habilidade prática é ensinada aqui (fica para a Sessão 2).

Visão de conjunto, casos-âncora e checklist de preparação: [docs/plan/plano-geral.md](../../docs/plan/plano-geral.md). Referências citadas: [referencias.md](../../referencias.md).

**Distribuição de tempo (90 min):**

| Bloco | Duração | Conteúdo |
|---|---|---|
| Abertura | 5 min | Boas-vindas, objetivos de aprendizagem, enquete rápida |
| 1. LLMs como Agentes | 20 min | Do chat ao loop de execução; três componentes; definição operacional |
| 2. Panorama de Modelos e Ferramentas | 15 min | Famílias de modelos; agentes de terminal e de editor; o ecossistema R |
| 3. Benefícios, Vantagens e Custos | 15 min | Onde vale a pena; evidência sobre produtividade; como estimar custo |
| 4. O *Harness*: Isolamento e Containerização | 15 min | Permissões, *sandbox*, raio de dano |
| 5. Prosa vs. Restrições Determinísticas | 15 min | Julgamento do modelo vs. regra fixa; o problema da validade da medida |
| Encerramento | 5 min | Tese da sessão, ponte para a Sessão 2 |

---

## Abertura (5 min)

- Apresentação rápida dos três ministrantes e do formato: Sessão 1 é conceitual, Sessão 2 é demonstração.
- Mostrar os cinco objetivos de aprendizagem da ementa (§2) em um slide.
- **Enquete de mão levantada** (ou formulário), com três perguntas:
  1. Quem já usou um chatbot (ChatGPT, Claude, Gemini) na pesquisa?
  2. Quem já usou um agente que roda comandos ou edita arquivos no seu computador?
  3. Quem já usou IA para classificar ou codificar dados que entraram numa análise?
- **Âncora de comparação**: numa pesquisa com 1.260 cientistas sociais quantitativos (fev.–mar. de 2026), 81% já tinham usado chatbots na pesquisa, mas só 20% usavam agentes regularmente; entre cientistas políticos, 25%. Usuários de agentes postaram 50% mais *working papers*, mas não submeteram mais artigos a periódicos (Lyttelton, Massenkoff e Wilmers, 2026). Guardar esse último dado: ele volta no bloco 3.

---

## Bloco 1 — LLMs como Agentes (20 min)

**Objetivo do bloco:** a turma sai entendendo por que "agente" não é sinônimo de "chatbot mais esperto", e consegue nomear os três componentes que distinguem um agente.

### 1.1 Gancho (3 min)

Comece perguntando à turma, sem introduzir jargão ainda:

> "Quem aqui já usou um LLM para revisar um texto ou tirar uma dúvida pontual? E quem já pediu para um LLM *executar* uma tarefa de várias etapas sozinho — por exemplo, coletar dados de várias fontes, organizar numa planilha e sinalizar inconsistências, sem você intervir a cada passo?"

A resposta esperada é: quase todos levantam a mão na primeira pergunta, poucos na segunda. Esse gap é o tema do bloco.

**Ponto de ênfase:** não é sobre o modelo ser "mais inteligente". É sobre uma mudança de arquitetura — de uma interação síncrona e supervisionada para um *loop* de execução com autonomia delimitada.

### 1.2 Limitações do paradigma de chat na pesquisa acadêmica (4 min)

Talking points:

- No modo chat, cada resposta depende de o pesquisador formular o próximo prompt. Isso funciona bem para tarefas de uma etapa (resumir, traduzir, explicar), mas degrada rapidamente em tarefas que exigem múltiplas etapas dependentes (coletar → limpar → codificar → validar).
- O chat não vê o seu computador: não abre o arquivo, não roda o script, não confere se o resultado bate. Quem copia, cola, roda e confere é você.
- **Caso-âncora A (discursos parlamentares)**: codificar 2.000 discursos segundo um livro de códigos. No modo chat, o pesquisador cola um trecho, pede a codificação, copia o resultado, cola o próximo — o humano é o *orquestrador* do loop. Com um agente, ele itera sobre o corpus sozinho, aplicando o mesmo protocolo, grava o resultado num arquivo, roda um script de checagem e só volta ao pesquisador para validação de amostra ou quando encontra ambiguidade.

**Pergunta para a turma:** "Que tarefa da pesquisa de vocês hoje segue exatamente esse padrão — vocês fazendo manualmente o que poderia ser um loop?" (Colher 1–2 respostas, sem aprofundar.)

### 1.3 Componentes centrais de um agente (6 min)

Apresentar os três componentes como resposta à pergunta de abertura:

1. **Raciocínio iterativo** — o modelo não produz uma resposta final de uma vez; ele avalia o estado atual da tarefa, decide o próximo passo, executa, observa o resultado e reavalia. É um ciclo, não uma chamada única.
2. **Memória e contexto** — distinguir o contexto da tarefa em andamento (a "janela de contexto", que é finita e se degrada quando fica cheia) da memória persistente entre sessões (arquivos como `AGENTS.md`, notas de projeto, decisões metodológicas registradas). Plantar aqui a ideia de **gerenciamento de contexto**, que volta na Sessão 2.
3. **Uso de ferramentas (*tool calling*)** — o agente não só "pensa em texto": ele invoca ferramentas externas (rodar código, ler e editar arquivos, consultar uma API, buscar na web) e usa o resultado *real* dessas ferramentas para decidir o próximo passo.

**Definição operacional para o slide** (Simon Willison, 2025): *"um agente é um LLM que roda ferramentas em loop para atingir um objetivo"*. Complementar com a distinção da Anthropic (*Building Effective Agents*, 2024) entre **fluxos de trabalho** (caminho definido pelo programador) e **agentes** (o modelo decide o caminho) — na pesquisa, muitas vezes queremos algo no meio.

**Ponto de ênfase:** a combinação dos três é o que separa um agente de um chatbot com prompt longo. Um chat "ajustado" para parecer autônomo, mas sem loop de execução real e sem ferramentas verificáveis, não é um agente.

### 1.4 Exercício de mesa: o modelo não age, ele pede (3 min)

Ideia emprestada do workshop da Australian Political Studies Association (2026), que encena o funcionamento do modelo com papel e dados. Dois voluntários:

- o **"modelo"** só pode escrever pedidos num cartão ("leia o arquivo X", "rode o script Y");
- o **"harness"** executa o pedido, se for permitido, e devolve o resultado.

Perguntas para fechar: quem decide o que é permitido? (o *harness*); quem guarda o que já foi feito? (arquivos e registros, não o modelo); onde deve ficar a regra que não pode falhar? (no *harness*, não no pedido). O exercício prepara os blocos 4 e 5.

### 1.5 Um exemplo concreto, sem demonstração (4 min)

Contar, em forma de narrativa, o relato de Scott Cunningham (Baylor; autor de *Causal Inference: The Mixtape*): em meados de novembro de 2025 ele passou a usar um agente de terminal (Claude Code) na pesquisa empírica e, desde então, escreveu mais de 50 textos numerados sobre o tema no Substack. O caso mais útil para a ciência política: ele reclassificou, com um modelo barato via API em lote, os 305 mil discursos do Congresso dos EUA sobre imigração de um artigo publicado na *PNAS*, por cerca de US$ 11 por rodada; a concordância discurso a discurso com a codificação original foi de 69%, mas as tendências agregadas ficaram quase idênticas (série "Claude Code", posts 15 a 22, fev. 2026). Depois, leu Ludwig, Mullainathan e Rambachan e concluiu que rótulos de LLM exigem amostra de validação humana. Em março de 2026 falou sobre o tema ao *Board of Governors* do Federal Reserve. Pontos a extrair:

- O ganho não veio de o modelo "saber economia", mas de ele executar, observar e corrigir dentro do projeto.
- O próprio Cunningham insiste que o ganho é maior para quem já tem expertise para avaliar o resultado — e alerta para o risco de erosão dessa expertise. Isso prepara o bloco 5.

**Transição para o Bloco 2:** "Se um agente é um modelo rodando ferramentas em loop, as próximas perguntas são: qual modelo, e dentro de qual ferramenta?"

---

## Bloco 2 — Panorama de Modelos e Ferramentas (15 min)

**Objetivo do bloco:** a turma consegue situar os nomes que ouve (Claude, GPT, Gemini, DeepSeek, Claude Code, Codex, Cursor...) em duas camadas distintas: o **modelo** e a **ferramenta/harness** que o envolve.

**Aviso ao instrutor:** versões e preços mudam em semanas. Os slides trazem os nomes vigentes em outubro de 2026, com o carimbo "out/2026"; conferir tudo na véspera da aula. Fontes oficiais e datas: `docs/research/2026-10-05_code-as-policy-modelos-harness.md`, bloco 2. Datas já conhecidas: o GPT-5.5 sai do ChatGPT e do Codex em 14/10/2026; o Claude Haiku 4.5 pode ser aposentado a partir de 15/10/2026.

### 2.1 Duas camadas: modelo e ferramenta (3 min)

- **Modelo**: o LLM propriamente dito (pesos treinados). Acessado via aplicativo (assinatura) ou via API (cobrança por uso).
- **Ferramenta/harness**: o programa que dá ao modelo acesso a arquivos, terminal e ferramentas, e que controla permissões. A mesma ferramenta pode rodar modelos diferentes, e o mesmo modelo se comporta de forma diferente em ferramentas diferentes.
- Analogia para a turma: o modelo é o motor; a ferramenta é o carro — com freio, cinto e retrovisor (ou sem eles).

### 2.2 Famílias de modelos (5 min)

| Família | Tipo | O que importa para a pesquisa |
|---|---|---|
| Claude (Anthropic): Opus 5.5, Sonnet 5.5, Haiku 4.5 | Fechado | Forte em programação e tarefas agênticas longas; base do Claude Code |
| GPT (OpenAI): GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna | Fechado | Amplo ecossistema; base do Codex; o Luna é muito barato para processamento em lote |
| Gemini (Google): 3.8 Flash, 3.1 Pro (*preview*) | Fechado | Janelas de contexto muito longas; integração com Google Workspace; base do Gemini CLI e do Antigravity |
| DeepSeek V4, Qwen3.8, Kimi K3, GLM | Pesos abertos (em geral) | Custo baixo por token; podem rodar localmente ou em provedores terceiros |
| Mistral, Gemma e outros | Pesos abertos | Rodar localmente (ex.: via Ollama) — relevante para dados sensíveis |

Pontos de ênfase:

- **Aberto vs. fechado importa para replicação**: modelos fechados são atualizados e descontinuados pelo fornecedor; uma versão de pesos abertos, registrada, pode ser rodada de novo daqui a cinco anos (Spirling, 2023; Barrie, Palmer e Spirling, 2025).
- **Dados sensíveis** (entrevistas, dados identificados) pesam a favor de modelos locais ou de contratos institucionais com garantias de não uso para treino — gancho para o comitê de ética.

### 2.3 Agentes de terminal e de editor (5 min)

- **Terminal**: Claude Code, Codex CLI, Gemini CLI, OpenCode (aberto, aceita vários provedores), goose (aberto, doado à Linux Foundation).
- **Editor/IDE**: Cursor, VS Code com Copilot, Positron Assistant (Posit — relevante para quem usa R).
- **Aplicativos de desktop com agente**: os aplicativos dos próprios fornecedores já trazem modos agênticos que operam arquivos locais — porta de entrada para quem não usa terminal.
- **Diferença para o chatbot**: esses programas leem a pasta do projeto, rodam scripts, veem erros e corrigem. O chat só vê o que você cola.

### 2.4 Para quem usa R (2 min)

Mencionar, sem demonstrar, que o ecossistema R já tem peças para isso: `ellmer` (chamar LLMs e definir ferramentas a partir do R), `mall` (aplicar LLMs a colunas de um *data frame*), `mcptools` e `btw` (expor a sessão R a um agente via MCP). O público do DCP usa muito R; vale deixar claro que não é preciso migrar para Python.

**Padronização**: ao longo de 2025 surgiram padrões abertos — MCP (conexão com ferramentas), `AGENTS.md` (instruções de projeto) e *Agent Skills* (instruções reutilizáveis). MCP e `AGENTS.md` foram doados à Agentic AI Foundation (Linux Foundation) em dezembro de 2025. Consequência prática: o que se aprende na Sessão 2 não fica preso a um fornecedor.

---

## Bloco 3 — Benefícios, Vantagens e Custos (15 min)

**Objetivo do bloco:** a turma sabe reconhecer quando vale configurar um agente (Objetivo 1 da ementa) e sabe estimar, em ordem de grandeza, quanto custa.

### 3.1 Onde agentes ajudam — e onde não (5 min)

Critério simples para o slide: **vale automatizar quando a tarefa é repetitiva, volumosa e verificável**.

| Tende a valer a pena | Tende a não valer |
|---|---|
| Limpeza e padronização de bases (TSE, INEP, IPEA) | Tarefa feita uma única vez, em 10 minutos, à mão |
| Classificação de milhares de documentos com livro de códigos | Julgamento teórico central do trabalho |
| Organização e triagem de pastas extensas de PDFs | Casos em que não há como checar o resultado |
| Transcrição e pré-codificação de entrevistas | Dados que não podem sair da máquina, sem modelo local |
| Reescrever e depurar código de análise; replicar um artigo | Escrita do argumento substantivo |

### 3.2 O que a evidência diz sobre produtividade (5 min)

Apresentar a evidência com honestidade — ela é mista e muda rápido:

- **METR (jul. 2025)**: ensaio randomizado com 16 desenvolvedores experientes em 246 tarefas reais — com IA, foram **19% mais lentos**, embora *acreditassem* ter sido 20% mais rápidos. Em fev. 2026, a METR declarou esse resultado desatualizado: ganhos agora parecem prováveis, mas o desenho ficou comprometido porque muitos desenvolvedores se recusaram a trabalhar sem IA.
- **Cientistas sociais (Lyttelton, Massenkoff e Wilmers, 2026)**: usuários de agentes produzem mais *working papers* e iniciam mais projetos, mas não submetem mais a periódicos — mais produção não é, automaticamente, mais ciência publicada. Também há desigualdade na adoção: nomes tipicamente masculinos adotam agentes a mais que o dobro da taxa de nomes tipicamente femininos; universidades de elite, 40% a mais. Bom gancho para quem estuda desigualdade.
- **Lição**: a percepção de ganho é um mau estimador do ganho. Medir, não confiar na sensação.

### 3.3 Modelos de cobrança e ordem de grandeza (5 min)

- **Assinatura de aplicativo** (valor mensal fixo, com limites de uso): previsível, bom para uso interativo diário.
- **API por token** (paga-se por milhão de tokens de entrada e de saída): bom para processamento em lote; exige cuidado com limites de gasto.
- Regra de bolso: 1 token ≈ 3/4 de palavra em inglês; em português um pouco menos.
- **Exemplo de conta no quadro** (caso-âncora A): 2.000 discursos × ~1.500 tokens de entrada + ~100 de saída ≈ 3,2 milhões de tokens. Multiplicar pelo preço vigente por milhão de tokens do modelo escolhido. Referência de outubro de 2026, para 1.000 documentos de ~2.000 tokens com saída curta: ~US$ 0,30 (GPT-6 Luna), ~US$ 2 (Gemini 3.8 Flash), ~US$ 6 (Claude Sonnet 5.5 ou GPT-6.1 Sol), ~US$ 12 (Claude Opus 5.5), ~US$ 30 (GPT-6 Astra); metade disso com *batch*. Transcrever 10 h de áudio: US$ 1,80 a 3,60 via API, ou zero com Whisper local. Premissas do cálculo: `docs/research/2026-10-05_code-as-policy-modelos-harness.md`, seção 2.6. Converter para reais na semana da aula e comparar com o valor de uma bolsa de mestrado.
- Modelos com raciocínio ligado podem multiplicar os tokens de saída; o tokenizador novo do Claude gera cerca de 30% mais tokens para o mesmo texto.
- **Custo escondido**: o tempo de verificação humana. Sempre orçar o tempo de validar uma amostra.

---

## Bloco 4 — O *Harness* do Agente: Isolamento e Containerização (15 min)

**Objetivo do bloco:** a turma entende que a segurança e a confiabilidade de um agente dependem mais do ambiente em que ele roda do que do modelo (Objetivo 2 da ementa).

### 4.1 O que é o *harness* (5 min)

- Definir *harness* como o ambiente que envolve o modelo e viabiliza o loop: onde o agente roda, quais permissões de leitura/escrita ele tem, que grau de isolamento existe e quem controla o fluxo (o agente decide sozinho quando parar, ou há pontos de checagem humana obrigatórios?).
- Os modos de permissão típicos: perguntar antes de cada ação; aprovar automaticamente leituras e perguntar em escritas; autonomia total. **Autonomia total só dentro de um ambiente isolado.**

### 4.2 Raio de dano e containerização (5 min)

- Pergunta para o slide: *"Qual é o pior comando que esse agente poderia rodar, e o que ele destruiria?"* Esse é o raio de dano.
- Containerização/*sandbox*: rodar o agente dentro de um contêiner (Docker, *dev container*) ou de uma máquina virtual na nuvem em que só a pasta do projeto está montada. Se algo der errado, apaga-se o contêiner; o computador do pesquisador fica intacto.
- **Caso-âncora C (dados públicos)**: um agente baixando e limpando dados do TSE precisa de internet e de escrita na pasta do projeto — e de mais nada. Não precisa ver a pasta de documentos pessoais, as chaves de outras contas ou o e-mail.

### 4.3 A "tríade letal" (5 min)

Apresentar o conceito de Simon Willison (2025): um agente fica vulnerável a ser manipulado (*prompt injection*) quando combina **(1) acesso a dados privados, (2) exposição a conteúdo não confiável** (páginas web, PDFs baixados, e-mails) **e (3) capacidade de se comunicar com o exterior**. Um PDF malicioso pode conter instruções escondidas que o modelo trata como ordens.

- Na pesquisa: raspar sites e ler PDFs de terceiros é exatamente "conteúdo não confiável". Se o mesmo agente tem acesso aos dados sigilosos de entrevistas e à internet, as três pernas estão presentes.
- Regra prática: **corte pelo menos uma das três pernas**. Gancho para MCP e segurança na Sessão 2.

---

## Bloco 5 — Instrução em Prosa vs. Restrições Determinísticas (15 min)

**Objetivo do bloco:** a turma consegue distinguir quando confiar no julgamento do modelo e quando impor uma regra fixa (Objetivo 3 da ementa). É a ponte conceitual para a Sessão 2.

### 5.1 Duas formas de controlar um agente (4 min)

| | Instrução em prosa | Restrição determinística |
|---|---|---|
| Exemplo | "Por favor, não altere os dados brutos." | Um script que bloqueia qualquer escrita em `dados/brutos/` |
| Quem decide | O modelo, a cada vez | O código, sempre da mesma forma |
| Garantia | Probabilística — funciona quase sempre | Determinística — funciona sempre |
| Serve para | Julgamento, estilo, ambiguidade | Integridade, formato, segurança, registro |

**Ponto de ênfase:** instrução em prosa é um pedido; restrição determinística é uma regra. Um pedido pode ser esquecido quando o contexto enche, quando o modelo "acha" que tem uma boa razão, ou quando uma instrução maliciosa num PDF manda o contrário.

### 5.2 *Code as policy*: dois sentidos do termo (2 min)

Quem procurar o termo vai cair em Liang et al. (2022), "Code as Policies", da robótica: lá, o LLM *gera* o programa que controla o robô, e o código gerado é a política. No uso atual com agentes, próximo de *policy as code* em infraestrutura, somos nós que *escrevemos* em código as regras que limitam o modelo. O que une os dois sentidos: a regra que vale é a que roda. Citação útil da documentação do Claude Code: as regras de permissão são impostas pela ferramenta, não pelo modelo.

### 5.3 Por que a pesquisa empírica exige previsibilidade em certos pontos (5 min)

Três problemas metodológicos que a turma precisa conhecer:

1. **Variância e replicação**: o mesmo modelo, com o mesmo *prompt*, pode dar respostas diferentes em dias diferentes; fixar a temperatura não resolve (Barrie, Palmer e Spirling, 2025).
2. **"LLM hacking"**: pequenas escolhas de implementação — modelo, redação do *prompt*, temperatura — mudam as anotações a ponto de tornar significativas hipóteses que não são; é um novo grau de liberdade do pesquisador (Baumann et al., 2025).
3. **Validade da medida em análises posteriores**: quando um LLM produz uma variável que entra numa regressão, o erro de classificação não é aleatório e enviesa a estimativa. A saída é combinar a saída do modelo com uma **amostra de validação codificada por humanos** e usar estimadores que corrigem o viés (Egami et al., 2023; Ludwig, Mullainathan e Rambachan, 2025).

Conclusão para o slide: **os pontos do processo que afetam a validade e a replicação — dados brutos, formato das variáveis, registro do que foi feito, amostra de validação — devem ser protegidos por regras, não por pedidos.**

### 5.4 Determinístico não é infalível (2 min)

- Uma regra que proíbe o agente de editar um arquivo não pega um script R, escrito pelo agente, que abre esse mesmo arquivo; para isso é preciso o *sandbox* do sistema operacional (que, no Claude Code, não funciona no Windows nativo, só com WSL2).
- Um *hook* local do Git se pula com `--no-verify`; por isso a mesma checagem roda de novo no servidor (GitHub).
- O *sandbox* não impede que o conteúdo lido vá para o fornecedor do modelo.
- Lição: **defesa em camadas** — *harness*, Git, servidor, revisão independente. A Sessão 2 mostra cada camada.

### 5.5 Gancho para a Sessão 2 (2 min)

- "Na próxima sessão vamos ver como essa distinção vira mecanismo: *skills* organizam a prosa; *hooks* impõem as regras; `AGENTS.md` registra o que o agente precisa saber; e separar um agente que executa de outro que audita dá ao trabalho uma revisão independente."
- Mencionar que vamos usar um projeto de demonstração com o caso-âncora A (discursos parlamentares).

---

## Encerramento (5 min)

- Retomar a tese: **o gargalo deixou de ser a execução e passou a ser a verificação.**
- Três frases para levar:
  1. Agente = modelo + ferramentas + loop; o *harness* decide o que ele pode fazer.
  2. Vale automatizar o que é repetitivo, volumoso e verificável.
  3. O que afeta validade e replicação se protege com regra, não com pedido.
- Perguntas finais.
- Leitura sugerida entre as sessões: Korinek (2025), *AI Agents for Economic Research*, seções introdutórias; e um ou dois textos da série de Cunningham.
