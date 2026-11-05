# =============================================================================
# validar_codificacao.R
#
# PT: Valida o arquivo de codificação produzido (por um humano ou por um agente)
#     contra o livro de códigos (codebook.md). É o exemplo central de
#     "code as policy" do minicurso: em vez de *pedir* ao agente que respeite o
#     formato, uma regra executável *verifica* o formato, sempre da mesma forma.
#
# EN: Validates the coding file (produced by a human or by an agent) against
#     the codebook. This is the workshop's core "code as policy" example:
#     instead of *asking* the agent to follow the format, an executable rule
#     *checks* it, the same way every time.
#
# Uso / Usage:
#   Rscript R/validar_codificacao.R [caminho/para/codificacao.csv]
#
# Saída / Exit status:
#   0 = arquivo válido / valid file
#   1 = arquivo inválido; os problemas são impressos no stderr
#       invalid file; problems are printed to stderr
# =============================================================================

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(stringr)
})

# -----------------------------------------------------------------------------
# 1. Parâmetros do livro de códigos / Codebook parameters
#    PT: Se o codebook mudar, é aqui (e só aqui) que a regra muda.
#    EN: If the codebook changes, this is the one place the rule changes.
# -----------------------------------------------------------------------------
colunas_esperadas <- c(
  "id_discurso", "posicao_educacao", "confianca",
  "trecho_evidencia", "codificador", "data_codificacao"
)
codigos_validos   <- c("favoravel", "contrario", "ambiguo", "nao_se_aplica")
confianca_valida  <- c("alta", "media", "baixa")

args             <- commandArgs(trailingOnly = TRUE)
arquivo_codigos  <- if (length(args) >= 1) args[[1]] else "dados/processados/codificacao.csv"
arquivo_brutos   <- "dados/brutos/discursos.csv"

# -----------------------------------------------------------------------------
# 2. Leitura / Reading
#    PT: Tudo como texto (col_types = "c") para não mascarar erros de formato
#        com conversões automáticas.
#    EN: Read everything as character so automatic type guessing does not hide
#        format errors.
# -----------------------------------------------------------------------------
brutos  <- read_csv(arquivo_brutos,  col_types = cols(.default = "c"))
codigos <- read_csv(arquivo_codigos, col_types = cols(.default = "c"))

problemas <- character()

# -----------------------------------------------------------------------------
# 3. Checagens / Checks
# -----------------------------------------------------------------------------

# 3.1 PT: Colunas exatamente como no codebook, na mesma ordem.
#     EN: Columns exactly as in the codebook, same order.
if (!identical(names(codigos), colunas_esperadas)) {
  problemas <- c(problemas, str_glue(
    "Colunas diferentes do codebook. Esperado: {str_c(colunas_esperadas, collapse = ', ')}. ",
    "Encontrado: {str_c(names(codigos), collapse = ', ')}."
  ))
  # PT: Sem as colunas certas, as demais checagens não fazem sentido.
  # EN: Without the right columns the remaining checks are meaningless.
  message(str_c("- ", problemas, collapse = "\n"))
  quit(status = 1)
}

# 3.2 PT: Cada discurso bruto codificado exatamente uma vez (nem falta, nem sobra).
#     EN: Every raw speech coded exactly once (no missing, no extra, no duplicates).
faltando   <- setdiff(brutos$id_discurso, codigos$id_discurso)
sobrando   <- setdiff(codigos$id_discurso, brutos$id_discurso)
duplicados <- codigos |> count(id_discurso) |> filter(n > 1) |> pull(id_discurso)

if (length(faltando))   problemas <- c(problemas, str_glue("Discursos sem codificação: {str_c(faltando, collapse = ', ')}."))
if (length(sobrando))   problemas <- c(problemas, str_glue("IDs que não existem nos dados brutos: {str_c(sobrando, collapse = ', ')}."))
if (length(duplicados)) problemas <- c(problemas, str_glue("IDs codificados mais de uma vez: {str_c(duplicados, collapse = ', ')}."))

# 3.3 PT: Valores dentro das categorias do codebook.
#     EN: Values restricted to codebook categories.
codigo_invalido <- codigos |> filter(!posicao_educacao %in% codigos_validos)
if (nrow(codigo_invalido)) {
  problemas <- c(problemas, str_glue(
    "Código inválido em posicao_educacao ({codigo_invalido$id_discurso}): '{codigo_invalido$posicao_educacao}'."
  ))
}

conf_invalida <- codigos |> filter(!confianca %in% confianca_valida)
if (nrow(conf_invalida)) {
  problemas <- c(problemas, str_glue(
    "Valor inválido em confianca ({conf_invalida$id_discurso}): '{conf_invalida$confianca}'."
  ))
}

# 3.4 PT: Evidência literal — o trecho citado precisa existir, caractere por
#         caractere, no discurso original. É uma defesa simples e eficaz contra
#         citações inventadas (alucinação).
#     EN: Verbatim evidence — the quoted excerpt must exist, character by
#         character, in the original speech. A simple, effective guard against
#         fabricated quotes (hallucination).
evidencia_inexistente <- codigos |>
  inner_join(brutos |> select(id_discurso, texto), by = "id_discurso") |>
  # PT: um trecho vazio "existiria" em qualquer discurso; por isso é recusado.
  # EN: an empty excerpt would "occur" in any speech, so it is rejected.
  filter(is.na(trecho_evidencia) | str_trim(trecho_evidencia) == "" |
           !str_detect(texto, fixed(trecho_evidencia)))

if (nrow(evidencia_inexistente)) {
  problemas <- c(problemas, str_glue(
    "trecho_evidencia não é citação literal do discurso {evidencia_inexistente$id_discurso}."
  ))
}

# 3.5 PT: Rastreabilidade — quem codificou e quando.
#     EN: Traceability — who coded and when.
sem_registro <- codigos |>
  filter(is.na(codificador) | codificador == "" |
           !str_detect(coalesce(data_codificacao, ""), "^\\d{4}-\\d{2}-\\d{2}$"))
if (nrow(sem_registro)) {
  problemas <- c(problemas, str_glue(
    "codificador ausente ou data_codificacao fora do formato AAAA-MM-DD em {sem_registro$id_discurso}."
  ))
}

# -----------------------------------------------------------------------------
# 4. Resultado / Result
# -----------------------------------------------------------------------------
if (length(problemas)) {
  message("Codificação INVÁLIDA / INVALID coding (", arquivo_codigos, "):")
  message(str_c("- ", problemas, collapse = "\n"))
  quit(status = 1)
}

message(str_glue("Codificação válida: {nrow(codigos)} discursos, todas as checagens passaram."))
