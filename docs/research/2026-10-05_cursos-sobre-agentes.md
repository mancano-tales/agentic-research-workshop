# Cursos, workshops e materiais didáticos sobre agentes de IA: panorama para o minicurso do DCP-USP

Pesquisa exploratória feita em 2026-10-05 para o minicurso "Agentes de IA para Pesquisa" (Seminário Discente DCP-USP 2026). Fontes: busca e leitura de páginas oficiais. O texto marca o grau de verificação de cada fonte:

- **verificado**: a página oficial (ou o PDF do programa) foi lida;
- **parcial**: confirmado só por snippet de busca ou página secundária, porque a página oficial recusou o acesso (HTTP 403) ou está atrás de paywall;
- **não verificado**: há indícios, mas nenhuma fonte confirmou.

---

## Parte A. Cursos gerais e da indústria

### A1. DeepLearning.AI + Anthropic: "Claude Code: A Highly Agentic Coding Assistant" (verificado)
- **Autor:** Elie Schoppik (Anthropic). **URL:** <https://deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant>
- **Data:** a página informa 17/08/2026 (pode ser data de atualização). **Formato:** curso curto, cerca de 2 h, 10 vídeos e 1 tarefa avaliada (PRO). **Público:** intermediário (desenvolvedores).
- **Tópicos:** explorar uma base de código; desenvolver, testar, refatorar e depurar; worktrees paralelos; integração com GitHub (issues, PRs, revisão); hooks; servidores MCP (Playwright, Figma); transformar notebook em dashboard.
- **Prática:** sim, com três projetos (chatbot RAG, notebook de e-commerce, app a partir de Figma).
- **Distintivo:** é o único curso curto de grande escala que mostra worktrees, hooks e GitHub juntos ([página](https://deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant)).

### A2. DeepLearning.AI + Anthropic: "Agent Skills with Anthropic" (verificado por busca e páginas DLAI)
- **URL:** <https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/>. **Formato:** cerca de 2h19, 10 vídeos e 1 tarefa avaliada; nível iniciante ([anúncio na comunidade](https://community.deeplearning.ai/t/new-course-enroll-in-agent-skills-with-anthropic/887920)).
- **Tópicos:** criar skills reutilizáveis; combinar skills com MCP e subagentes; exemplos como gerar questões de prática a partir de notas de aula, analisar séries temporais e montar fluxos de revisão de código e "research agents".
- **Distintivo:** os exemplos são acadêmicos (notas de aula, guias de estudo), o que facilita adaptar para o público do DCP.

### A3. DeepLearning.AI + Anthropic: "MCP: Build Rich-Context AI Apps with Anthropic" (verificado)
- **URL:** <https://learn.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic>. **Formato:** cerca de 1h38, 11 vídeos e 7 notebooks; nível intermediário.
- **Tópicos:** arquitetura cliente-servidor do MCP; tools, resources e prompts; construir um servidor MCP e conectá-lo ao Claude Desktop; criar um host com vários clientes ([página](https://deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic)).

### A4. DeepLearning.AI: "Agentic AI" (Andrew Ng) (verificado)
- **URL:** <https://deeplearning.ai/courses/agentic-ai/>. **Formato:** 5 módulos, 31 vídeos e 3 tarefas avaliadas, cerca de 10 h por semana durante 2 semanas ([Coursera](https://www.coursera.org/learn/dlai-agentic-ai)).
- **Tópicos:** quatro padrões de projeto (reflexão, uso de ferramentas, planejamento, multiagente); avaliação e análise de erros; o agente de pesquisa é o fio condutor.
- **Distintivo:** dá peso a **evals e análise de erro**, que outros cursos tratam pouco.

### A5. Anthropic Academy (Skilljar) (verificado)
- **URL:** <https://anthropic.skilljar.com/>. Plataforma gratuita, com certificado. Segundo [uma fonte secundária](https://pasqualepillitteri.it/es/news/373/anthropic-academy-cursos-gratuitos-claude), foi lançada em março de 2026.
- **Catálogo relevante:** Claude Code 101, **Claude Code in Action**, Introduction to MCP, MCP Advanced Topics, **Introduction to Agent Skills**, **Introduction to Subagents**, Introduction to Claude Cowork, **AI Fluency: Framework & Foundations** e as versões de AI Fluency para Educators, Students e outros públicos, além de AI Capabilities and Limitations e Teaching AI Fluency.
- **Claude Code in Action** ([página](https://anthropic.skilljar.com/claude-code-in-action)): plan mode, compactação de contexto, rewind, CLAUDE.md, skills, modos de permissão, **hooks como "regras de enforcement"**, rotinas agendadas, modo headless, revisão de PR no GitHub, "gate turns on test results" e plugins.
- **AI Fluency** ([página](https://anthropic.skilljar.com/ai-fluency-framework-foundations)): framework dos **4D** (Delegation, Description, Discernment, Diligence), de Joseph Feller (UCC) e Rick Dakan (Ringling). Serve como esqueleto conceitual para quem não programa.
- **Distintivo:** é a fonte primária mais próxima da Sessão 2 do DCP (skills, hooks, permissões, subagentes).

### A6. Hugging Face: Agents Course, MCP Course e Context Course (verificado)
- **Agents Course** (<https://huggingface.co/learn/agents-course/unit0/introduction>): Unit 1, fundamentos (ciclo Thought-Action-Observation, chat templates, tokens especiais); Unit 2, frameworks (smolagents, LangGraph, LlamaIndex); Unit 3, casos de uso; Unit 4, tarefa final em benchmark com leaderboard. Bônus: fine-tuning para function calling, **observabilidade e avaliação**, agentes em jogos. Carga de 3 a 4 h por semana; exige Python.
- **MCP Course** (<https://huggingface.co/learn/mcp-course/unit0/introduction>): parceria com a Anthropic; fundamentos, uma aplicação ponta a ponta e o deploy.
- **Context Course** (<https://huggingface.co/learn/context-course/unit0/introduction.md>): **context engineering para agentes de código** (skills, MCP, plugins, coordenação multiagente, ciclo de vida do agente, agente mínimo). São 6 unidades e o curso pressupõe Claude Code, Codex ou OpenCode instalado. Autores: Ben Burtenshaw e outros.
- **Distintivo:** o Agents Course usa um **leaderboard** como avaliação final. O Context Course parte da frase "an agent is only as good as the context it has".

### A7. Microsoft: "AI Agents for Beginners" (verificado)
- **URL:** <https://github.com/microsoft/ai-agents-for-beginners>. Repositório aberto, multilíngue, com 18 lições.
- **Lições:** introdução; frameworks; padrões de projeto; tool use; RAG agêntico; **agentes confiáveis**; planejamento; multiagente; metacognição; produção; **protocolos (MCP, A2A, NLWeb)**; **context engineering**; **memória**; Microsoft Agent Framework; computer use; deploy; agentes locais; **segurança de agentes**.
- **Distintivo:** é o currículo aberto mais completo em tópicos, mas é centrado em construir agentes com frameworks, não em usar um harness pronto.

### A8. Google + Kaggle: "5-Day AI Agents Intensive" (verificado)
- **URL:** <https://www.kaggle.com/learn-guide/5-day-agents> ([recap do Google](https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap/)). Edição ao vivo em novembro de 2025, com mais de 1,5 milhão de inscritos; nova edição com tema "vibe coding" em 15 a 19/06/2026 ([TechRepublic](https://techrepublic.com/article/news-google-kaggle-ai-agents-course-vibe-coding)).
- **Dias** ([KDnuggets](https://www.kdnuggets.com/kaggle-googles-free-5-day-agentic-ai-course)): (1) intro e "quando uma tarefa precisa de agente"; (2) ferramentas, MCP e human-in-the-loop; (3) context engineering e memória; (4) qualidade (logging, tracing, avaliação); (5) produção e A2A.
- **Formato:** cada dia combina um whitepaper, codelabs (Gemini + ADK), livestream e Discord, e o curso termina com um capstone.
- **Distintivo:** a pergunta "esta tarefa precisa mesmo de um agente?" aparece logo no Dia 1.

### A9. OpenAI Academy: Codex Bootcamp, Codex for Faculty and Researchers e Codex Summer Studio (verificado)
- **Codex Bootcamp** (<https://academy.openai.com/public/resources/codex-bootcamp-2026-09-23>): série ao vivo em três partes. 101 em 23/09 (escopo, contexto, steering, revisão); 201 em 30/09 (contexto compartilhado, aprovações, **skills reutilizáveis**, conexões com ferramentas); 301 em 07/10/2026 (**subagentes, permissões**, Codex SDK).
- **Codex for Faculty and Researchers** ([evento](https://academy.openai.com/public/clubs/higher-education-05x4z/events/codex-for-faculty-and-researchers-lm708a7oum)): webinar de 1 h com foco em contexto, revisão e "manter humanos no controle da qualidade e da reprodutibilidade".
- **Codex Summer Studio** ([GovTech](https://www.govtech.com/education/higher-ed/openai-trains-faculty-and-researchers-to-use-coding-agents)): de 29/07 a 19/08/2026, quatro sessões de 1 h, com trilhas de ensino, pesquisa e departamento. Cada participante traz um projeto próprio e sai com um "build kit" de prompts reutilizáveis.
- **Agents SDK:** não encontrei curso oficial da OpenAI. Existe um curso comercial de terceiros, de Paul Deitel na O'Reilly, em 23/07/2026 ([Deitel](https://deitel.com/2026/06/)).

### A10. Universidades (verificado, salvo indicação)
- **UC Berkeley RDI: LLM Agents MOOC** (outono 2024), **Advanced LLM Agents** (primavera 2025) e **Agentic AI MOOC** (outono 2025), com Dawn Song e Xinyun Chen ([Berkeley RDI Education](https://rdi.berkeley.edu/education); [slides de introdução](https://rdi.berkeley.edu/agentic-ai/slides/introduction_25.pdf)). São cerca de 12 aulas de 2 h sobre raciocínio e planejamento, frameworks, **avaliação, multiagente, segurança**, e aplicações em código, web e descoberta científica. É o mais acadêmico dos cursos, com palestras de pesquisadores.
- **Stanford CS146S "The Modern Software Developer"** (Mihail Eric, outono 2025 e outono 2026): <https://themodernsoftware.dev/>. Dez semanas: anatomia de um agente de código, MCP, context engineering, padrões, terminal, **testes e segurança**, code review, deploy. As tarefas são públicas e o curso traz convidados da indústria. A edição 2026 acrescenta skills e spec-driven development.
- **Stanford CS329Z "Engineering AI Agents"** (Diyi Yang e outros, outono 2026), **parcial**: só tenho fontes secundárias ([Beri](https://www.beri.net/learning/stanford-cs329z-engineering-ai-agents)). Segundo elas, o curso constrói RAG, tools e o loop do zero antes de usar frameworks, e trata de LLM-as-judge, segurança e guardrails.
- **Stanford CS329A "Self Improving AI Agents"**, seminário de pós-graduação ([bulletin](https://bulletin.stanford.edu/courses/2263721)).
- **UMass Lowell COMP 4600/5300 "AI Agents with Claude Code"** (outono 2026), **parcial** ([anúncio](https://www.uml.edu/myuml/submissions/2026/2026-04-15-16-21-07-announcing-a-new-topics-course-ai.aspx)).

---

## Parte B. Cursos e workshops para pesquisadores e cientistas sociais

### B1. Pedro Sant'Anna (Emory): `claude-code-my-workflow` (verificado)
- **URL:** <https://github.com/pedrohcgs/claude-code-my-workflow>. Template que o pesquisador copia (fork) e adapta. Última atualização em 24/08/2026; mais de 1.500 estrelas.
- **Conteúdo:** 18 agentes (proofreader, slide-auditor, r-reviewer, claim-verifier, referees), 61 skills, 37 regras e 11 hooks (pre-commit, bloqueio de git destrutivo).
- **Ideias-chave:** *quality gates* numéricos (commit ≥80, PR ≥90); **QA adversarial** em que um agente crítico e um corretor alternam até não surgir achado novo, com teto de 5 rodadas; workflow que começa pelo plano; verificadores com contexto limpo; auditoria de reprodutibilidade.
- **Público:** economistas e cientistas políticos. É o exemplo mais maduro de "code as policy" aplicado à pesquisa.

### B2. Chris Blattman (UChicago Harris): claudeblattman.com (verificado)
- **URL:** <https://claudeblattman.com/>, com repositório em `chrisblattman/claudeblattman`. Começou em janeiro de 2026; atualizações até abril de 2026.
- **Tópicos:** instalação em Mac e Windows e no VS Code; CLAUDE.md; MCP; **gestão de custos**; gestão de sessão; ciclo prompt-plano-revisão-revisão; assistente executivo (e-mail, agenda); gestão de projetos; estudo de caso de imposto de renda; `/council` (críticos em paralelo); mais de 20 skills para baixar.
- **Distintivo:** foi escrito por quem "nunca escreveu uma linha de código", para trabalhadores do conhecimento sem formação em programação ([about](https://claudeblattman.com/about/)). É o perfil mais próximo do público do DCP.

### B3. Scott Cunningham (Baylor): série "Claude Code" no Substack e Mixtape Sessions (parcial)
- **Série "Claude Code Changed How I Work"** ([parte 1, 13/12/2025](https://causalinf.substack.com/p/claude-code-changed-how-i-work-part); [parte 7, 17/01/2026, sobre slides](https://causalinf.substack.com/p/claude-code-series-part-7-making)): relato de uso em pesquisa empírica com R, Python e Stata, com assinatura de US$ 200 por mês. O conteúdo completo está atrás de paywall.
- **Mixtape Sessions:** **não verificado** que exista um workshop dedicado a Claude Code. A busca mostra que o CodeChella Madrid (maio de 2026), de inferência causal, incluiu uma seção sobre Claude Code em projetos de pesquisa ([SAV](https://ekonom.sav.sk/en/news/codechella-madrid-20261)).

### B4. Anton Korinek: "AI Agents for Economic Research" (verificado)
- NBER WP 34202, de setembro de 2025 (<https://www.nber.org/papers/w34202>), com materiais em <https://www.GenAIforEcon.org>. É uma atualização da série publicada no JEL.
- **Tópicos:** "vibe coding"; construir agentes com LangGraph sem formação em programação; revisão de literatura, código econométrico, coleta de dados e fluxos multietapa.
- **Distintivo:** é um texto-tutorial que pode servir de leitura prévia. O foco está em construir agentes, não em usar um harness.

### B5. Harvard Kennedy School: API-212M "Agentic Data Analysis" (Teddy Svoronos) (verificado)
- **URL:** <https://www.hks.harvard.edu/courses/advanced-quantitative-methods-iii-agentic-data-analysis>. Disciplina de pós-graduação (MPA/ID), baseada em projeto.
- **Tópicos:** dirigir agentes (Claude Code, Codex) em todo o pipeline de análise de políticas, com robustez e comunicação; **LLM como método (classificação de texto)**; *managing cognitive debt*; **verification-first analysis**; reprodutibilidade.
- **Distintivo:** foi o único curso a nomear explicitamente "dívida cognitiva", e trata o LLM ao mesmo tempo como ferramenta e como instrumento de medida.

### B6. Universität Gießen (GGS): "AI-Assisted Empirical Research with Claude Code" (Florian Gärtner) (verificado, PDF do programa)
- **URL:** <https://www.uni-giessen.de/de/fbz/zentren/ggs/veranstaltungen/curriculum/wise2627/syllabi26/syllabus-claude-code>. Quatro dias inteiros, de 15 a 23/10/2026, 3 ECTS, até 15 participantes; doutorandos e pós-docs **sem experiência com terminal ou git**.
- **Tópicos:** como o LLM funciona ("por que esquece", contexto poluído, fabricação); terminal; estrutura de projeto (instruções e convenções); **git como rede de segurança e camada de proveniência**; pipeline até LaTeX/Overleaf; **regras, hooks, permissões, comandos, a diferença entre skills e agentes**; **sandbox (Docker) e modelo local**; contexto e custo; verificação e detecção de fabricação; RAG sobre a própria biblioteca; multiagente; **sessões paralelas com branches e worktrees**; rotinas agendadas; proteção de dados e credenciais.
- **Método:** cada bloco tem input curto, demo ao vivo e exercício guiado, sobre **projetos de exemplo já configurados**, e o curso fecha com um projeto final na pesquisa do próprio aluno.
- **Distintivo:** é o mais próximo da ementa do DCP em tópicos (harness, sandbox, hooks, git), com cerca de 10 vezes mais horas.

### B7. Universität Konstanz: microcredencial "Coding with Claude Code for the Social Sciences" (Lena Janys) (verificado)
- **URL:** <https://afww.uni-konstanz.de/en/node/877>. Dois dias online, em 18 e 19/02/2027, 1 ECTS, €250.
- **Tópicos:** capacidades e limites; chat, Claude Code e skills; formular tarefas; human-in-the-loop e code review; **testes e sandboxes**; ética, privacidade e reprodutibilidade.

### B8. Princeton: CSDP e DDSS (parcial: as páginas devolveram 403; conteúdo vem de snippets de busca)
- **"Skills Workshop: Agentic AI for Political Science Research"** (Christopher Kenny, DDSS), 10/09/2026, 1 h ([CSDP](https://csdp.princeton.edu/events/skills-workshop-agentic-ai-political-science-research)). Trata de Claude Code e Codex trabalhando dentro do projeto, **AGENTS.md e skills reutilizáveis** para codificar convenções e conhecimento de domínio, simulação e um grafo de conhecimento da literatura para revisar rascunhos.
- **"Claude Code I" e "Claude Code II"** (DDSS), em 02/10 e 09/10/2026 ([Claude Code II](https://ddss.princeton.edu/events/2026/claude-code-ii)).
- **Distintivo:** é o único workshop de **ciência política** que cita AGENTS.md pelo nome.

### B9. Harvard Bok Center: série de verão sobre Claude (parcial: 403; dados de snippets)
- "Advanced Claude Code: **Skills, MCPs, Hooks, and Multi-Agent Workflows**", 20/05/2026, 1h30, para docentes que já instalaram o Claude Code ([evento](https://bokcenter.harvard.edu/event/advanced-claude-code-skills-mcps-hooks-and-multi-agent-workflows.md)). Fecha com um capstone em 04/06/2026 sobre Claude Code e Cowork para produzir material de curso e divulgar pesquisa ([evento](https://bokcenter.harvard.edu/event/claude-code-putting-it-all-together-develop-course-content-and-communicate-research)).
- **Distintivo:** a série separa um nível introdutório de um avançado. A sessão avançada, de 1h30, cobre skills, MCP, hooks e multiagente, praticamente a mesma lista da Sessão 2 do DCP.

### B10. Ohio State (PRISM): "AI-Assisted Research Workflow" (Myriam Shiran) (verificado)
- **URL:** <https://polisci.osu.edu/events/myriam-shiran-ai-assisted-research-workflow>. 13/04/2026, 1h30, no Departamento de Ciência Política.
- **Tópicos:** ciclo de vida de um projeto reprodutível: criar o repositório no GitHub, clonar, usar Claude Code e Cowork para planejar, escrever e depurar Python, e chegar a notebooks prontos para publicação. Sem pré-requisito de programação.

### B11. EUI (Florença): "AI applications for social scientists" (Olsson e Valli) (verificado, PDF)
- **URL:** <https://www.eui.eu/Documents/DepartmentsCentres/SPS/Seminars/2026-27-Seminars/OLSSON-VALLI-AI-applications-for-social-scientists-outline.pdf>. Segundo trimestre de 2026-27, seminário semanal de 2 h.
- **Tópicos:** como os LLMs funcionam; **modelos comerciais versus locais; escolhas de modelo, configuração, dados e custo**; fluxos de pesquisa; APIs e modelos locais; **validação contra outras fontes, entre modelos e contra benchmarks humanos**; documentar o uso de IA; ética, dados sensíveis, **dependência de fornecedores comerciais** e **mudança dos modelos durante o projeto**.
- **Distintivo:** foi o único a tratar a deriva de versão do modelo como problema de pesquisa.

### B12. Escolas de métodos (verificado, salvo indicação)
- **Essex Summer School 2026, curso 2B "Generative AI for Social Science Research"** (Maximilian Weber, Mainz), de 20 a 31/07/2026, 35 h ([página](https://essexsummerschool.com/courses/ess-2026-course-list/2b/)). Cobre prompting, sumarização, chain-of-thought, multimodalidade, **um dia de "Agents & Automation"**, fine-tuning e projetos com discursos parlamentares e surveys, usando LangChain, Llama e `rollama`.
- **Essex 3G "Text Analysis for Social Scientists: Utilizing LLM-Assisted Coding"** (Raymond Hicks, Columbia) ([página](https://essexsummerschool.com/courses/ess-2026-course-list/3g/)). É texto-como-dado em R, com "vibe coding" opcional.
- **ECPR Methods School: "Large Language Models for Social Science Research"** (Giovanni Pagano, Milão), de 8 a 15/09/2026, **parcial** (só snippet de busca; página não localizada). Trata de codificação de conteúdo, survey augmentation e desenho experimental.
- **GESIS:** workshop de um dia, "The Methodological Potential of LLMs for Social Science Research" (Julia Romberg), em 29/01/2026 ([bidt](https://en.bidt.digital/event/the-methodological-potential-of-llms-for-social-science-research/)), com discussão de vieses; e o Fall Seminar 2026 "From Embeddings to LLMs" ([GESIS](https://www.gesis.org/gesis-training/news-details/article/gesis-training-overview-june-2026)).
- **Columbia LLM4SS Summer Academy** (Xi Song), de 26/05 a 05/06/2026, com 15 a 20 participantes de **"limited coding experience"** ([página](https://sociology.columbia.edu/node/2577)).
- **ICPSR 2026:** não encontrei curso específico de agentes ou LLMs no programa geral (**não verificado**) ([topical workshops](https://www.icpsr.umich.edu/sites/icpsr/events/2026-icpsr-summer-program-topical-workshops)).

### B13. Associações
- **Australian Political Studies Association, 3rd Workshop on Quantitative Methods**, "Integrating AI into Quantitative Political Research", 11/06/2026 (verificado; [ANU](https://rsss.cass.anu.edu.au/news/3rd-apsa-workshop-quantitative-methods-integrating-ai-quantitative-political-research)). Tem três módulos: (1) como funcionam os modelos de linguagem, **com papel, caneta e dados**; (2) agentes para pesquisa empírica, com verificação e riscos; (3) codificação de texto reprodutível com ferramentas abertas.
- **American Political Science Association (APSA EUA), SPSA e ABCP:** não encontrei short course sobre agentes em 2026 (**não verificado**).

### B14. Outros materiais para pesquisadores
- **Tom Pepinsky (Cornell), "Agentic AI and Social Science Research Practice"**, 23/01/2026 ([post](https://tompepinsky.com/2026/01/23/agentic-ai-and-social-science-research-practice/)). A regra que ele propõe é usar agentes para tarefas que seguem regras e não para gerar respostas, argumentos ou interpretações. Cita como riscos a citação alucinada e o p-hacking automatizado. Dá uma boa provocação para abrir a Sessão 1.
- **"Claude Code for Social Scientists"** (Onour Impram), bilíngue turco/inglês ([GitHub](https://github.com/thegoatpsy/claude-code-for-social-scientists)). Reúne 32 skills de integridade (verificação de DOI, PRISMA, anonimização, pré-registro) para Claude Code e Codex. É um **precedente de curso não anglófono** com conteúdo adaptado, e não só traduzido.

### B15. Iniciativas brasileiras ou em português
- **Não encontrei nenhum curso acadêmico brasileiro sobre agentes de código para pesquisa** em USP, FGV, IESP, Insper, ENAP ou ABCP (**não verificado**, ou seja, a busca não achou nada). O que aparece:
  - FFLCH-USP, "AI Tá On: Inteligência Artificial para Humanidades e Educação" (janeiro de 2025), sobre prompts e IA generativa para docentes e pesquisadores, sem agentes ([Agência FAPESP](https://agencia.fapesp.br/ai-ta-on-inteligencia-artificial-para-humanidades-e-educacao/53734));
  - cursos de mercado ou executivos, como a FIA ([PDF](https://fia.com.br/wp-content/uploads/2025/09/CP-Extensao-Curso-Agentes-de-IA-Revolucao-da-IA.pdf)), "Construção de Agentes de IA" para compras públicas ([PDF](https://inovecapacitacao.com.br/wp-content/uploads/2026/05/CONSTRUCAO-DE-AGENTES-DE-IA-1.pdf)) e "Claude Aplicado" na Unifor ([página](https://unifor.br/web/educacao-continuada/claude-aplicado-ia-que-automatiza-sua-rotina));
  - disciplina de PG em computação, "Grandes Modelos de Linguagem" (UFMG, 2025/2) ([PDF](https://ppgcc.dcc.ufmg.br/wp-content/uploads/2025/06/2025-2_TECC_Grandes_Modelos_de_Linguagem_Rodrygo_Anisio.pdf));
  - pesquisa substantiva sobre LLMs na CP brasileira, por exemplo o viés político dos LLMs comparado ao ESEB 2022, de doutorandos do IESP-UERJ ([SciELO Preprints](https://preprints.scielo.org/index.php/scielo/preprint/view/15668)).
- Um texto de divulgação de 29/07/2026 relata "quase silêncio absoluto" da academia brasileira sobre agentes de código ([Cavichiolli](https://doutoranathalia.com.br/blog/news-768-algo-grande-esta-acontecendo-na-ciencia-mundial-e-o-brasil/)).

---

## 1. Tabela-síntese por tópico

Legenda: **X** = cobre explicitamente; **p** = parcial ou menção; **–** = não encontrado na descrição; **?** = não verificado. A tabela se baseia nas ementas e descrições públicas, não no conteúdo integral dos cursos.

| Curso | Def. agente | Tool use/loop | Modelos e custos | Harness/sandbox | Seg./prompt inj. | Permissões/hooks | Skills | MCP | Memória/contexto | Multiagente/subag. | Avaliação/verif. | Git/repro | Ética/uso acad. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DLAI Claude Code (A1) | p | X | – | X | – | X (hooks) | – | X | X | p (worktrees) | X (testes) | X | – |
| DLAI Agent Skills (A2) | p | X | – | X | – | – | X | X | p | X | – | – | – |
| DLAI MCP (A3) | p | X | – | – | – | – | – | X | p | – | – | – | – |
| DLAI Agentic AI / Ng (A4) | X | X | p | – | – | – | – | – | p | X | X | – | – |
| Anthropic CC in Action (A5) | p | X | – | X | – | X | X | p | X | p | X | X | – |
| Anthropic AI Fluency (A5) | X | – | – | – | – | – | – | – | – | – | X (discernment) | – | X |
| HF Agents Course (A6) | X | X | p | – | – | – | – | – | p | p | X (bônus) | – | – |
| HF Context Course (A6) | p | X | – | X | – | – | X | X | X | X | – | – | – |
| Microsoft for Beginners (A7) | X | X | p | – | X | p | – | X | X | X | p | – | X (trustworthy) |
| Kaggle 5-Day (A8) | X | X | – | p | – | X (HITL) | – | X | X | X | X | – | – |
| OpenAI Codex Bootcamp (A9) | p | X | – | X | – | X | X | X | X | X | X | p | – |
| Berkeley Agentic AI (A10) | X | X | p | p | X | – | – | – | X | X | X | – | X |
| Stanford CS146S (A10) | X | X | p | X | X | – | X | X | X | p | X | X | – |
| Sant'Anna workflow (B1) | – | X | – | X | p | X | X | p | X | X | X | X | X |
| Blattman (B2) | p | X | X | X | p | p | X | X | X | X | X | p | p |
| HKS Svoronos (B5) | p | X | – | X | – | – | – | – | – | – | X | X | X |
| Gießen / Gärtner (B6) | X | X | X | X | X | X | X | p | X | X | X | X | X |
| Konstanz / Janys (B7) | X | X | – | X | X | – | X | – | – | – | X | X | X |
| Princeton / Kenny (B8) | p | X | – | X | – | – | X | ? | X (AGENTS.md) | ? | ? | ? | ? |
| Harvard Bok adv. (B9) | – | X | – | X | – | X | X | X | p | X | ? | ? | ? |
| OSU / Shiran (B10) | – | X | – | X | – | – | – | – | – | – | p | X | p |
| EUI / Olsson-Valli (B11) | X | p | X | – | X | – | – | – | – | – | X | p | X |
| Essex 2B (B12) | p | p | X | – | – | – | – | – | – | p | – | – | p |
| AusPSA workshop (B13) | X | X | – | – | – | – | – | – | – | – | X | X | X |

---

## 2. Consenso, raridades e exclusividades

**Consenso** (aparece em quase todos):
- **Tool use e o ciclo do agente** (pensar, agir, observar): é o núcleo de todos os cursos da indústria e aparece implícito nos de pesquisa.
- **Contexto e memória**: o tema de "context engineering" virou eixo próprio em 2026 (HF Context Course, Kaggle Dia 3, Microsoft lição 12, Claude Code in Action).
- **MCP**: está presente em praticamente todos os cursos da indústria de 2025-26.
- **Multiagente e subagentes**: também quase universal.
- **Avaliação e verificação**: aparece em todos, mas com sentidos diferentes. Na indústria é *evals*, tracing e testes; nos cursos de pesquisa é **verificar se o resultado está certo** (fabricação, interpretação, contra benchmark humano).

**Raros:**
- **Modelos e custos em perspectiva comparada.** Só EUI, Blattman, Gießen e Essex tratam disso. Os cursos da indústria falam do próprio produto.
- **Harness, sandbox e containerização.** Só Gießen (Docker, modelo local) e Konstanz (sandboxes) tratam isso como tema de aula. Stanford CS146S e Microsoft (agentes locais) tocam no assunto.
- **Segurança e prompt injection.** Aparece na Microsoft (lição 18), em Berkeley, Stanford e Gießen. Quase nenhum curso para pesquisadores trata injection; Gießen fala do agente "com acesso total à sua máquina".
- **Hooks, permissões e "enforcement".** Aparecem em Anthropic CC in Action, DLAI Claude Code, Harvard Bok (avançado), Gießen e Sant'Anna. **Nenhum curso enquadra explicitamente** a dicotomia "prosa (CLAUDE.md, skills) versus regra determinística (hooks)" como conceito central. O que mais se aproxima é o Claude Code in Action, que fala em "enforcement rules through hooks".
- **AGENTS.md como padrão entre harnesses:** só Princeton/Kenny cita o nome.

**Exclusivos (ou quase) dos cursos voltados a pesquisa:**
- **Citação alucinada e verificação de referências** (Pepinsky, Impram, Sant'Anna `/verify-claims`, AusPSA).
- **Git como camada de proveniência e reprodutibilidade** (Gießen, OSU, HKS, Sant'Anna). Na indústria, git é tratado só como fluxo de trabalho.
- **LLM como instrumento de medida e validação contra codificação humana** (HKS "text classification", EUI "human benchmarks", Essex, ECPR, GESIS).
- **Deriva do modelo e dependência de fornecedor** (EUI).
- **Dívida cognitiva e o limite entre delegar e interpretar** (HKS, Pepinsky, Gießen "o que delegar e o que manter").
- **Proteção de dados e anonimização** (Gießen, Konstanz, Impram, EUI).
- **Revisão adversarial no papel de parecerista** (Sant'Anna, `/council` de Blattman).

---

## 3. Lacunas e diferenciais possíveis do minicurso do DCP

1. **"Code as policy" como conceito, e não como recurso do produto.** Nenhum curso encontrado organiza a aula em torno da pergunta "quando uma instrução em prosa basta e quando ela precisa virar uma regra executável" (hook, pre-commit, CI). O DCP pode transformar isso na tese central da Sessão 1, que já tem o bloco "prosa vs. regras determinísticas", e demonstrá-la na Sessão 2. Exemplos possíveis: um hook que bloqueia `git push --force` ou a edição de `data/raw/`, e um pre-commit que exige trailer de autoria. Os pontos de apoio são o Claude Code in Action ([Anthropic](https://anthropic.skilljar.com/claude-code-in-action)) e os hooks de Sant'Anna ([repo](https://github.com/pedrohcgs/claude-code-my-workflow)).
2. **Agnosticismo de harness.** Quase todos os cursos são de um fornecedor só (Anthropic, OpenAI, Google, Microsoft). O DCP pode mostrar a mesma tarefa em dois harnesses (Claude Code e Codex) e usar o AGENTS.md como "contrato portável", como faz Kenny em Princeton.
3. **Validação de medidas com LLM.** Os cursos de agentes ignoram o tema e os cursos de "LLMs para ciências sociais" ignoram agentes. Uma demo em que o agente codifica um corpus, calcula a concordância com codificação humana e registra a versão do modelo uniria os dois mundos (EUI, HKS, Essex).
4. **Público lusófono e dados brasileiros.** Não encontrei curso acadêmico em português sobre agentes de código para pesquisa (seção B15). O precedente turco/inglês de Impram mostra o valor de adaptar, e não só traduzir. Dados possíveis: TSE, Câmara/Senado, ESEB, DOU.
5. **Custos em reais e acesso.** Só Blattman e Gießen discutem custo, e sempre em dólar e no contexto de assinatura dos EUA. Comparar planos, API e modelos abertos ou locais com o orçamento de bolsista CAPES/CNPq é um diferencial concreto.
6. **Segurança aplicada a pesquisa** (prompt injection via PDF ou página web, segredos em `.env`, dados sensíveis de survey). Os cursos de pesquisa quase não tratam injection.

---

## 4. Recomendações para a ementa

### Incluir ou reforçar
- **Sessão 1, abertura:** "Quando a tarefa precisa de um agente?" (Kaggle Dia 1), contrapondo a regra de Pepinsky de "seguir regras, sim; interpretar, não" ([post](https://tompepinsky.com/2026/01/23/agentic-ai-and-social-science-research-practice/)). Isso dá o enquadramento ético e metodológico em 10 minutos.
- **Sessão 1, como o LLM funciona:** encenar o loop do agente com papel e dados (AusPSA, [ANU](https://rsss.cass.anu.edu.au/news/3rd-apsa-workshop-quantitative-methods-integrating-ai-quantitative-political-research)). Uma variante: um aluno é o "modelo", outro o "harness", que só executa ferramentas escritas em cartões. Assim se mostra que o modelo não age, só pede.
- **Sessão 1, modelos e custos:** acrescentar "o modelo muda durante o projeto" (EUI) e registrar modelo, versão e data como prática de reprodutibilidade.
- **Sessão 1, harness e sandbox:** usar a formulação de Gießen ("o agente age com o seu acesso total à máquina") como motivação, antes de containerização e permissões.
- **Sessão 2, git como proveniência:** se ainda não estiver explícito, incluir. Aparece em todos os cursos de pesquisa (Gießen, OSU, HKS, Sant'Anna).
- **Sessão 2, verificação:** fazer uma demo curta de verificador com contexto limpo ou revisão adversarial (Sant'Anna, `/council` de Blattman) e uma de verificação de DOI ou citação (Impram).
- **Usar o framework 4D (Anthropic AI Fluency)** como vocabulário comum para não programadores: delegar, descrever, discernir e agir com diligência ([curso](https://anthropic.skilljar.com/ai-fluency-framework-foundations)).

### Cortar ou reduzir
- **Construção de agentes com frameworks** (LangGraph, smolagents, ADK, Agent Framework). Domina os cursos da indústria, mas não serve a pós-graduandos sem programação em 3 h. No máximo, um slide indicando HF, Microsoft e Korinek como trilha posterior.
- **Construir um servidor MCP.** Basta *usar* um MCP pronto (Zotero, filesystem, navegador) e explicar a arquitetura em um diagrama.
- **Deploy e produção, A2A, computer use:** fora do escopo.

### Ideias pedagógicas
1. **Projeto de exemplo já configurado** (Gießen): um repositório-modelo com dados da CP brasileira, CLAUDE.md/AGENTS.md, uma skill e um hook prontos. A instalação não consome o tempo de aula e o aluno faz fork depois.
2. **Bloco curto com input, demo e exercício guiado** (Gießen). Com 1h30, a sugestão é fazer 3 ciclos de cerca de 25 minutos na Sessão 2.
3. **A mesma tarefa com e sem governança:** pedir ao agente algo proibido em prosa (CLAUDE.md diz "não edite `data/raw`") e mostrar quando ele obedece e quando escapa; depois ativar o hook e mostrar o bloqueio. É a demo mais direta de "code as policy".
4. **Demo de prompt injection inofensiva:** um PDF ou página com uma instrução escondida que o agente lê, seguida da discussão sobre permissões e sandbox.
5. **Mini-validação de medida:** o agente classifica 50 discursos; a turma compara com um gabarito humano e calcula a concordância.
6. **"Build kit" de saída** (OpenAI Summer Studio): cada aluno leva um template de AGENTS.md e uma skill adaptados à própria pesquisa.
7. **Introdutório versus avançado** (Harvard Bok): deixar explícito que a Sessão 2 é para quem já instalou o harness, com tutorial de instalação enviado antes (Gießen, Blattman).
8. **Leituras e trilhas pós-curso:** claudeblattman.com (não programadores), `claude-code-my-workflow` (avançado), Korinek NBER WP 34202 (construir agentes), Anthropic Academy (gratuito, com certificado).
