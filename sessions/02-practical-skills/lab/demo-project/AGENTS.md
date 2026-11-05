# AGENTS.md — Projeto de demonstração: discursos e gasto em educação

Instruções para agentes de IA que operam neste projeto. Leia antes de qualquer ação.

## O projeto

Codificação da posição de parlamentares sobre expansão do gasto em educação, a partir de discursos (fictícios, para fins didáticos). A variável produzida será usada em análise estatística posterior; por isso, formato, rastreabilidade e validação importam mais do que velocidade.

## Estrutura

- `dados/brutos/` — dados originais. **Somente leitura.** (Protegido também por hook.)
- `dados/processados/` — tudo o que for gerado.
- `codebook.md` — livro de códigos. É a autoridade sobre categorias e formato.
- `R/` — scripts de análise e validação, em R, estilo tidyverse.
- `logs/` — registro automático das ações do agente. Não editar.

## Como trabalhar

- Para codificar os discursos, use a skill `codificar-discursos`.
- Para revisar a codificação, use o subagente `auditor`, com contexto limpo. Não se autoavalie.
- Antes de dar uma tarefa como concluída, rode `Rscript R/validar_codificacao.R` e mostre a saída.
- Scripts novos em R: pipe nativo `|>`, `readr`/`dplyr`/`stringr`, comentários explicativos em português e inglês.
- Se algo no livro de códigos estiver ambíguo, pergunte ao pesquisador em vez de decidir sozinho.

## O que nunca fazer

- Modificar, mover ou apagar arquivos em `dados/brutos/`.
- Alterar `codebook.md` sem pedido explícito do pesquisador.
- Inventar citações: `trecho_evidencia` é sempre cópia literal.
- Ler ou exibir arquivos de credenciais (`.env`, chaves).
