# =============================================================================
# validar_apos_escrita.R  — hook PostToolUse e Stop
#
# PT: Valida dados/processados/codificacao.csv com R/validar_codificacao.R
#     sempre que o arquivo puder ter mudado, qualquer que seja o caminho:
#     - depois de Edit/Write/MultiEdit nesse arquivo;
#     - depois de qualquer comando Bash, se o conteúdo do arquivo mudou desde a
#       última validação (um script R ou um redirecionamento do shell também
#       gravam o arquivo, e o hook não pode depender de qual ferramenta foi usada);
#     - quando o agente tenta encerrar a tarefa (evento Stop).
#     Se a validação falhar, devolve os problemas ao agente (exit 2), que precisa
#     corrigir o arquivo antes de seguir. O agente não "decide" se valida.
#     No Stop, o bloqueio se repete enquanto o arquivo continuar inválido. Para
#     não prender o agente num laço, há uma saída explícita e visível: mover o
#     arquivo para dados/processados/codificacao_invalida.csv (quarentena) e
#     explicar ao pesquisador. Apagar um resultado que já tinha sido validado,
#     sem quarentena, também bloqueia o encerramento.
#
# EN: Validates dados/processados/codificacao.csv with R/validar_codificacao.R
#     whenever the file may have changed: after Edit/Write/MultiEdit on it;
#     after any Bash command if its content changed since the last validation;
#     and when the agent tries to stop. On Stop the block repeats while the
#     file is invalid; the explicit way out is to quarantine the file and tell
#     the researcher. Deleting a previously validated result also blocks Stop.
# =============================================================================

`%||%` <- function(x, y) if (is.null(x)) y else x

entrada <- jsonlite::fromJSON(
  paste(readLines(file("stdin"), warn = FALSE), collapse = "\n"),
  simplifyVector = FALSE
)

# PT: O hook roda na raiz do projeto, onde o validador espera dados/brutos/.
# EN: Run from the project root, where the validator expects dados/brutos/.
raiz <- Sys.getenv("CLAUDE_PROJECT_DIR", unset = getwd())
setwd(raiz)

alvo <- "dados/processados/codificacao.csv"
quarentena <- "dados/processados/codificacao_invalida.csv"
marca <- "logs/.codificacao-validada.md5"
evento <- entrada$hook_event_name %||% "PostToolUse"
ferramenta <- entrada$tool_name %||% ""
caminho <- chartr("\\", "/", entrada$tool_input$file_path %||% "")

# PT: Arquivo ausente. Se nunca houve validação, não há o que checar.
#     Se houve (a marca existe, de versão aprovada ou reprovada) e o arquivo
#     sumiu sem ir para a quarentena, o resultado foi apagado: avisa depois do
#     comando e bloqueia o encerramento.
# EN: Missing file: fine if nothing was ever validated; if any version was
#     validated (passed or failed) and was deleted without quarantine, report
#     it and block stopping.
if (!file.exists(alvo)) {
  apagado <- file.exists(marca) && !file.exists(quarentena)
  if (apagado && (identical(evento, "Stop") || identical(ferramenta, "Bash"))) {
    message(
      "A codificação validada (", alvo, ") foi apagada. Recrie-a e valide-a ou, ",
      "se a exclusão foi intencional, mova uma cópia para ", quarentena,
      " e explique ao pesquisador."
    )
    quit(status = 2)
  }
  quit(status = 0)
}

hash_atual <- unname(tools::md5sum(alvo))
hash_validado <- if (file.exists(marca)) readLines(marca, warn = FALSE)[1] else ""

precisa_validar <- switch(
  evento,
  # PT: Ao encerrar, valida sempre. / EN: On Stop, always validate.
  Stop = TRUE,
  PostToolUse = if (ferramenta == "Bash") {
    !identical(hash_atual, hash_validado)
  } else {
    grepl(alvo, caminho, fixed = TRUE)
  },
  FALSE
)

if (!precisa_validar) quit(status = 0)

saida <- suppressWarnings(system2(
  "Rscript", c("R/validar_codificacao.R", alvo),
  stdout = TRUE, stderr = TRUE
))
status <- attr(saida, "status") %||% 0L

# PT: A marca registra toda validação, aprovada ou não. Assim, apagar um
#     arquivo que nunca passou na validação também conta como exclusão de um
#     resultado (e não como "projeto sem resultado ainda").
# EN: The marker records every validation, passed or failed, so deleting a
#     file that never passed is also treated as deleting a result.
dir.create("logs", showWarnings = FALSE)
if (status == 0) {
  writeLines(hash_atual, marca)
  quit(status = 0)
}
writeLines(paste0("invalida:", hash_atual), marca)

saida_de_emergencia <- if (identical(evento, "Stop")) {
  paste0(
    "\nSe não for possível corrigir, mova o arquivo para ", quarentena,
    " e explique ao pesquisador o que ficou pendente."
  )
} else {
  ""
}

message(
  "O arquivo de codificação não passou na validação automática ",
  "(R/validar_codificacao.R). Corrija os problemas abaixo antes de continuar:\n",
  paste(saida, collapse = "\n"),
  saida_de_emergencia
)
quit(status = 2)
