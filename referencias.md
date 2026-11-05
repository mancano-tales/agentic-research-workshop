# Bibliografia Comentada — Workshop Agentes (DCP-USP 2026)

Referências de apoio às duas sessões, atualizadas em setembro de 2026. Organizadas por função no curso, não por ordem alfabética. Entradas BibTeX correspondentes em [referencias.bib](referencias.bib).

Convenção: **[S1]** e **[S2]** indicam em que sessão a referência é usada; **[E]** marca as leituras essenciais, candidatas a entrar numa lista curta na ementa.

Observação: boa parte do material mais útil sobre agentes de pesquisa circula em *working papers*, blogs e repositórios, não em periódicos. Isso reflete a velocidade da área, e deve ser dito à turma: são fontes para orientar a prática, a serem lidas com o mesmo senso crítico de qualquer literatura cinzenta.

---

## 1. Leituras essenciais

1. **Korinek, Anton (2025).** *AI Agents for Economic Research*. NBER Working Paper 34202. **[S1][S2][E]**
   Atualização (ago. 2025) do artigo de Korinek no *Journal of Economic Literature* (2023). Explica o que são agentes, como planejam e usam ferramentas, e traz exemplos passo a passo — revisão de literatura, código econométrico, coleta de dados — pensados para quem não programa. Melhor introdução acadêmica única ao tema.
   <https://www.nber.org/papers/w34202>

2. **Cunningham, Scott (2025–2026).** Série "Claude Code" no *Scott's Mixtape Substack* (mais de 50 textos). **[S1][S2][E]**
   Cunningham é professor de economia na Baylor University (professor visitante no Departamento de Governo de Harvard em 2025–26 e na Harvard Kennedy School em 2026–27), autor de *Causal Inference: The Mixtape* (Yale University Press, 2021) e de *Causal Inference: The Remix* (Yale University Press, 2026). A série documenta, em tempo real, a adoção de agentes de terminal na pesquisa empírica aplicada: organização de projetos, replicação, depuração e — o ponto mais citável — os "retornos à expertise": o agente amplifica quem já sabe avaliar o resultado e pode corroer a formação de quem não sabe. Em março de 2026 falou sobre o tema ao *Board of Governors* do Federal Reserve (ele confirma a palestra; o título "AI Agents for Research Workers" e a demonstração ao vivo vêm de reportagem da Forbes, não conferida na fonte). Não encontramos livro com esse título. Levantamento detalhado, com datas e links: [docs/research/2026-10-06_scott-cunningham.md](https://github.com/mancano-tales/course-llm-agents-for-research/blob/main/docs/research/2026-10-06_scott-cunningham.md).
   <https://causalinf.substack.com/s/claude-code>

3. **Cunningham, Scott.** *MixtapeTools* (repositório GitHub), em especial o protocolo **Referee 2**. **[S2][E]**
   Auditoria em cinco etapas (correção do código, replicação em outra linguagem, estrutura de pastas, automação das saídas, econometria), executada por uma instância nova do agente que nunca viu o trabalho. Base conceitual do subagente auditor do projeto de demonstração. O repositório traz também, desde agosto de 2026, o primeiro *hook* dele (`hooks/protect-raw-data`): um *hook* que bloqueia edição em `data/raw`, uma trava do sistema operacional e uma impressão digital SHA-256 dos arquivos, porque um *hook* sozinho é contornável por um script ("The fix is not a bigger hook. It is a stack."). É a mesma lógica de guarda e sensor do projeto de demonstração.
   <https://github.com/scunning1975/MixtapeTools>

4. **Lyttelton, Thomas; Massenkoff, Maxim; Wilmers, Nathan (2026).** *Coding Agents in the Social Sciences*. Anthropic Research, 27 maio 2026. **[S1][E]**
   Pesquisa com 1.260 cientistas sociais quantitativos (fev.–mar. 2026): 81% usaram chatbots, 20% usam agentes (39% entre economistas, 25% entre cientistas políticos). Usuários de agentes postam 50% mais *working papers*, sem diferença em submissões a periódicos. Adoção desigual por gênero e prestígio institucional. Útil tanto como dado de abertura quanto como objeto de discussão sobre desigualdade.
   <https://www.anthropic.com/research/coding-agents-social-sciences>

5. **Barrie, Christopher; Palmer, Alexis; Spirling, Arthur (2025).** "Replication for Language Models: Problems, Principles, and Best Practice for Political Science". *American Journal of Political Science* (aceito). **[S1][S2][E]**
   Desenho de replicação iterada ao longo de meses: LLMs podem ser muito precisos, mas a variância entre execuções é frequentemente inaceitável, e controlar a temperatura não resolve. Referência central da ciência política sobre replicabilidade com LLMs.
   <https://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf>

6. **Ludwig, Jens; Mullainathan, Sendhil; Rambachan, Ashesh (2026).** "Large Language Models: An Applied Econometric Framework". *Annual Review of Economics* 18. **[S1][S2][E]**
   Quando um LLM é usado para *medir* um conceito que entra numa análise, a inferência válida exige combinar a saída do modelo com uma pequena amostra de validação; quando é usado para *prever*, exige garantir que não houve vazamento de treino. Fundamento do passo "amostra de validação humana" da *skill* de demonstração.
   <https://www.nber.org/papers/w33344>

7. **Anthropic — Schluntz, Erik; Zhang, Barry (2024).** *Building Effective Agents*. **[S1][E]**
   Texto curto e muito citado que distingue *fluxos de trabalho* (caminho definido pelo programador) de *agentes* (o modelo decide o caminho) e recomenda começar pelo mais simples.
   <https://www.anthropic.com/engineering/building-effective-agents>

---

## 2. Agentes: conceitos, arquitetura e engenharia de contexto

- **Willison, Simon (2025).** "I think 'agent' may finally have a widely enough agreed upon definition to be useful jargon now" — definição operacional *"um LLM que roda ferramentas em loop para atingir um objetivo"*. Blog pessoal (simonwillison.net), set. 2025. **[S1]**
- **Anthropic (2025).** *Effective Context Engineering for AI Agents*. Por que a janela de contexto é um recurso finito, e como subagentes, arquivos de memória e carregamento sob demanda ajudam a administrá-la. **[S1][S2]**
  <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
- **Anthropic (2025).** *Claude Code: Best Practices for Agentic Coding*; documentação oficial de *hooks*, *skills*, subagentes e `CLAUDE.md`. Referência técnica para o formato usado no projeto de demonstração. **[S2]**
  <https://code.claude.com/docs>
- **Liu, Jiacheng; Zhao, Xiaohan; Shang, Xinyi; Shen, Zhiqiang (2026).** "Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems". arXiv:2604.14228. Análise acadêmica da arquitetura de agentes de terminal: permissões, *hooks*, subagentes, memória. Útil para quem quiser aprofundar o bloco sobre *harness*. **[S1]**
  <https://arxiv.org/abs/2604.14228>

## 3. Padrões abertos

- **Model Context Protocol (MCP)** — especificação e documentação. Doado pela Anthropic à Agentic AI Foundation (Linux Foundation) em 9 dez. 2025. **[S1][S2]**
  <https://modelcontextprotocol.io>
- **AGENTS.md** — formato aberto de instruções de projeto para agentes, contribuído pela OpenAI à mesma fundação; adotado por mais de 60 mil projetos. **[S2]**
  <https://agents.md>
- **Agent Skills** — padrão aberto de *skills*, publicado pela Anthropic em 18 dez. 2025. **[S2]**
  <https://agentskills.io>
- **Linux Foundation (2025).** Anúncio da formação da Agentic AI Foundation (AAIF). **[S1]**
  <https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation>

## 4. Fluxos de trabalho de pesquisadores (pontos de partida práticos)

- **Sant'Anna, Pedro H. C. (2026).** *claude-code-my-workflow* — *template* para acadêmicos (LaTeX/Beamer, Quarto, R) com agentes revisores, portões de qualidade e protocolos de replicação; extraído do curso de doutorado *Causal Panel Data* (Emory). Adaptado por grupos de economia e ciência política. **[S2]**
  <https://github.com/pedrohcgs/claude-code-my-workflow>
- **Blattman, Christopher (2026).** *Claude Blattman — AI for Professionals Who Don't Code*. Site aberto de um economista político (Chicago Harris) sem formação em programação, com *skills*, fluxos de "críticos paralelos" e tutoriais para iniciantes. Excelente para o público-alvo do minicurso. **[S2]**
  <https://claudeblattman.com>
- **Crawfurd, Lee.** *claude-skills* — *skills* para revisão de artigos, revisão de código e auditoria de reprodutibilidade computacional. **[S2]**
  <https://github.com/lcrawfurd/claude-skills>
- **Korinek, Anton (2023).** "Generative AI for Economic Research: Use Cases and Implications for Economists". *Journal of Economic Literature* 61(4): 1281–1317. Versão anterior, centrada em chatbots; boa para contrastar com a de 2025. **[S1]**

## 5. LLMs como instrumento de medida nas ciências sociais

- **Egami, Naoki; Hinck, Musashi; Stewart, Brandon M.; Wei, Hanying (2023).** "Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models". *NeurIPS*. Como usar rótulos de LLM numa regressão sem viés, com uma amostra de validação. Pacote R `dsl`. **[S1][S2]**
- **Baumann, Joachim et al. (2025).** "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation". arXiv:2509.08825. Escolhas de modelo, *prompt* e temperatura mudam conclusões substantivas — um novo grau de liberdade do pesquisador. **[S1]**
  <https://arxiv.org/abs/2509.08825>
- **Gilardi, Fabrizio; Alizadeh, Meysam; Kubli, Maël (2023).** "ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks". *PNAS* 120(30). O artigo que popularizou a anotação com LLMs na ciência política. **[S1]**
- **Törnberg, Petter (2024).** "Best Practices for Text Annotation with Large Language Models". *Sociologica* 18(2). Lista prática de cuidados: validação, documentação, modelos abertos. **[S2]**
- **Spirling, Arthur (2023).** "Why Open-Source Generative AI Models Are an Ethical Choice for Science". *Nature* 616: 413. **[S1][S2]**
- **Argyle, Lisa P. et al. (2023).** "Out of One, Many: Using Language Models to Simulate Human Samples". *Political Analysis* 31(3). Referência para a discussão (fora do escopo principal do curso) sobre "amostras de silício". **[S1]**
- **Bail, Christopher A. (2024).** "Can Generative AI Improve Social Science?". *PNAS* 121(21). Panorama equilibrado de usos e riscos. **[S1]**

## 6. Evidência sobre produtividade

- **Becker, Joel et al. / METR (2025).** "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity". Ensaio randomizado: desenvolvedores experientes 19% mais lentos com IA, embora se percebessem 20% mais rápidos. **[S1]**
  <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
- **METR (2026).** "We Are Changing Our Developer Productivity Experiment Design" (24 fev. 2026). O resultado anterior está desatualizado; ganhos parecem prováveis, mas a recusa de trabalhar sem IA comprometeu o desenho. Bom exemplo, para a turma, de problema de seleção num experimento. **[S1]**
  <https://metr.org/blog/2026-02-24-uplift-update/>
- **Lyttelton, Massenkoff e Wilmers (2026)** — ver item 4 das leituras essenciais.

## 7. Segurança

- **Willison, Simon (2025).** "The Lethal Trifecta for AI Agents: Private Data, Untrusted Content, and External Communication". Blog pessoal, 16 jun. 2025. Modelo mental mais útil para explicar *prompt injection* a não especialistas. **[S1][S2]**
  <https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/>

## 8. Ecossistema R (para o público do DCP)

- **`ellmer`** (Posit) — interface do R para LLMs, com suporte a ferramentas (*tool calling*). <https://ellmer.tidyverse.org>
- **`mall`** (Posit) — aplica LLMs a colunas de *data frames* (classificação, extração, sentimento). <https://mlverse.github.io/mall/>
- **`mcptools`** e **`btw`** (Posit) — expõem a sessão R e a documentação de pacotes a agentes via MCP.
- **`dsl`** — implementação em R do *design-based supervised learning* de Egami et al. (2023).

## 9. Leitura de fundo (divulgação)

- **Mollick, Ethan (2024).** *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin. E o boletim *One Useful Thing* (oneusefulthing.org), atualizado com frequência sobre modelos e agentes.

---

## Nota sobre verificação

As referências das seções 1, 3, 4, 6 e 7 foram conferidas online em setembro de 2026. As das demais seções são publicações consolidadas, citadas de memória bibliográfica: conferir volume, páginas e DOI antes de usá-las em citação formal (slides ou ementa). Dados que envelhecem rápido — versões de modelos, preços, número de adotantes de padrões — devem ser reconferidos na semana da aula (ver checklist em `docs/plan/plano-geral.md`).
