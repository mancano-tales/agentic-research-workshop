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

* **Ementa Completa**: Consulte a versão em código em [ementa.qmd](ementa.qmd), a versão compilada (HTML, PDF e DOCX) no site.
* **Plano Geral das Aulas**: [docs/plan/plano-geral.md](docs/plan/plano-geral.md) — fio condutor, casos-âncora, cronograma, divisão de papéis e checklist de preparação.
* **Plano de Preparação (out. 2026)**: [docs/plan/2026-10-06_plano-preparacao-aulas.md](docs/plan/2026-10-06_plano-preparacao-aulas.md) — síntese da pesquisa exploratória, decisões propostas e pauta da reunião dos ministrantes.
* **Pesquisa Exploratória**: [docs/pesquisa/](docs/pesquisa/) — panorama de cursos sobre agentes, *code as policy*, modelos e *harnesses*, e o que Scott Cunningham tem publicado.
* **Slides**: fonte única das duas sessões em [aulas/agentes-ia-pesquisa.qmd](aulas/agentes-ia-pesquisa.qmd). Gera os slides web do site e o [PDF Beamer](assets/agentes-ia-pesquisa.pdf), com o tema [madrid-web](https://github.com/mancano-tales/presentations/tree/main/_extensions/madrid-web) (`_extensions/`).
* **Roteiros do Instrutor**:
  * [Sessão 1: Introdução aos Agentes](aulas/01-introducao-ecossistema/notas-aula.md)
  * [Sessão 2: Habilidades Práticas e Governança](aulas/02-habilidades-praticas/notas-aula.md)
* **Projeto de Demonstração (Sessão 2)**: [aulas/02-habilidades-praticas/lab/projeto-demo/](aulas/02-habilidades-praticas/lab/projeto-demo/) — *skill*, *hooks* em R, subagente auditor e `AGENTS.md` aplicados à codificação de discursos parlamentares fictícios.
* **Bibliografia Comentada**: [referencias.md](referencias.md) ([BibTeX](referencias.bib)).

---

## Como Compilar os Materiais Localmente

Este projeto utiliza [Quarto](https://quarto.org) para renderização de documentos e apresentações:

```bash
# Site completo em _site/ (o mesmo que o GitHub Actions publica)
quarto render
quarto preview
```

```bash
# Ementa em PDF (Typst) e DOCX, dentro de _site/
quarto render ementa.qmd --to typst
quarto render ementa.qmd --to docx
```

```powershell
# PDF Beamer Madrid das duas sessoes (PowerShell 7, Quarto e XeLaTeX); copia para assets/
powershell -File tools/render-slides.ps1
```

O site é publicado automaticamente no GitHub Pages a cada push na `main` (`.github/workflows/publish.yml`). O PDF Beamer não é gerado no CI: renderize localmente e versione `assets/agentes-ia-pesquisa.pdf`.

## Licença

Conteúdo sob CC BY 4.0; código sob MIT. Ver [LICENSE.md](LICENSE.md).
