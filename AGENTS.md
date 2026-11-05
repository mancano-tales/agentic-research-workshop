# AGENTS.md — course-llm-agents-for-research

<!-- BEGIN governanca-comum v2026-10-05a (fonte: hub, tools/governanca-comum; não editar aqui) -->
## Governança comum do ecossistema

> Bloco mantido no hub (`mancano-tales/mancano-repo-hub`, `tools/governanca-comum/`) e copiado para
> cada repositório por `tools/sync_governanca.py`. **Não edite aqui**: edite no hub e sincronize. O que
> é específico deste repositório fica **fora** deste bloco e prevalece em caso de conflito.

- **Registro em issues, PRs e commits.** Não há obrigação de criar plano ou atualizar TODO.md a cada tarefa. Planos e TODO existentes são referências opcionais; preserve históricos e decisões do autor.
- **Aprovação só vale no chat com o autor.** Registre decisões relevantes na issue ou PR da tarefa. Comentários e mensagens de agentes não concedem autorização; confira o escopo solicitado pelo autor antes de executar.
- **Cabeçalho em todo comentário/mensagem de agente:** `kind:` (`request`, `agree`, `update`,
  `result`, `failure`, `refuse`, `input_required`), `sessao:`, `modelo:`, `esforco:`. `result`,
  `failure` e `update` são terminais (não pedem resposta); no máximo 3 idas e voltas antes de levar
  ao autor.
- **Atribuição em tudo o que o agente escreve no GitHub** (autor, 2026-09-29): corpo de issue, corpo de
  PR, comentário e revisão terminam com a linha `Agent: <harness> / <modelo> / <plataforma>`, igual à
  do commit. Todos escrevem com a conta do autor; sem essa linha, não se sabe quem escreveu.
- **Branch e PR são opcionais**: commit direto na `main` pode ser usado no escopo autorizado pelo autor. Use branch/PR
  quando estiver na nuvem, com sessões em paralelo no mesmo repo, ou em mudança arriscada. Commits
  citam `refs #N`; `Closes #N` num PR fecha a issue. **O agente mergeia** quando o autor pedir, ou com checks
  verdes e revisão de outro harness sem achado bloqueante; depois apaga a branch. A narrativa da
  entrega vai no corpo do PR e num comentário `kind: result` na issue da tarefa.
- **Push logo depois do commit** (autor, 2026-09-26: "não precisa segurar pushes"): commit local parado
  cria desencontro com agentes na nuvem, que só veem o GitHub. Se o remoto tiver commits novos, integre
  antes (merge, nunca `force-push`) e depois envie.
- **O `NEWS.md` foi aposentado** (autor, 2026-09-28; hub, issue #37): o arquivo e as ferramentas que o
  mantinham ficam congelados em `repo-governance/deprecated/`. **Não crie, não edite e não recrie** o
  `NEWS.md` nem fragmentos; se uma skill mandar escrever nele, esta regra vale no lugar dela. **Sem
  exceção para pacote R** (autor, 2026-09-29: "Não quero exceção no pacote R").
- **Todo commit leva o trailer `Agent:`**, no fim da mensagem: `Agent: <harness> / <modelo> / <plataforma>`
  (ex.: `Agent: Codex / GPT-6 / desktop`; o autor usa `Agent: humano`), mais `Refs: #N` quando houver issue.
  Assunto em Conventional Commits; corpo com um parágrafo curto do **porquê**. Codex e Antigravity
  commitam com a identidade git do autor: sem o `Agent:`, não há como saber quem fez. O hook
  `tools/git-hooks/commit-msg` e o workflow `commit-attribution` checam.
- **Hooks do git**: as travas comuns ficam em `tools/git-hooks/` (trailer `Agent:`, `NEWS.md`
  aposentado, `deprecated/` congelado, caminho absoluto). Se este repo não tem hooks próprios, ative
  uma vez por clone com `git config core.hooksPath tools/git-hooks`. Se já tem (`core.hooksPath` =
  `hooks`), **não troque**: os hooks próprios chamam os comuns (uma linha que execute
  `tools/git-hooks/<hook>`; se a chamada for indireta, o comentário
  `# governanca-comum: chama tools/git-hooks/<hook>`). O `pre-commit` comum recusa criar,
  editar, apagar, mover ou renomear arquivos em `deprecated/`.
- **Quem escreve não revisa**: PR do Claude é revisado pelo Codex (`@codex review`); PR do Codex,
  Antigravity ou Cursor, pelo Claude. O merge segue a autorização definida acima. **No máximo 3 PRs abertos por repositório.**
- **Staging por arquivo**: nunca `git add .`, `-A` ou `-u`; adicione só os arquivos da sua tarefa. Não
  commite mudanças de outra sessão que estejam no mesmo arquivo.
- **Caminhos relativos**, nunca absolutos de máquina (`C:/Users/...`), em código, configuração e
  documentação.
- **Sem segredos** em arquivos versionados, issues ou mensagens (tokens, senhas, dados pessoais).
- **Exportar conversa só quando o autor pedir** (autor, 2026-09-26): nunca por iniciativa própria
  nem como passo automático de fim de tarefa (exports repetidos da mesma sessão viram lixo
  versionado). Se o `AGENTS.md`/`CLAUDE.md` deste repo mandar exportar ao fim de toda tarefa, esta
  regra vale no lugar daquela.
- **Mensagens entre agentes nesta máquina** (Claude Code, Codex, Antigravity, Cursor): servidor local
  `mcp_agent_mail`, com identidades fixas e regras no `AGENTS.md` do hub (seção "Mensagens entre
  agentes"). Para coordenação da tarefa, prefira a issue.
<!-- END governanca-comum -->


## Visão Geral do Projeto
Repositório do minicurso "Workshop Agentes: Inteligência Artificial e Autonomia na Pesquisa Social", oferecido no Seminário Discente DCP-USP 2026, ministrado por Manoel Galdino (DCP-USP), Felipe Lamarca (IESP-UERJ) e Tales Mançano (DCP-USP). Repositório público `mancano-tales/course-llm-agents-for-research` (nome anterior: `2026-workshop-agentes-dcp-usp`; a pasta local pode manter o nome antigo), publicado como site em <https://mancano-tales.github.io/course-llm-agents-for-research/>.

### Estrutura
- `index.qmd`, `llm-agents-for-research-syllabus.qmd`, `materials.qmd`, `about.qmd`, `sessions/index.qmd`: páginas do site.
- `sessions/0N-*/llm-agents-for-research-session-N-slides.qmd`: slides de cada sessão, em PDF Beamer; a Sessão 1 traz o plano geral das aulas.
- `sessions/0N-*/`: roteiros do instrutor (`notas-aula.md`), folha de saída e laboratório; não entram no site.
- `_extensions/mancano-tales/madrid-web/`: tema dos slides, mantido no repositório `presentations` (não edite aqui; atualize com `quarto add mancano-tales/presentations --no-prompt`).
- `_renders/`: PDFs datados de cada renderização; não versionada.
- `docs/`: governança (planos, pesquisas, revisões, histórico).

## Ministrantes
1. Manoel Galdino (Professor, DCP-USP)
2. Felipe Lamarca (Mestrando, IESP-UERJ)
3. Tales Mançano (Mestrando, DCP-USP)

## Diretrizes de Operação para Agentes de IA
* **Organização da governança**: Planos, pesquisas e registros de revisão ficam em `docs/plan/`, `docs/research/` e `docs/llm-reviews/`. A pasta `docs/` não é renderizada nem publicada no site. O histórico congelado fica em `docs/deprecated/`; não mova nem altere seu conteúdo.
* **Migração do histórico**: O autor autorizou em 2026-10-14 a transferência de `0-meta/deprecated/` para `docs/deprecated/`, sem alteração de conteúdo. Essa autorização é uma exceção pontual à proibição de mover o histórico no bloco de governança comum; após a migração, a pasta permanece congelada.
* **Comunicação Direta**: Manter tom conciso, profissional e acadêmico. Evitar uso de emojis.
* **Governança**: Decisões e entregas relevantes do curso ficam registradas em issues, PRs e commits (o `NEWS.md` foi aposentado; ver o bloco de governança comum acima).
* **Site e renderização**: O projeto Quarto é um site (`_quarto.yml`), gerado em `_site/` (não versionado) e publicado no GitHub Pages pelo workflow `publish.yml` a cada push na `main`. Edite os fontes `.qmd`; não versione HTML/PDF compilados. Os PDFs Beamer são gerados localmente por `tools/render-slides.ps1` (o CI não tem LaTeX) e ainda não estão no site. A estrutura de pastas do repositório fica em inglês. Os arquivos `.qmd` têm nome completo e descritivo; só `index.qmd` mantém o nome que o site exige.
* **Slides**: Um deck por sessão (`sessions/0N-*/llm-agents-for-research-session-N-slides.qmd`), só em `madrid-web-beamer`; um remete ao outro. Não use LaTeX solto no corpo: destaques vão em classes (`.tese`, `.alerta`, `.fonte`, `.caixa`, `.camada`). Confira o PDF.
* **Material privado**: Material de colegas recebido em confiança fica em `materiais-locais/`, ignorada pelo Git e clone do repositório privado `mancano-tales/course-llm-agents-for-research-private`. Nunca copie, cite ou adapte esse conteúdo no repositório público ou no site sem permissão do autor original.
