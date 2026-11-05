# =============================================================================
# proteger_dados_brutos.R  — hook PreToolUse
#
# PT: Roda ANTES de cada ação de edição/escrita ou comando de terminal do
#     agente. Se a ação tentar modificar algo em dados/brutos/, o hook bloqueia
#     (exit 2) e devolve ao agente uma explicação no stderr. É o equivalente a
#     um git hook "pre-commit": a regra dispara sempre, independentemente do
#     "bom senso" do modelo ou do que estiver escrito no AGENTS.md.
#
# EN: Runs BEFORE every edit/write action or shell command by the agent. If the
#     action tries to modify anything under dados/brutos/, the hook blocks it
#     (exit 2) and returns an explanation to the agent on stderr. Analogous to
#     a git "pre-commit" hook: the rule always fires, regardless of the model's
#     judgement or what AGENTS.md says.
#
# Protocolo / Protocol (Claude Code hooks):
#   - stdin: JSON com tool_name e tool_input / JSON with tool_name, tool_input
#   - exit 0: permite a ação / allow
#   - exit 2: bloqueia; stderr é mostrado ao agente / block; stderr goes to agent
# =============================================================================

`%||%` <- function(x, y) if (is.null(x)) y else x

entrada <- jsonlite::fromJSON(
  paste(readLines(file("stdin"), warn = FALSE), collapse = "\n"),
  simplifyVector = FALSE
)

ferramenta <- entrada$tool_name %||% ""
parametros <- entrada$tool_input %||% list()

pasta_protegida <- "dados/brutos"

bloquear <- function(motivo) {
  message(
    "BLOQUEADO pelo hook proteger_dados_brutos.R: ", motivo, "\n",
    "Os dados brutos são somente leitura neste projeto (ver AGENTS.md). ",
    "Grave resultados em dados/processados/."
  )
  quit(status = 2)
}

# -----------------------------------------------------------------------------
# Caso 1 / Case 1: ferramentas de edição de arquivos / file editing tools
# -----------------------------------------------------------------------------
if (ferramenta %in% c("Edit", "Write", "MultiEdit", "NotebookEdit")) {
  caminho <- parametros$file_path %||% parametros$notebook_path %||% ""
  # PT: normaliza separadores do Windows para a comparação funcionar em qualquer SO.
  # EN: normalise Windows separators so the check works on any OS.
  caminho <- gsub("\\\\", "/", caminho)
  if (grepl(pasta_protegida, caminho, fixed = TRUE)) {
    bloquear(paste0("tentativa de ", ferramenta, " em ", caminho, "."))
  }
}

# -----------------------------------------------------------------------------
# Caso 2 / Case 2: comandos de terminal / shell commands
#   PT: Adivinhar quais comandos "escrevem" não funciona: truncate, perl -pi ou
#       um script Python também alteram arquivos. Por isso a regra é invertida:
#       um comando que menciona a pasta protegida só passa se o programa estiver
#       numa lista curta de programas de LEITURA e não houver redirecionamento
#       de saída. Todo o resto é bloqueado.
#       Limite honesto: um script (ex.: Rscript analise.R) pode abrir dados/brutos
#       sem que o caminho apareça no comando. Para isso existe a segunda camada,
#       o sensor verificar_integridade_brutos.R, que compara o MD5 dos arquivos
#       com a referência em dados/brutos.md5 depois de cada comando. Na vida
#       real, some a isso permissões do sistema de arquivos (somente leitura)
#       ou montagem somente leitura no contêiner.
#   EN: Guessing which commands write does not work, so the rule is inverted:
#       a command mentioning the protected folder passes only if its program is
#       on a short read-only allowlist and there is no output redirection. A
#       script can still open the folder without naming it; the integrity
#       sensor (verificar_integridade_brutos.R) covers that case.
# -----------------------------------------------------------------------------
if (ferramenta == "Bash") {
  comando <- parametros$command %||% ""
  if (grepl(pasta_protegida, comando, fixed = TRUE)) {
    leitura <- c("cat", "head", "tail", "less", "more", "wc", "ls", "grep",
                 "diff", "md5sum", "sha256sum", "file", "stat")
    # PT: analisa cada trecho do comando (separado por ;, &&, || ou |).
    # EN: check each segment of the command (split on ;, &&, || or |).
    trechos <- trimws(strsplit(comando, "&&|[|]{1,2}|;|\n", perl = TRUE)[[1]])
    trechos <- trechos[nzchar(trechos)]
    for (trecho in trechos) {
      if (!grepl(pasta_protegida, trecho, fixed = TRUE)) next
      palavras <- strsplit(trecho, "[[:space:]]+")[[1]]
      # PT: ignora atribuições de variável no início (VAR=valor programa ...).
      palavras <- palavras[!cumprod(grepl("^[A-Za-z_][A-Za-z0-9_]*=", palavras))]
      programa <- basename(palavras[1] %||% "")
      if (!(programa %in% leitura) || grepl(">", trecho, fixed = TRUE)) {
        bloquear(paste0(
          "comando de terminal que toca ", pasta_protegida,
          " e não é uma leitura simples: `", trecho, "`."
        ))
      }
    }
  }
}

quit(status = 0)
