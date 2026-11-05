# =============================================================================
# verificar_integridade_brutos.R  — hook PostToolUse (Bash) e Stop
#
# PT: Segunda camada de proteção dos dados brutos. O hook proteger_dados_brutos.R
#     é uma barreira ANTES da ação, mas só enxerga o texto do comando: um script
#     (ex.: Rscript limpar.R) pode alterar dados/brutos sem que o caminho apareça.
#     Este hook é um SENSOR: depois de cada comando de terminal, e antes de o
#     agente encerrar, pergunta ao Git se dados/brutos/ difere da última versão
#     registrada (arquivo alterado, apagado, novo ou oculto). Qualquer diferença,
#     seja qual for o programa que a causou, devolve um alerta ao agente (exit 2)
#     e o impede de encerrar até que os dados sejam restaurados.
#     Por que o Git, e não uma lista de hashes num arquivo? Porque um script que
#     altera os dados também poderia reescrever essa lista: o agente não pode
#     guardar o próprio boletim. O histórico do Git só muda com um commit, que
#     fica visível; e, num projeto real, o servidor (GitHub) pode recusar
#     commits que mexam em dados/brutos.
#     O sensor não desfaz a alteração: avisa e trava. A restauração é feita com
#     git checkout -- dados/brutos (e git clean para arquivos novos).
#
# EN: Second layer protecting the raw data. After every shell command and
#     before the agent stops, asks Git whether dados/brutos/ differs from the
#     last committed version (modified, deleted, new or hidden files). Git is the
#     reference because a script that alters the data could also rewrite a
#     checksum file; the agent must not hold its own report card.
# =============================================================================

raiz <- Sys.getenv("CLAUDE_PROJECT_DIR", unset = getwd())

# PT: o stdin do hook não é usado, mas é lido para não deixar o processo pendurado.
# EN: stdin is unused but drained.
invisible(readLines(file("stdin"), warn = FALSE))

setwd(raiz)
estado <- suppressWarnings(system2(
  "git",
  c("status", "--porcelain", "--ignored", "--untracked-files=all", "--", "dados/brutos"),
  stdout = TRUE, stderr = TRUE
))
codigo <- attr(estado, "status")

if (!is.null(codigo) && codigo != 0) {
  message(
    "ALERTA do hook verificar_integridade_brutos.R: não foi possível consultar o Git ",
    "(o projeto precisa estar num repositório Git para a verificação de integridade).\n",
    paste(estado, collapse = "\n")
  )
  quit(status = 2)
}

if (length(estado) == 0) quit(status = 0)

message(
  "ALERTA do hook verificar_integridade_brutos.R: os dados brutos diferem da última ",
  "versão registrada no Git.\n",
  paste0("- ", estado, collapse = "\n"), "\n",
  "Pare o que estiver fazendo, restaure os dados com `git checkout -- dados/brutos` ",
  "(e `git clean -fdx dados/brutos` para arquivos novos) e explique ao pesquisador o que ",
  "aconteceu. Os dados brutos são somente leitura (ver AGENTS.md)."
)
quit(status = 2)
