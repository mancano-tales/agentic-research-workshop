# Livro de Códigos — Posição sobre Expansão do Gasto em Educação

Livro de códigos didático para o projeto de demonstração. Os discursos em `dados/brutos/discursos.csv` são **fictícios**, criados para fins de ensino.

## Unidade de análise

Um discurso (uma linha de `dados/brutos/discursos.csv`).

## Variável `posicao_educacao`

Posição do orador sobre a **expansão do gasto público ou da oferta pública em educação** (vagas, repasses, programas, bolsas, infraestrutura).

| Código | Definição | Regra de decisão |
|---|---|---|
| `favoravel` | O orador defende ampliar gasto, oferta ou programas educacionais. | Há defesa explícita de mais recursos, vagas ou programas. |
| `contrario` | O orador se opõe a ampliar gasto, oferta ou programas educacionais. | Há oposição explícita, ainda que condicionada a outra medida. |
| `ambiguo` | O orador expressa apoio e ressalvas de peso comparável. | Apoio condicionado a quem paga, ou argumentos dos dois lados sem conclusão clara. |
| `nao_se_aplica` | O discurso não trata de educação. | Homenagens, questões de ordem, outros temas. |

## Variável `confianca`

Grau de confiança do codificador na atribuição: `alta`, `media` ou `baixa`. Discursos com confiança `baixa` devem obrigatoriamente entrar na amostra de validação humana.

## Variável `trecho_evidencia`

Trecho **copiado literalmente** do texto do discurso que justifica o código. Para `nao_se_aplica`, copiar a primeira frase do discurso. Paráfrases não são aceitas — a validação automática confere se o trecho existe, caractere por caractere, no texto original.

## Formato de saída

Arquivo `dados/processados/codificacao.csv`, com exatamente estas colunas, nesta ordem:

`id_discurso, posicao_educacao, confianca, trecho_evidencia, codificador, data_codificacao`

- `codificador`: identificação de quem codificou (ex.: nome e versão do modelo, ou iniciais do pesquisador).
- `data_codificacao`: data no formato `AAAA-MM-DD`.
