# =============================================================================
# registrar_acoes.R  — hook PostToolUse (rastreabilidade / traceability)
#
# PT: Acrescenta uma linha em logs/registro-agente.jsonl para cada ação do
#     agente que modifica arquivos ou roda comandos e que foi concluída com
#     sucesso (o PostToolUse só dispara depois de ações bem-sucedidas). Leituras
#     e buscas não entram, e as tentativas bloqueadas ficam na tela, não aqui.
#     É um "caderno de laboratório" automático das mudanças: permite
#     reconstruir depois o que o agente alterou, mesmo que a conversa se perca.
#     Para comandos de terminal, guarda só o programa chamado e os caminhos de
#     arquivo citados, nunca o comando inteiro: um comando pode conter dados,
#     textos longos ou credenciais que não devem ficar gravados no log.
#
# EN: Appends one line to logs/registro-agente.jsonl for every successful
#     agent action that edits files or runs commands. Reads, searches and
#     blocked attempts are not recorded. For shell commands only the program
#     and the file paths mentioned are kept, never the full command line, which
#     may contain data or credentials.
# =============================================================================

`%||%` <- function(x, y) if (is.null(x)) y else x

entrada <- jsonlite::fromJSON(
  paste(readLines(file("stdin"), warn = FALSE), collapse = "\n"),
  simplifyVector = FALSE
)

parametros <- entrada$tool_input %||% list()

# PT: Resume um comando de terminal: primeira palavra (o programa) e os tokens
#     que parecem caminhos de arquivo do projeto.
# EN: Summarise a shell command: the program plus tokens that look like paths.
resumir_comando <- function(comando) {
  linha <- trimws(strsplit(comando, "\n", fixed = TRUE)[[1]][1])
  # PT: descarta, ANTES de separar as palavras, as atribuições de variável no
  #     início (API_TOKEN=segredo curl ..., inclusive TOKEN="valor com espaço")
  #     e os programas que só "embrulham" outro (env, sudo, nohup, time...).
  # EN: before splitting into words, drop leading VAR=value assignments
  #     (quoted values included) and wrapper programs.
  atribuicao <- "^(?:[A-Za-z_][A-Za-z0-9_]*=(?:\"[^\"]*\"|'[^']*'|[^[:space:]]*)[[:space:]]*)+"
  embrulho <- "^(?:env|sudo|nohup|time|command|exec)(?:[[:space:]]+|$)"
  repeat {
    nova <- sub(embrulho, "", sub(atribuicao, "", linha, perl = TRUE), perl = TRUE)
    if (identical(nova, linha)) break
    linha <- nova
  }
  # PT: se ainda sobrar uma atribuição com aspas no meio do comando, não se
  #     arrisca: nada do comando é registrado.
  # EN: if a quoted assignment remains mid-command, record nothing of it.
  if (grepl("[A-Za-z_][A-Za-z0-9_]*=[\"']", linha)) linha <- ""
  tokens <- strsplit(linha, "[[:space:]]+")[[1]]
  tokens <- gsub("^[\"']|[\"']$", "", tokens[nzchar(tokens)])
  if (length(tokens) == 0) return(list(programa = NA, caminhos = character(0)))
  caminhos <- unique(grep("^[[:alnum:]_./-]+\\.[[:alnum:]]+$|/", tokens[-1], value = TRUE))
  caminhos <- grep("^-|=|://", caminhos, value = TRUE, invert = TRUE)
  list(programa = tokens[1], caminhos = caminhos)
}

alvo <- if (!is.null(parametros$file_path)) {
  parametros$file_path
} else if (!is.null(parametros$command)) {
  resumir_comando(parametros$command)
} else {
  NA
}

registro <- list(
  momento    = format(Sys.time(), "%Y-%m-%dT%H:%M:%S%z"),
  sessao     = entrada$session_id %||% NA,
  ferramenta = entrada$tool_name %||% NA,
  alvo       = alvo
)

raiz <- Sys.getenv("CLAUDE_PROJECT_DIR", unset = getwd())
dir.create(file.path(raiz, "logs"), showWarnings = FALSE)

cat(
  jsonlite::toJSON(registro, auto_unbox = TRUE, na = "null"), "\n",
  sep = "",
  file = file.path(raiz, "logs", "registro-agente.jsonl"),
  append = TRUE
)

quit(status = 0)
