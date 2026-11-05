# Plano Geral do Minicurso — Workshop Agentes (DCP-USP 2026)

Documento de organização pedagógica das duas sessões. Serve como ponto de partida para a divisão de trabalho entre os ministrantes e para a preparação dos slides. Os roteiros detalhados de fala estão em:

- [Sessão 1 — Introdução aos Agentes](../../sessions/01-introduction-ecosystem/notas-aula.md)
- [Sessão 2 — Habilidades Práticas e Governança](../../sessions/02-practical-skills/notas-aula.md)
- [Bibliografia comentada](../../referencias.md) ([BibTeX](../../referencias.bib))

Tudo aqui segue a ementa submetida ([llm-agents-for-research-syllabus.qmd](../../llm-agents-for-research-syllabus.qmd)); nenhum tópico novo foi acrescentado ao programa, apenas detalhado.

---

## 1. Fio condutor

As duas sessões respondem a uma única pergunta: **como usar agentes de IA na pesquisa social sem abrir mão de rigor, registro e replicabilidade?**

- **Sessão 1 (conceitual)**: o que é um agente, o que existe hoje, quanto custa, onde ele roda (*harness*) e qual é a diferença entre pedir algo em prosa e impor uma regra determinística.
- **Sessão 2 (demonstrações)**: os mecanismos concretos que transformam essa distinção em prática — *skills*, *hooks*, MCP, `AGENTS.md` — e exemplos de boas aplicações.

A tese que amarra as duas sessões, e que deve aparecer na abertura e no encerramento de cada uma:

> O gargalo da pesquisa com agentes deixou de ser a *execução* e passou a ser a *verificação*. Quem pesquisa continua sendo responsável pelo resultado; o agente só muda o que precisa ser verificado e como.

Essa formulação dialoga diretamente com o argumento de Scott Cunningham sobre "retornos à expertise" (o agente amplifica quem já sabe avaliar o resultado) e com a literatura metodológica recente sobre validação de medidas produzidas por LLMs (Ludwig, Mullainathan e Rambachan; Egami et al.; Barrie, Palmer e Spirling; Baumann et al.).

## 2. Três casos-âncora (usados nas duas sessões)

Para que os exemplos não fiquem abstratos, sugerimos repetir os mesmos três casos ao longo das duas sessões, todos próximos do cotidiano de um pós-graduando do DCP:

| Caso | Tarefa | Onde aparece |
|---|---|---|
| **A. Discursos parlamentares** | Classificar discursos da Câmara dos Deputados segundo um livro de códigos (ex.: posição sobre política educacional) | S1 bloco 1 (chat vs. agente); S2 skills, hooks e auditoria — é o [projeto de demonstração](../../sessions/02-practical-skills/lab/demo-project/) |
| **B. Entrevistas qualitativas** | Transcrever e pré-codificar tematicamente entrevistas semiestruturadas | S1 bloco 3 (custos); S2 bloco 5 (aplicações: transcrição local, sigilo) |
| **C. Dados públicos** | Baixar e limpar dados do TSE/INEP/IPEA e montar uma base analítica | S1 bloco 4 (*harness*); S2 bloco 3 (MCP, APIs governamentais) |

## 3. Cronograma resumido

### Sessão 1 — Introdução aos Agentes (90 min, sem prática)

| # | Bloco (item da ementa) | Min | Responsável (a definir) |
|---|---|---|---|
| 0 | Abertura: apresentação, objetivos, enquete rápida | 5 | |
| 1 | LLMs como Agentes | 20 | |
| 2 | Panorama de Modelos e Ferramentas | 15 | |
| 3 | Benefícios, Vantagens e Custos | 15 | |
| 4 | O *Harness*: Isolamento e Containerização | 15 | |
| 5 | Instrução em Prosa vs. Restrições Determinísticas | 15 | |
| 6 | Encerramento e ponte para a Sessão 2 | 5 | |

### Sessão 2 — Habilidades Práticas e Governança (90 min, demonstrações ao vivo)

| # | Bloco (item da ementa) | Min | Responsável (a definir) |
|---|---|---|---|
| 0 | Abertura: retomada da Sessão 1, apresentação do projeto de demonstração | 5 | |
| 1 | *Skills* e orquestração (implementador vs. auditor) | 15 | |
| 2 | *Hooks* e *code as policy* (demonstração ao vivo) | 20 | |
| 3 | MCP, linha de comando e segurança | 15 | |
| 4 | `AGENTS.md` e reprodutibilidade | 15 | |
| 5 | Aplicações exemplares | 15 | |
| 6 | Encerramento: checklist para levar para casa, perguntas | 5 | |

**Sugestão de divisão (a validar entre os três):** um ministrante conduz a fala enquanto outro opera o terminal nas demonstrações — isso reduz o risco de a demonstração travar a exposição. Uma divisão possível é cada ministrante assumir dois blocos por sessão e revezar a função de "operador de terminal".

## 4. Materiais a produzir

| Material | Status | Observação |
|---|---|---|
| Ementa (PDF/DOCX) | Pronto | Submetida em 2026-08-31 |
| Roteiro da Sessão 1 | Pronto (este commit) | Revisar exemplos e distribuir blocos |
| Roteiro da Sessão 2 | Pronto (este commit) | Idem |
| Projeto de demonstração (`lab/demo-project/`) | Pronto (este commit) | Ensaiar pelo menos uma vez com o agente que será usado ao vivo |
| Bibliografia comentada | Pronto (este commit) | Decidir se uma lista curta entra na ementa |
| Slides (Quarto Reveal.js) | A fazer | Sugestão: `sessions/0N-*/llm-agents-for-research-session-N-slides.qmd`, renderizados para `docs/` |
| Gravação de *backup* das demonstrações | A fazer | Vídeo curto de cada demo, caso a rede ou a API falhe |
| Folha-resumo de uma página para os participantes | A fazer | Checklist do bloco de encerramento da Sessão 2 |

## 5. Checklist da semana da aula

- [ ] Conferir versões e preços atuais dos modelos citados no bloco 2 e no bloco 3 da Sessão 1 (mudam mês a mês; não confiar nos números do roteiro sem verificar).
- [ ] Rodar o projeto de demonstração do zero numa máquina limpa, com o mesmo agente e o mesmo plano/conta que serão usados ao vivo.
- [ ] Garantir que o R e o pacote `jsonlite` estejam instalados na máquina de demonstração (os *hooks* são scripts R).
- [ ] Separar uma chave de API com limite de gastos baixo para a demonstração (nunca a chave pessoal principal).
- [ ] Gravar o vídeo de *backup* das demonstrações.
- [ ] Confirmar sala, projetor, rede e se os participantes terão acesso à internet (a Sessão 2 não exige que eles instalem nada).
- [ ] Decidir o link de materiais que será divulgado (este repositório, se ficar público).

## 6. Decisões em aberto

1. **Qual agente usar ao vivo.** O roteiro foi escrito para funcionar com qualquer agente de terminal que suporte *hooks*, *skills* e `AGENTS.md`. Os exemplos de configuração usam o formato do Claude Code (`.claude/settings.json`), que é o mais documentado; convém mostrar ao menos uma vez uma alternativa aberta (OpenCode, goose) para não parecer propaganda de fornecedor — coerente com a decisão já tomada na ementa de evitar centralizá-la em produtos (commit `ff3e9d7`).
2. **Lista de leituras na ementa.** A ementa atual não tem seção de referências. Se quisermos incluir, sugerimos 5 a 7 itens da seção "Leituras essenciais" de `referencias.md`, e recompilar via Quarto.
3. **Enquete de abertura.** Usar formulário (Mentimeter, Google Forms) ou mão levantada. Os dados da pesquisa da Anthropic com 1.260 cientistas sociais (81% usaram chatbots; 20% usam agentes; 25% entre cientistas políticos) servem de comparação com a turma.
4. **Público com e sem programação.** A ementa promete que não é preciso programar. As demonstrações da Sessão 2 mostram código, mas o roteiro sempre explica *o que a regra faz* antes de mostrar *como está escrita*.
