---
name: codificar-discursos
description: Codifica discursos parlamentares de dados/brutos/discursos.csv segundo o livro de códigos (codebook.md) e gera a amostra de validação humana. Use quando o usuário pedir para classificar, codificar ou anotar os discursos.
---

# Skill: codificar discursos segundo o livro de códigos

Esta skill empacota o protocolo de codificação do projeto. Ela é **instrução em prosa**: orienta o julgamento do agente. As regras que não podem falhar (dados brutos intocados, formato do arquivo, evidência literal) estão nos *hooks* e em `R/validar_codificacao.R`, não aqui.

## Passos

1. Leia `codebook.md` inteiro antes de codificar qualquer discurso. Não invente categorias.
2. Leia `dados/brutos/discursos.csv`. Não modifique esse arquivo em hipótese alguma.
3. Para cada discurso, decida `posicao_educacao` e `confianca` aplicando as regras de decisão do livro de códigos. Em caso de dúvida entre duas categorias, escolha a mais conservadora (`ambiguo`) e marque `confianca = baixa`.
4. Em `trecho_evidencia`, copie **literalmente** o trecho que justifica o código. Não parafraseie, não corrija a grafia, não junte frases de lugares diferentes.
5. Preencha `codificador` com o nome e a versão do modelo que você é, e `data_codificacao` com a data de hoje (AAAA-MM-DD).
6. Grave o resultado em `dados/processados/codificacao.csv`, com as colunas na ordem exata do livro de códigos.
7. Se a validação automática devolver erros, corrija o arquivo e grave de novo. Não contorne a validação.
8. Gere `dados/processados/amostra_validacao.csv` para codificação humana às cegas:
   - inclua todos os discursos com `confianca = baixa`;
   - complete com um sorteio aleatório dos demais até somar pelo menos 30% dos discursos, usando uma semente fixa (`set.seed(2026)`) e registrando a semente;
   - inclua apenas `id_discurso` e `texto`, **sem** o código atribuído pelo modelo, para não induzir o codificador humano.
9. Ao final, informe ao usuário: quantos discursos foram codificados, a distribuição por categoria, quais ficaram com confiança baixa e onde está a amostra de validação.

## O que não fazer

- Não altere o livro de códigos para "encaixar" um discurso difícil; registre a dificuldade e avise o usuário.
- Não audite o próprio trabalho como se isso fosse uma revisão independente. A auditoria é feita pelo subagente `auditor`, com contexto limpo.
