# LLM Agents for Research — Agentes de IA para Pesquisa

Minicurso *Workshop Agentes: Inteligência Artificial e Autonomia na Pesquisa Social* (Seminário Discente DCP-USP 2026).

**Site:** <https://mancano-tales.github.io/course-llm-agents-for-research/> (slides, ementa e materiais).

Materiais, ementa, slides e laboratório do minicurso. Material de terceiros recebido em confiança não fica aqui.

## Ministrantes
* **Manoel Galdino** ([@mgaldino](https://github.com/mgaldino)) — Professor no Departamento de Ciência Política da USP
* **Felipe Lamarca** ([@felipelmc](https://github.com/felipelmc)) — Mestrando em Ciência Política no IESP-UERJ
* **Tales Mançano** ([@mancano-tales](https://github.com/mancano-tales)) — Mestrando em Ciência Política no DCP-USP

---

## Estrutura do Minicurso (2 Sessões de 1h30)

| Sessão | Tema Principal | Tópicos Centrais |
|---|---|---|
| **Sessão 1** | Do Chatbot ao Agente | LLMs como agentes (terminal, arquivos), panorama de modelos, prosa vs. instruções determinísticas, containerização — sem prática |
| **Sessão 2** | Habilidades Práticas | Hooks de agente (*code as policy*, analogia com git hooks — sem exigir git prévio), skills e orquestração/gerenciamento de contexto, MCP, `AGENTS.md`, boas aplicações exemplares de IA para pesquisa |

---

## Documentos e Materiais

* **Ementa Completa**: Consulte a versão em código em [llm-agents-for-research-syllabus.qmd](llm-agents-for-research-syllabus.qmd), a versão compilada (HTML, PDF e DOCX) no site.
* **Plano Geral das Aulas**: [docs/plan/plano-geral.md](docs/plan/plano-geral.md) — fio condutor, casos-âncora, cronograma, divisão de papéis e checklist de preparação.
* **Plano de Preparação (out. 2026)**: [docs/plan/2026-10-06_plano-preparacao-aulas.md](docs/plan/2026-10-06_plano-preparacao-aulas.md) — síntese da pesquisa exploratória, decisões propostas e pauta da reunião dos ministrantes.
* **Pesquisa Exploratória**: [docs/research/](docs/research/) — panorama de cursos sobre agentes, *code as policy*, modelos e *harnesses*, e o que Scott Cunningham tem publicado.
* **Slides**: um deck por sessão, em [sessions/01-introduction-ecosystem/llm-agents-for-research-session-1-slides.qmd](sessions/01-introduction-ecosystem/llm-agents-for-research-session-1-slides.qmd) e [sessions/02-practical-skills/llm-agents-for-research-session-2-slides.qmd](sessions/02-practical-skills/llm-agents-for-research-session-2-slides.qmd). Geram PDFs Beamer com o tema [madrid-web](https://github.com/mancano-tales/presentations/tree/main/_extensions/madrid-web) (`_extensions/`).
* **Roteiros do Instrutor**:
  * [Sessão 1: Introdução aos Agentes](sessions/01-introduction-ecosystem/notas-aula.md)
  * [Sessão 2: Habilidades Práticas e Governança](sessions/02-practical-skills/notas-aula.md)
* **Projeto de Demonstração (Sessão 2)**: [sessions/02-practical-skills/lab/demo-project/](sessions/02-practical-skills/lab/demo-project/) — *skill*, *hooks* em R, subagente auditor e `AGENTS.md` aplicados à codificação de discursos parlamentares fictícios.
* **Bibliografia Comentada**: [referencias.md](referencias.md) ([BibTeX](referencias.bib)).

---

## Como Compilar os Materiais Localmente

Este projeto utiliza [Quarto](https://quarto.org) para renderização de documentos e apresentações:

```bash
# Site e PDFs Beamer em _site/ (exige LaTeX; o GitHub Actions publica só as páginas e a ementa)
quarto render
quarto preview
```

```bash
# Ementa em PDF (Typst) e DOCX, dentro de _site/
quarto render llm-agents-for-research-syllabus.qmd --to typst
quarto render llm-agents-for-research-syllabus.qmd --to docx
```

```powershell
# PDFs Beamer das duas sessoes (PowerShell, Quarto e XeLaTeX); saida datada em _renders/
powershell -File tools/render-slides.ps1
```

O site é publicado automaticamente no GitHub Pages a cada push na `main` (`.github/workflows/publish.yml`). Os PDFs Beamer não são gerados no CI e ainda não estão no site: renderize localmente.

## Licença

Conteúdo sob CC BY 4.0; código sob MIT. Ver [LICENSE.md](LICENSE.md).
