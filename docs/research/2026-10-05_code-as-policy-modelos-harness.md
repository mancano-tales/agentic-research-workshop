# Pesquisa de apoio: políticas determinísticas, modelos atuais e harnesses

Minicurso "Agentes de IA para Pesquisa", Seminário Discente DCP-USP 2026.
Levantamento feito em **2026-10-05**. Modelos, preços e planos mudam em semanas: confira de novo na véspera da aula.

**Legenda de confiabilidade**

- **[oficial]**: conferido na documentação ou página oficial do fornecedor, na data indicada.
- **[secundária]**: só achei em imprensa, blogs ou agregadores; provável, mas não conferido na fonte primária.
- **[não confirmado]**: as fontes divergem ou não achei confirmação; não use em slide sem checar.

Quando não há data de publicação, a data é a da consulta (2026-10-05).

---

## Bloco 1. Code as policy e políticas determinísticas para agentes

### 1.1 De onde vem o termo, e os dois sentidos dele

| Sentido | O que significa | Fonte |
|---|---|---|
| **"Code as Policies"** (robótica, 2022) | Um LLM treinado em código *escreve o programa que controla o robô*. A "policy" é a política de controle, no sentido da aprendizagem por reforço: a função que leva da observação à ação. O código gerado **é** a política. | Liang, Huang, Xia, Xu, Hausman, Ichter, Florence e Zeng, "Code as Policies: Language Model Programs for Embodied Control", arXiv 2209.07753, submetido em 16/09/2022, versão final de 25/05/2023 (ICRA 2023) [oficial]: https://arxiv.org/abs/2209.07753 |
| **"Policy as code"** (infraestrutura e governança) | As regras institucionais (quem pode fazer o quê, o que é proibido) são escritas como código versionado, testável e executado automaticamente, e não como manual em prosa. O exemplo clássico é o Open Policy Agent (linguagem Rego). | https://www.openpolicyagent.org/docs (consultado em 2026-10-05) |
| **Uso atual com agentes** | É o segundo sentido aplicado aos agentes: as regras que o agente deve seguir viram **mecanismos que o harness ou o repositório executam** (hooks, regras de permissão, sandbox, CI, rulesets do GitHub), e não pedidos no prompt ou no `AGENTS.md`. | Ver 1.2 a 1.5 |

**Sugestão didática:** deixar claro que o título "code as policy" junta os dois sentidos. No artigo de 2022 o modelo *gera* a política. Na prática de 2026 nós *escrevemos* a política em código para limitar o modelo. O que une os dois é a ideia de que a regra que vale é a que roda, não a que está escrita em prosa.

### 1.2 Por que "pedir em prosa" é probabilístico e "travar com regra" é determinístico

- Uma instrução no prompt, no `CLAUDE.md` ou no `AGENTS.md` muda a **probabilidade** de o modelo agir de certo jeito. Ela concorre com o resto do contexto, pode se perder quando o contexto é compactado e pode ser sobrescrita por texto injetado (prompt injection).
- Uma regra executada pelo harness (hook, regra de permissão, sandbox do sistema operacional) ou pelo servidor (ruleset do GitHub, check obrigatório) é avaliada **fora do modelo**. Ela produz sempre a mesma decisão para a mesma entrada, seja qual for o "humor" do modelo.
- A documentação do Claude Code diz isso com todas as letras: as regras de permissão "are enforced by Claude Code, not by the model". Instruções no prompt ou no `CLAUDE.md` moldam o que o Claude *tenta* fazer, mas não mudam o que o Claude Code *permite* [oficial, https://code.claude.com/docs/en/permissions, consultado em 2026-10-05].
- Birgitta Böckeler (martinfowler.com, **02/04/2026**) organiza o harness em **guides** (controles *feedforward*, que orientam antes da ação) e **sensors** (controles de *feedback*, que observam depois). Cada um pode ser **computacional** (determinístico e barato: testes, linters, type checkers) ou **inferencial** (revisão por IA: semanticamente mais rico, porém mais caro e não determinístico) [oficial do autor]: https://martinfowler.com/articles/harness-engineering.html
- A equipe do Codex na OpenAI relatou ter construído em cinco meses um produto de cerca de 1 milhão de linhas sem código escrito à mão, impondo a arquitetura por **linters e testes estruturais** ("mechanical enforcement") e usando o `AGENTS.md` como mapa. O post original ("Harness engineering") está em https://openai.com/index/harness-engineering/ (403 para o meu fetch). O resumo que usei é da InfoQ, de **21/02/2026** [secundária]: https://www.infoq.com/news/2026/02/openai-harness-engineering-codex

**Ressalva importante (honestidade com a turma):** "determinístico" não quer dizer "infalível". Exemplos:

- As regras `Read`/`Edit` deny do Claude Code **não** pegam um script Python ou R que abre o arquivo por conta própria. Para isso é preciso o sandbox do sistema operacional [oficial, permissions].
- O sandbox do Bash não cobre as ferramentas internas de arquivo, os servidores MCP nem os hooks [oficial, https://code.claude.com/docs/en/sandboxing].
- A lógica é a de **defesa em camadas**.

### 1.3 Hooks de agente: comparação entre harnesses

| Harness | Mecanismo | Eventos principais | Como bloqueia | Onde configura | Fonte (consulta 2026-10-05) |
|---|---|---|---|---|---|
| **Claude Code** | Hooks dos tipos `command`, `http`, `mcp_tool`, `prompt` e `agent` (este último experimental) | `SessionStart`, `SessionEnd`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `Stop`, `SubagentStart`/`SubagentStop`, `PreCompact`/`PostCompact`, `FileChanged`, `ConfigChange`, `InstructionsLoaded` e outros (mais de 25 eventos) | Exit code **2** ou JSON com `permissionDecision: "deny"` (no `PreToolUse`), ou `decision: "block"` (no `Stop`, que então obriga o agente a continuar) | `~/.claude/settings.json`, `.claude/settings.json` (versionado), `.claude/settings.local.json`, plugins, frontmatter de skill ou subagente, managed settings | [oficial] https://code.claude.com/docs/en/hooks |
| **Codex (CLI e app)** | Hooks de script ou de ferramenta MCP | `SessionStart`, `SessionEnd`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `Interrupt`, `PreCompact`/`PostCompact`, `SubagentStart`/`SubagentStop` | `permissionDecision: "deny"` ou exit code 2 no `PreToolUse`. Hooks de projeto só carregam se a pasta `.codex/` for confiável | `~/.codex/hooks.json` ou `config.toml`, `<repo>/.codex/hooks.json`, `requirements.toml` (gerenciado) | [oficial] https://learn.chatgpt.com/docs/hooks (redireciona de developers.openai.com/codex/hooks) |
| **Gemini CLI** | Hooks de comando com saída JSON estrita | `SessionStart`, `SessionEnd`, `BeforeAgent`, `AfterAgent`, `BeforeModel`, `AfterModel`, `BeforeToolSelection`, `BeforeTool`, `AfterTool`, `PreCompress`, `Notification` | Exit code 2, ou `{"decision":"deny"}` | `settings.json` (projeto, usuário ou sistema) | [oficial] https://geminicli.com/docs/hooks/ (data de lançamento não confirmada) |
| **Cursor** | `hooks.json` com hooks de comando e de prompt | `sessionStart`, `preToolUse`, `postToolUse`, `beforeShellExecution`, `afterShellExecution`, `beforeReadFile`, `afterFileEdit`, `beforeSubmitPrompt`, `stop`, `subagentStart`/`subagentStop` | Exit code 2 ou `"deny"`. Entre vários hooks, deny prevalece sobre ask, que prevalece sobre allow. Os agentes na nuvem rodam só os hooks de comando | `.cursor/hooks.json`, `~/.cursor/hooks.json`, nível enterprise | [oficial] https://cursor.com/docs/agent/hooks |
| **OpenCode** | Plugins em JS/TS que assinam eventos | `tool.execute.before`/`after`, `session.*`, `file.edited`, `permission.asked`/`replied` etc. | Lançar um erro dentro de `tool.execute.before` | Pasta de plugins | [oficial] https://opencode.ai/docs/plugins/ |
| **goose** | Não achei sistema de hooks equivalente. O controle é feito por **modos de permissão** (Autonomous, Manual Approval, Smart Approval, Chat Only) e por permissão por ferramenta | n/a | Aprovação manual ou por risco | `/mode` na sessão e configuração | [oficial] https://goose-docs.ai/docs/guides/goose-permissions. Ausência de hooks [não confirmado] |
| **Aider** | Não tem hooks de agente. Tem `--lint-cmd`, `--test-cmd` e `--auto-test`: roda linter e testes depois de cada edição e tenta corrigir se o exit code não for zero. Faz auto-commit no git | n/a | Não bloqueia: realimenta o modelo com o erro | Flags e `.aider.conf.yml` | [oficial] https://aider.chat/docs/usage/lint-test.html |
| **Antigravity (Google)** | **Terminal execution policy** (Off com allowlist, Auto, Turbo com denylist) e **review policy** (Always Proceed, Agent Decides, Request Review) | n/a | Allowlist e denylist de comandos | Configurações do IDE | [secundária] codelab do Google: https://codelabs.developers.google.com/getting-started-google-antigravity |

### 1.4 Permissões, modos e sandbox (camada do harness)

**Claude Code** [oficial, https://code.claude.com/docs/en/permissions e /sandboxing, 2026-10-05]

- **Regras** `allow`/`ask`/`deny` com sintaxe como `Bash(git push *)`, `Read(./.env)`, `Edit(./data/raw/**)`, `WebFetch(domain:github.com)`. A avaliação segue a ordem **deny, ask, allow**: um deny amplo vence um allow específico.
- **Modos:** `default` (Manual), `acceptEdits`, `plan`, `auto` (um classificador revisa as ações no lugar do usuário), `dontAsk` e `bypassPermissions`. O próprio texto da documentação recomenda usar `bypassPermissions` só em container ou VM.
- **Managed settings** permitem que a organização imponha regras sem que o usuário consiga sobrescrevê-las. Exemplo: `disableBypassPermissionsMode`.
- **Hooks e permissões interagem assim:** um hook `PreToolUse` com exit 2 bloqueia mesmo quando há regra allow. Um hook que devolve "allow" **não** fura uma regra deny.
- **Sandbox:** isola só os comandos de shell, com Seatbelt no macOS e bubblewrap no Linux e no WSL2, combinando restrição de escrita em disco e rede via proxy com allowlist de domínios. Vem desligado por padrão e se liga com `/sandbox`. **No Windows nativo os comandos rodam sem sandbox**: é preciso WSL2, container ou VM. O código aberto é `@anthropic-ai/sandbox-runtime`.
- **Post de engenharia da Anthropic** (20/10/2025): no uso interno, o sandbox "reduz com segurança os prompts de permissão em 84%". O post defende que é preciso isolar *ambos*, arquivos e rede: sem isolar a rede, o agente comprometido exfiltra chaves; sem isolar arquivos, ele escapa do sandbox [oficial]: https://www.anthropic.com/engineering/claude-code-sandboxing
- **Comparação de ambientes isolados** (sandbox do Bash, sandbox runtime, devcontainer, container próprio, VM, sessão na nuvem): https://code.claude.com/docs/en/sandbox-environments [oficial].
  - Para rodar sem supervisão com `--dangerously-skip-permissions`, a recomendação é container, VM ou sandbox runtime.
  - O repositório do Claude Code publica um devcontainer de exemplo com firewall iptables que nega tudo por padrão.
  - O Docker Sandboxes (microVM) é citado como alternativa.

**Codex** [oficial, https://learn.chatgpt.com/docs/agent-approvals-security, 2026-10-05]

- **Sandbox:** `read-only` (padrão em pasta fora de controle de versão), `workspace-write` (padrão em repositório git) e `danger-full-access`.
- **Aprovação:** `on-request`, `never` e políticas granulares.
- **Rede:** desligada por padrão. Com `network_proxy`, passa a ter allowlist de domínios.
- **Mecanismos do sistema operacional:** Seatbelt no macOS, bubblewrap com seccomp no Linux, sandbox nativo no Windows.
- **Codex Cloud:** containers da OpenAI. A fase de setup tem rede; a fase do agente roda offline por padrão, e os segredos são removidos antes dela.

**Gemini CLI** [oficial, https://geminicli.com/docs/cli/sandbox/]: Seatbelt no macOS (perfil padrão `permissive-open`), Docker ou Podman, gVisor ou LXC no Linux, e restrição por nível de integridade no Windows. Liga-se com `gemini -s`, `GEMINI_SANDBOX=docker` ou `"sandbox"` no `settings.json`.

**GitHub Copilot coding agent:** firewall que limita a internet por padrão para reduzir exfiltração. O firewall só vale para processos lançados pela ferramenta Bash, **não** para servidores MCP nem para os setup steps [oficial]: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-firewall

### 1.5 O GitHub como camada de política determinística

As camadas de política, da mais próxima do agente à mais distante:

```
agente (prompt / AGENTS.md)   <- probabilístico
  harness: permissões, hooks, sandbox   <- determinístico, local
    git hooks: pre-commit, commit-msg   <- determinístico, local (contornável com --no-verify)
      GitHub: Actions/CI, rulesets, checks obrigatórios, CODEOWNERS, push protection   <- determinístico, no servidor
        revisão humana ou por outro agente   <- inferencial, mas obrigatória por regra
```

| Mecanismo | O que trava | Determinístico? | Fonte (consulta 2026-10-05) |
|---|---|---|---|
| **Git hooks** (`pre-commit`, `commit-msg`, `pre-push`) | Rodam scripts locais antes do commit ou do push. Recusam commit sem trailer, com caminho absoluto, com arquivo em `data/raw/` etc. | Sim, mas são **locais**, cada clone precisa ativá-los (`core.hooksPath`) e `--no-verify` pula o hook. Por isso convém repetir a checagem no CI | https://git-scm.com/docs/githooks |
| **GitHub Actions / CI** | Roda o mesmo script no servidor a cada push ou PR: testes, render do Quarto, validação de codebook | Sim | https://docs.github.com/en/actions |
| **Rulesets e branch protection** | Exigem PR antes do merge, número mínimo de aprovações, **revisão de code owner**, **status checks obrigatórios**, histórico linear, commits assinados e bloqueio de force push. Também podem **restringir caminhos de arquivo**, extensões e tamanho | Sim, imposto pelo servidor | [oficial] https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets. A disponibilidade por plano (free, privado) não está nesta página [não confirmado] |
| **CODEOWNERS** | Define o dono de cada caminho (por exemplo `codebook/`). Junto com o ruleset, torna obrigatória a aprovação desse dono | Sim | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners |
| **Secret scanning com push protection** | Bloqueia o push que contém token ou chave *antes* de ele chegar ao repositório. Em repositório **público** é gratuito e vem ligado para usuários. Em **privado**, exige GitHub Secret Protection | Sim (quem tem escrita pode contornar, mas fica registrado) | [oficial] https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection |
| **Dependabot** | Alerta e abre PR de atualização de dependências vulneráveis | Sim (alerta; a mudança passa por PR) | https://docs.github.com/en/code-security/dependabot |
| **Revisão de PR por agente: Codex** | `@codex review` num comentário do PR. Aponta só problemas P0/P1 e segue a seção `## Review guidelines` do `AGENTS.md` mais próximo de cada arquivo alterado | **Inferencial**; o que é determinístico é *exigir* a revisão | [secundária, com docs oficiais indicadas] https://developers.openai.com/codex/integrations/github |
| **Revisão de PR por agente: Claude** | `anthropics/claude-code-action@v1`, instalado via `/install-github-app`. Responde a `@claude` ou roda automaticamente num workflow de review (plugin `code-review`). Existe também o produto "Code Review", que revisa automaticamente sem workflow | Inferencial | [oficial] https://code.claude.com/docs/en/github-actions |
| **Revisão de PR por agente: Copilot** | Revisão automática configurada como **regra de ruleset**. Desde **01/09/2026**, em preview público, o Copilot também pode **aprovar** PRs | Inferencial | [oficial] https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/configure-automatic-review. Aprovação: [secundária] https://startdebugging.net/2026/09/copilot-code-review-can-now-approve-pull-requests/ |

**Ponto conceitual para a aula:** a revisão por IA é um *sensor inferencial*. O que a torna parte de uma política determinística é a **regra** que a exige, como "nenhum merge sem check verde e sem aprovação de um revisor que não seja o autor". O governance deste próprio repositório é um exemplo: quem escreve não revisa, e o PR do Claude é revisado pelo Codex.

### 1.6 Exemplos aplicados à pesquisa (prosa vs. regra)

| Objetivo | Em prosa (probabilístico) | Travado (determinístico) |
|---|---|---|
| **Proteger dados brutos** | "Nunca edite `data/raw/`" no `AGENTS.md` | (a) Claude Code: `"deny": ["Edit(./data/raw/**)", "Write(./data/raw/**)"]`. (b) Hook `PreToolUse` que sai com exit 2 quando o caminho começa com `data/raw/`. (c) Sandbox com `filesystem.denyWrite`, que pega também scripts R ou Python. (d) Ruleset do GitHub restringindo o caminho `data/raw/**`. (e) Permissão somente leitura no sistema operacional |
| **Exigir validação do codebook** | "Valide o codebook antes de terminar" | Hook `Stop` que roda `Rscript tools/validar_codebook.R` e devolve `decision: "block"` com o erro, obrigando o agente a continuar até passar. Mais um **required status check** no CI e um CODEOWNERS de `codebook/` apontando para a pesquisadora responsável |
| **Impedir caminhos absolutos** | "Use caminhos relativos" | `pre-commit` que roda um grep por caminhos de máquina (do tipo `C:/.../Users/...` ou `/home/<usuário>/`) nos arquivos em stage e recusa o commit, repetido no CI. Este repositório já faz isso em `tools/git-hooks/` |
| **Registrar autoria do agente** | "Assine seus commits" | `commit-msg` que exige o trailer `Agent: <harness> / <modelo> / <plataforma>`, mais um workflow `commit-attribution` no CI. Também existe a regra de ruleset para *metadata restrictions* |
| **Reprodutibilidade** | "Garanta que o código roda" | Workflow que, num runner limpo, faz `renv::restore()` ou `uv sync`, roda o pipeline (`targets::tar_make()`, `quarto render`) e compara os resultados com valores esperados. Fica como *required status check* da `main` |
| **Não vazar segredos ou dados pessoais** | "Não coloque chaves no código" | Push protection, regra `Read(./.env)` deny, sandbox com rede restrita e máscara de credenciais |
| **Não apagar nada** | "Cuidado com `rm`" | `deny: ["Bash(rm -rf *)"]` ou hook, mais "Block force pushes" no ruleset |

### 1.7 Literatura e blogs de referência

- **Simon Willison, "The lethal trifecta for AI agents"** (16/06/2025). A combinação que deve ser evitada é: (1) acesso a dados privados, (2) exposição a conteúdo não confiável e (3) capacidade de se comunicar com o exterior. Willison considera "95% de detecção" uma nota de reprovação em segurança: é melhor cortar uma das três pernas do que confiar em guardrail probabilístico [oficial]: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- **OWASP Top 10 for Agentic Applications (2026)**, publicado em dezembro de 2025 pelo OWASP GenAI Security Project. A lista vai de ASI01 Agent Goal Hijack a ASI10 Rogue Agents e inclui Tool Misuse, Identity & Privilege Abuse, Supply Chain, Unexpected Code Execution, Memory/Context Poisoning, Insecure Inter-Agent Communication, Cascading Failures e Human-Agent Trust Exploitation. A lista veio de fontes secundárias (Giskard, Teleport e outras): https://goteleport.com/blog/owasp-top-10-agentic-applications. A página oficial deve estar em genai.owasp.org [não confirmado diretamente].
- **Anthropic, "Making Claude Code more secure and autonomous" (sandboxing)**, 20/10/2025: https://www.anthropic.com/engineering/claude-code-sandboxing
- **Böckeler, "Harness engineering for coding agent users"**, 02/04/2026: https://martinfowler.com/articles/harness-engineering.html
- **Especificação do MCP**, seção de segurança: as descrições de ferramentas devem ser tratadas como não confiáveis, e o protocolo "não pode impor" esses princípios, que cabem a quem implementa: https://modelcontextprotocol.io/specification/latest

---

## Bloco 2. Modelos atuais (outubro de 2026)

### 2.1 Anthropic (Claude) [oficial, consultado em 2026-10-05]

Fontes: https://platform.claude.com/docs/en/about-claude/models/overview e https://platform.claude.com/docs/en/about-claude/pricing

| Modelo | ID da API | Entrada (US$/MTok) | Saída (US$/MTok) | Contexto | Observação |
|---|---|---|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | 10 | 50 | 1M | Para raciocínio exigente e trabalho agêntico longo. Cache read de US$ 0,25 |
| Claude Opus 5.5 | `claude-opus-5-5` | 4 | 20 | 1M | Ponto de partida recomendado pela Anthropic. Lançado em **22/09/2026**. Cache read de US$ 0,20 |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | 2 | 10 | 1M | "Melhor combinação de velocidade e inteligência" |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | 1 | 5 | 200K | O mais rápido. Aposentadoria "não antes de 15/10/2026" |
| Claude Mythos 5 / 5.1 | (acesso limitado, Project Glasswing) | 10 | 50 | | Só por convite |
| Legados ainda disponíveis | Fable 5, Opus 5 (US$ 5/25), Opus 4.8, 4.7, 4.6, 4.5, Sonnet 5 (US$ 2/10), Sonnet 4.6 (US$ 3/15) | | | | |

- Batch API com **50% de desconto**. Cache read custa 0,1x da entrada (0,05x no Opus 5.5 e 0,025x no Fable 5.1).
- **Tokenizador novo** a partir do Opus 4.7: gera cerca de **30% mais tokens** para o mesmo texto. Leve isso em conta nas estimativas de custo.
- **Opus 5.5 contra o Opus 5**, números do anúncio oficial (https://www.anthropic.com/news/claude-opus-5-5) [oficial]:
  - Terminal-Bench 4.0: 66,4% contra 52,3%
  - OSWorld 2.1: 81,8% contra 74,0% (parcial)
  - GDPval-AA v2.1: Elo 1846 contra 1708
  - A Anthropic estima custo típico cerca de 40% menor
- A comparação com o GPT-6 Astra (Terminal-Bench 4.0: 66,4% contra 57,9%) aparece em imprensa [secundária]: https://officechai.com/ai/claude-opus-5-5-benchmarks/

### 2.2 OpenAI (GPT) [oficial, consultado em 2026-10-05]

Fontes: https://developers.openai.com/api/docs/models e https://developers.openai.com/api/docs/pricing

| Modelo | Entrada | Entrada em cache | Saída (US$/MTok) | Contexto | Observação |
|---|---|---|---|---|---|
| GPT-6 Astra (`gpt-6-astra`) | 10 | 1,00 | 50 | 1,05M | Topo de linha. Lançamento no início de set/2026 (3 ou 4/09, conforme a imprensa) [secundária: https://news.bgov.com/artificial-intelligence/openai-rolls-out-gpt-6-astra-model-with-cyber-guardrails-1] |
| GPT-6.1 Sol (`gpt-6.1-sol`) | 2 | 0,10 | 10 | 1,05M | "Desempenho próximo do Astra, a custo menor" |
| GPT-6 Sol (`gpt-6-sol`) | 2 | 0,20 | 10 | | |
| GPT-6 Luna (`gpt-6-luna`) | 0,10 | 0,01 | 0,50 | 1,05M | Alto volume e baixo custo |
| GPT-5.6 Sol / Terra / Luna | 4 / 2 / 0,20 | | 20 / 12 / 1,20 | | Geração anterior |
| GPT-5.5 | 5 | | 30 | | **Sai do ChatGPT e do Codex em 14/10/2026** [oficial: https://learn.chatgpt.com/docs/pricing] |

- Batch com 50% de desconto.
- **Transcrição de áudio** (US$/min): `gpt-transcribe` 0,0045; `gpt-4o-transcribe` 0,006; `gpt-4o-mini-transcribe` 0,003; Whisper 0,006.
- As páginas openai.com/api/pricing e chatgpt.com/pricing deram 403. Usei developers.openai.com e learn.chatgpt.com, que são oficiais.

### 2.3 Google (Gemini) [oficial, consultado em 2026-10-05]

Fontes: https://ai.google.dev/gemini-api/docs/models e https://ai.google.dev/gemini-api/docs/pricing

| Modelo | Entrada | Saída (US$/MTok) | Observação |
|---|---|---|---|
| Gemini 3.8 Flash | 0,75 | 3,75 | Flash mais recente. A página anuncia aumento de preço da família 3.x em 01/01/2027 |
| Gemini 3.7 Flash / 3.6 Flash | 0,75 | 3,75 | |
| Gemini 3.5 Flash | 1,50 | 9,00 | |
| Gemini 3.5 Flash-Lite | 0,30 | 2,50 | |
| Gemini 3.1 Pro (preview) | 2,00 | 12,00 | Até 200K tokens de prompt. Segundo a página de modelos, ainda é o Pro mais capaz. **Não achei um "3.5 Pro" ou posterior** [não confirmado; vale checar perto da aula] |
| Gemini 3.5 Transcribe | US$ 0,003/min de áudio | | Conforme a página de preços, ainda a reconferir |

Batch com cerca de 50% de desconto.

### 2.4 Modelos chineses e abertos

| Família | Situação em out/2026 | Preço de API (US$/MTok) | Confiabilidade e fonte |
|---|---|---|---|
| **DeepSeek** | `deepseek-flash` (V4-Flash, 1M de contexto, visão, modo thinking) e **V4-Pro**. Pesos abertos sob licença MIT. Preview em 24/04/2026; Flash oficial em 31/07/2026 | Flash: entrada 0,15–0,30 (cache miss), saída 0,60–1,20. V4-Pro: 0,66–1,32 / 1,98–3,96. Fora do horário de pico pela metade do preço | Preços [oficial]: https://api-docs.deepseek.com/quick_start/pricing. Datas [secundária]. Se o V4-Pro já saiu do preview [não confirmado] |
| **Qwen (Alibaba)** | Qwen3.8 anunciado em jul/2026. Repositório oficial lista **Qwen3.8-2.4T-A95B** (12/08/2026) e **Qwen3.8-27B** (14/08/2026) com pesos abertos, além do Qwen3.6-27B e do Qwen3.5 em vários tamanhos | Não conferi o preço oficial da API | [oficial] https://github.com/QwenLM/Qwen3.8 (README). Detalhes do Max [secundária] |
| **Kimi (Moonshot)** | **Kimi K3**, 1M de contexto, API desde 16/07/2026. Pesos prometidos sob Modified MIT | K3: 3 / 15 (cache 0,30). K2.7-code: 0,95 / 4,00. K2.6: 0,95 / 4,00 | Preços [oficial]: https://platform.kimi.ai/docs/pricing/chat. Pesos efetivamente publicados [não confirmado] |
| **Mistral** | Medium 3.5 (v26.04, Modified MIT), Small 4 (v26.03, Apache 2.0), Large 3 (v25.12, Apache 2.0), Ministral 3, Codestral. A documentação lista também o GLM 5.3 (Z.ai) como modelo hospedado | Não conferi o preço | [oficial] https://docs.mistral.ai/getting-started/models/models_overview/ |
| **Meta (Llama / Muse)** | O portal de desenvolvedor da Meta (dev.meta.ai) destaca agora a família **Muse** (Muse Spark 1.3 para código e agentes, via API; Muse Glimmer no Hugging Face). As notícias sobre "Llama 4.5" e "Llama 5" são contraditórias | | Linha Muse [oficial]: https://dev.meta.ai/. Situação do Llama aberto em 2026 [não confirmado] |
| **Z.ai (GLM)** | GLM 5.3, pesos abertos, citado como 1º no Terminal-Bench 3.0 em agregador (10/09/2026) | | [secundária] |

### 2.5 Planos de assinatura e o que incluem de agente

| Plano | Preço mensal (USD) | Agente incluído | Fonte |
|---|---|---|---|
| Claude Free | 0 | Chat, criação de arquivos e execução de código | [oficial] https://claude.com/pricing |
| **Claude Pro** | 20 (17 no anual) | **Claude Code**, Projects, Design/Slides/Docs | idem |
| **Claude Max** | a partir de 100 (5x ou 20x o Pro) | Claude Code com limite maior e acesso prioritário | idem |
| Claude Team | 25 por assento (20 no anual); assento premium 125 (100 no anual) | Claude Code e Cowork | idem |
| ChatGPT Free / Go | 0 / 8 | **Codex incluído em todos os planos** (com limites) | [oficial] https://learn.chatgpt.com/docs/pricing |
| **ChatGPT Plus** | 20 | Codex (CLI, app, IDE, nuvem). Modelos GPT-6 Luna e GPT-6.1 Sol | idem |
| **ChatGPT Pro** | 100, 200 ou 500 | Codex com limites maiores. GPT-6 Astra; "Ultrafast" no plano de 500 | idem |
| ChatGPT Business | 20 por usuário (anual, 2 usuários ou mais) | Codex | idem |
| Google AI Pro | não conferido nesta fonte (mercado cita US$ 20) | Gemini CLI, Antigravity e limites maiores | [secundária] |
| **Google AI Ultra** | 100 (5x o Pro) ou 200 (20x; antes 250) | Acesso prioritário ao **Antigravity**. Uso medido por computação, renovado a cada 5h | [oficial] https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions (I/O 2026) |

**Recado para a turma:** os planos de assinatura cobram por "janela de 5 horas" com limite de uso, e não por token. Para uso interativo (Claude Code, Codex) costumam sair mais baratos que a API. Para processar um corpus em lote, a **Batch API** costuma ser mais previsível.

### 2.6 Ordens de grandeza de custo para tarefas de pesquisa

São cálculos meus a partir dos preços oficiais acima. São estimativas, não cotações.

**Cenário A: classificar 1.000 documentos.** Cada documento tem cerca de 2.000 tokens. O prompt e o codebook somam 500 tokens e ficam em cache. A saída é um rótulo em JSON de cerca de 100 tokens. Total aproximado: 2,5M tokens de entrada e 0,1M de saída. O custo de cache, que é pequeno, ficou de fora.

| Modelo | Preço padrão | Com Batch (-50%) |
|---|---|---|
| GPT-6 Luna | ~US$ 0,30 | ~US$ 0,15 |
| DeepSeek Flash (horário de pico) | ~US$ 0,87 | (fora do pico ~US$ 0,44) |
| Gemini 3.8 Flash | ~US$ 2,25 | ~US$ 1,10 |
| Claude Haiku 4.5 | ~US$ 3,00 | ~US$ 1,50 |
| Claude Sonnet 5.5 / GPT-6.1 Sol | ~US$ 6,00 | ~US$ 3,00 |
| Claude Opus 5.5 | ~US$ 12,00 | ~US$ 6,00 |
| GPT-6 Astra | ~US$ 30,00 | ~US$ 15,00 |

Ressalvas:

- Texto em português tende a gerar mais tokens que em inglês.
- O tokenizador novo do Claude produz cerca de 30% mais tokens.
- Modelos com **raciocínio** ("thinking") podem multiplicar os tokens de saída por 10 ou mais. Se o raciocínio estiver ligado, reestime.
- **Conclusão:** de centavos a algumas dezenas de dólares por mil documentos. O custo dominante é o **tempo de validação humana** do codebook e da amostra de concordância, não a API.

**Cenário B: transcrever 10 horas de áudio (600 min).**

| Serviço | Custo |
|---|---|
| `gpt-4o-mini-transcribe` (US$ 0,003/min) | ~US$ 1,80 |
| Gemini 3.5 Transcribe (US$ 0,003/min, a reconferir) | ~US$ 1,80 |
| `gpt-transcribe` (US$ 0,0045/min) | ~US$ 2,70 |
| `gpt-4o-transcribe` ou Whisper API (US$ 0,006/min) | ~US$ 3,60 |
| Whisper local | US$ 0, mais o tempo de máquina. Recomendável quando o áudio tem dados sensíveis (comitê de ética, LGPD) |

**Cenário C: uma sessão agêntica de 1 hora.** O exemplo oficial do Claude Managed Agents, com Opus 5, 50k tokens de entrada e 15k de saída, dá cerca de **US$ 0,70** por hora, já incluída a taxa de US$ 0,08/h de runtime [oficial, página de pricing]. Sessões reais de Claude Code ou Codex leem muito mais contexto: na prática, de alguns a dezenas de dólares por dia de uso intenso via API [estimativa; não confirmado em fonte].

### 2.7 Benchmarks de agência (com datas)

| Benchmark | O que mede | Situação recente | Fonte |
|---|---|---|---|
| **METR time horizon** | Duração (em tempo de especialista humano) das tarefas que o agente completa com 50% de sucesso | Última atualização da página: **08/05/2026** (Claude Mythos Preview inicial). A página avisa que **medidas acima de 16 h não são confiáveis** com a suíte atual. Valores citados por terceiros: Mythos Preview ~17,4 h; Opus 4.6 ~14,5 h; GPT-5.3-Codex ~6,5 h; Claude 3.7 Sonnet (fev/2025) 59 min | Página [oficial]: https://metr.org/time-horizons/. Valores [secundária]: https://www.greaterwrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year (fala em dobra a cada ~3,5 meses). Medição do Opus 5.5 ou do GPT-6 [não confirmado: não achei] |
| **Terminal-Bench** | Tarefas reais no terminal (agente mais harness) | Versão 4.0 citada no anúncio do Opus 5.5 (66,4%, set/2026). Agregadores ainda listam a 3.0, com resultados diferentes conforme o harness | [oficial] anúncio da Anthropic. Ranking em https://www.tbench.ai/leaderboard (não renderizou no fetch) |
| **SWE-bench (Verified / Pro)** | Correção de issues reais do GitHub | Agregadores: Mythos Preview 77,8% no SWE-bench Pro (jun/2026); Opus 5 com 79,2% [secundária]. **Não consegui ler o leaderboard oficial** (https://www.swebench.com/). Vale avisar que o Verified está saturado e possivelmente contaminado, mas essa afirmação [não confirmado nesta pesquisa] | [secundária] https://benchmarklist.com/benchmarks/swe_bench_pro/ |
| **OSWorld** | Uso de computador (GUI) | Opus 5.5: 81,8% no OSWorld 2.1 (parcial) | [oficial] anúncio da Anthropic |

**Mensagem pedagógica:** o benchmark mede **modelo e harness juntos**. O mesmo modelo muda de pontuação conforme o harness (mini-SWE-agent, Claude Code, Codex). Isso amarra o Bloco 2 ao Bloco 3.

---

## Bloco 3. Harnesses

### 3.1 Definições

- **Fórmula curta:** "Agent = Model + Harness". O harness é tudo o que não é o modelo, e o usuário constrói um "harness externo" para o seu caso de uso (Böckeler, martinfowler.com, 02/04/2026) [oficial do autor].
- **Anthropic:** em "Effective harnesses for long-running agents", "harness" é o arcabouço em volta do modelo que permite trabalhar através de várias janelas de contexto. Os componentes são:
  - um agente inicializador que cria `init.sh`, o arquivo de progresso `claude-progress.txt` e uma lista de funcionalidades em JSON, todas marcadas como falhando;
  - commits frequentes no git, usado como memória e como forma de reverter.

  Fonte: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents. O fetch não mostrou a data; pela minha memória é de novembro de 2025 [não confirmado].
- **OpenAI:** "harness engineering" é o trabalho de projetar o ambiente, as restrições e os ciclos de feedback que tornam os agentes do Codex confiáveis: linters e testes estruturais, `AGENTS.md` como mapa e observabilidade. Post original em openai.com (403). Resumo pela InfoQ (21/02/2026) [secundária].
- **Definição operacional para a aula:** o harness é o programa que (1) monta o contexto (instruções, `AGENTS.md`, skills), (2) oferece as ferramentas (shell, edição, web, MCP), (3) executa o laço modelo, ferramenta, resultado, (4) **impõe limites** (permissões, sandbox, hooks) e (5) guarda o estado entre sessões (git, arquivos de progresso, memória).

### 3.2 Panorama de agentes de terminal e IDE (out/2026)

| Agente | Tipo | Modelos | Hooks | Skills (padrão aberto) | Subagentes | MCP | `AGENTS.md` | Sandbox nativo | Observações e fontes |
|---|---|---|---|---|---|---|---|---|---|
| **Claude Code** (Anthropic) | CLI, IDE, desktop, web e nuvem | Claude | Sim (mais de 25 eventos) | Sim | Sim | Sim | Lê `CLAUDE.md`; o `CLAUDE.md` pode importar `@AGENTS.md`, como neste repositório | Sim (Bash; macOS, Linux e WSL2; não no Windows nativo) | https://code.claude.com/docs [oficial] |
| **Codex** (OpenAI) | CLI de código aberto, app desktop (macOS em 02/02/2026, Windows em 04/03/2026), IDE e nuvem | GPT | Sim | Sim | Sim | Sim | Sim (formato nativo) | Sim (Seatbelt, bwrap+seccomp, Windows) | Hooks e sandbox [oficial]. Datas do app [secundária]: https://intuitionlabs.ai/articles/openai-codex-app-ai-coding-agents |
| **Gemini CLI** (Google) | CLI de código aberto | Gemini | Sim (11 eventos) | Sim (padrão desde a v0.26, 27/01/2026) | Sim (desde 15/04/2026) | Sim | Sim | Sim (Seatbelt, Docker/Podman, gVisor) | Hooks e sandbox [oficial]. Datas [secundária] |
| **Antigravity** (Google) | IDE "agent-first" (fork do VS Code), anunciado em 18/11/2025 | Gemini e outros | Não confirmado | Não confirmado | Agent Manager (vários agentes em paralelo) | Não confirmado | Não confirmado | Políticas de terminal e de revisão | [secundária] codelab do Google |
| **OpenCode** | CLI e desktop de código aberto, multi-provedor | Vários | Via plugins | Sim | Não confirmado | Sim | Não confirmado | Não confirmado | https://opencode.ai/docs [oficial] |
| **goose** (Block, hoje na AAIF) | CLI e desktop de código aberto (Rust), multi-provedor | Vários | Não achei | Sim | Sim (subagentes paralelos) | Sim (nativo) | Sim | 4 modos de permissão | Repositório transferido para a organização `aaif-goose` em 07/04/2026 [secundária] |
| **Cursor** | IDE e agentes na nuvem | Vários | Sim | Sim | Sim | Sim | Sim | Não confirmado | https://cursor.com/docs [oficial] |
| **Aider** | CLI de código aberto | Vários | Não (só lint e teste automáticos) | Não confirmado | Não | Não confirmado | Sim (lista do agents.md) | Não | https://aider.chat [oficial] |
| **GitHub Copilot** (agente) | IDE, CLI e coding agent na nuvem (GitHub Actions) | Vários | Não confirmado | Sim | Não confirmado | Sim | Sim | Firewall na nuvem | Docs do GitHub [oficial] |

### 3.3 Containerização e sandbox: resumo para quem não programa

| Nível | O que isola | Esforço | Quando usar |
|---|---|---|---|
| Permissões do harness (allow, ask, deny) | Decisões do agente | Baixo | Sempre |
| Sandbox nativo (Claude Code `/sandbox`, Codex `workspace-write`, `gemini -s`) | Comandos de shell: disco e rede | Baixo (no Windows, só via WSL2 no Claude Code) | No dia a dia, para reduzir prompts de permissão |
| Sandbox runtime da Anthropic (`npx @anthropic-ai/sandbox-runtime claude`) | O processo inteiro do agente, inclusive MCP e hooks | Baixo a médio (beta) | Quando se quer isolar também o MCP |
| **Devcontainer** (Docker com VS Code) | Ambiente de desenvolvimento inteiro | Médio (exige Docker) | Padronizar o ambiente da equipe e rodar sem supervisão |
| VM / microVM (Docker Sandboxes, Firecracker) | Sistema operacional inteiro | Alto | Código não confiável |
| **Nuvem** (Claude Code na web, Codex Cloud, Copilot coding agent, Jules) | VM ou container do fornecedor, com proxy de rede | Nenhum (exige plano e, em geral, GitHub) | Delegar tarefas de forma assíncrona |

Fonte da tabela: https://code.claude.com/docs/en/sandbox-environments [oficial, 2026-10-05], complementada pelas docs do Codex e do Gemini citadas acima.

**Aviso da própria documentação:** o isolamento **não muda o que é enviado ao modelo**. Os arquivos que o agente lê vão para a API do fornecedor. Para dados sensíveis (entrevistas, microdados identificados), o sandbox não resolve a questão de privacidade e LGPD: é preciso decidir **quais dados o agente pode ler**.

### 3.4 Padrões abertos

| Padrão | O que é | Governança e adoção | Fonte |
|---|---|---|---|
| **MCP (Model Context Protocol)** | Protocolo JSON-RPC entre host, cliente e servidor. Os servidores expõem **tools**, **resources** e **prompts**; os clientes oferecem **elicitation**. Tem extensões opcionais (Tasks, Skills over MCP, MCP Apps) | Revisão mais recente da especificação: **2026-07-28**. Doado à AAIF | [oficial] https://modelcontextprotocol.io/specification/latest |
| **AGENTS.md** | Arquivo Markdown livre, sem campos obrigatórios, com instruções para agentes: build, testes, convenções | Mantido pela AAIF. Mais de 60 mil projetos de código aberto. Suportado por Codex, Copilot, Jules, Gemini CLI, Cursor, Aider, Devin, Zed, Warp, Junie e outros | [oficial] https://agents.md/ |
| **Agent Skills** (`SKILL.md`) | Pasta com `SKILL.md` (frontmatter com `name` e `description`, depois instruções) e, opcionalmente, `scripts/`, `references/` e `assets/`. Usa **divulgação progressiva**: no início só se carrega nome e descrição, e o resto só quando a skill é ativada | Criado pela Anthropic e aberto em dez/2025 [data secundária]. Mais de 40 clientes na vitrine oficial: Claude Code, Codex/ChatGPT, Gemini CLI, Cursor, GitHub Copilot, VS Code, OpenCode, goose, OpenHands, Junie, Mistral Vibe, Kiro e outros | [oficial] https://agentskills.io/ |
| **Agentic AI Foundation (AAIF)** | Fundação da Linux Foundation para padrões de agentes | Criada em **09/12/2025** com MCP (Anthropic), goose (Block) e AGENTS.md (OpenAI). Membros platinum: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft e OpenAI | [oficial] https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation. Atenção: o fetch de aaif.io devolveu uma página genérica de "working groups" que não batia com isso [conteúdo atual do site não confirmado] |

---

## Implicações para as aulas

### O que mostrar em slide

1. **Um slide-tese:** "Prosa orienta, regra garante." À esquerda, uma linha do `AGENTS.md` ("não edite `data/raw/`"). À direita, a regra `deny` e o hook que fazem o mesmo de forma impositiva. Citação curta da documentação do Claude Code: as regras de permissão são "enforced by Claude Code, not by the model".
2. **Escada de camadas** (diagrama da seção 1.5): prompt, harness, git hooks, CI/rulesets, revisão. Marcar o que é probabilístico e o que é determinístico, e o que é local e o que roda no servidor (`--no-verify` existe, o ruleset não se contorna).
3. **Grade guides × sensors e computacional × inferencial** de Böckeler, com exemplos de pesquisa: o codebook como guide, os testes de validação como sensor computacional e a revisão por outro agente como sensor inferencial.
4. **Lethal trifecta** (Willison): dados privados, conteúdo não confiável e saída para fora. Exemplo de ciência política: um agente que lê e-mails de entrevistados, navega na web e pode enviar mensagens.
5. **Os dois "code as policy"**: Liang et al. 2022 (o LLM gera a política do robô) contra "policy as code" (nós codificamos as regras do agente). É um slide curto para desfazer a confusão terminológica.
6. **Tabela de modelos e preços**, com a data "out/2026" em destaque e o aviso de que muda em semanas. Mostrar só 6 a 8 linhas: Opus 5.5, Sonnet 5.5, Haiku 4.5, GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Gemini 3.8 Flash, DeepSeek Flash.
7. **Custo de mil documentos**, para mostrar que o gargalo é a validação e não o dinheiro (de centavos a cerca de US$ 30).
8. **"Benchmark mede modelo + harness"**, com o METR time horizon (curva exponencial e aviso de que acima de 16 h a medida não é confiável) e a variação de pontuação conforme o harness.
9. **Mapa dos padrões abertos:** AGENTS.md (o quê), Skills (como), MCP (com quê) e AAIF (quem governa). A mensagem é que o investimento num formato não prende a um fornecedor.

### Demonstrações sugeridas (ao vivo, 5 a 10 min cada)

1. **Pedir contra travar.**
   - Num repositório de exemplo com `data/raw/eleicoes.csv`, pedir ao agente: "corrija os nomes de municípios direto no CSV bruto". Primeiro só com a regra no `AGENTS.md`: o agente pode obedecer ou não. Depois com `"deny": ["Edit(./data/raw/**)"]` em `.claude/settings.json`, mostrando o bloqueio.
   - Fechar com um script R que escreve no arquivo, para mostrar que a regra deny **não** pega isso e que é preciso o sandbox (no Windows, WSL2) ou permissão de arquivo no sistema operacional.
2. **Hook `Stop` validando o codebook.** Um hook que roda `Rscript tools/validar_codebook.R`. Se alguma categoria do resultado não estiver no codebook, devolve `decision: "block"` e o agente é obrigado a corrigir antes de encerrar.
3. **Git hooks deste repositório.** Tentar commitar sem o trailer `Agent:` ou com um caminho absoluto de máquina e mostrar a recusa do `tools/git-hooks/commit-msg` e do `pre-commit`. Depois mostrar que o mesmo teste roda no CI (workflow `commit-attribution`), porque o hook local pode ser pulado.
4. **GitHub como juiz.**
   - Abrir um PR feito pelo agente.
   - Mostrar o *required status check* de reprodutibilidade (`quarto render` e testes) falhando e depois passando.
   - Mostrar o ruleset que exige PR e aprovação, mais o CODEOWNERS do `codebook/`.
   - Comentar `@codex review` (ou acionar o Claude Code Action) para a revisão cruzada: "quem escreve não revisa".
5. **Push protection.** Num repositório **público** de teste, tentar dar push de um arquivo com um token falso no formato real e mostrar o bloqueio. Usar só token de exemplo inválido, nunca credencial real.
6. **Mesmo modelo, harnesses diferentes.** A mesma tarefa curta (por exemplo, "padronize os nomes de partidos e gere uma tabela de frequências") no Claude Code e no Codex ou Gemini CLI, comparando as permissões pedidas, o sandbox e o rastro deixado no git.
7. **Calculadora de custo ao vivo.** Contar os tokens de 10 documentos reais (endpoint de contagem de tokens ou `tiktoken`) e extrapolar para mil com a tabela de preços. Discutir a Batch API e o cache.

### Cuidados

- Rever **todos os preços e nomes de modelos na véspera**. O GPT-5.5 sai do ChatGPT e do Codex em **14/10/2026**, e o Haiku 4.5 pode ser aposentado a partir de **15/10/2026**.
- Itens marcados como **[não confirmado]** não devem ir para slide sem checagem: Llama em 2026, Gemini Pro posterior ao 3.1, valores do METR para modelos de set/2026, ranking oficial do SWE-bench, página oficial da OWASP, data do post de harnesses da Anthropic, pesos do Kimi K3.
- Para usuários Windows na plateia: o sandbox do Claude Code **não funciona no Windows nativo**. Recomendar WSL2 ou devcontainer, ou usar o Codex, que tem sandbox nativo no Windows.
- Dados sensíveis: o sandbox não impede o envio de conteúdo ao fornecedor. Discutir anonimização, modelos locais ou abertos (Qwen, DeepSeek, Mistral com pesos abertos) e exigências do comitê de ética.
