# Demonstração da Sessão 1: fichamento com OpenAlex

Roteiro do instrutor para a demonstração de ponta a ponta (20 min). A tarefa vai da pergunta à conferência humana, com um único pedido em linguagem natural.

## Fronteira com a Sessão 2

Aqui não entram *skills*, *hooks*, `AGENTS.md`, subagentes, modo de plano como lição, Git ou o corpus de discursos. A fala de saída é: como isso vira um protocolo repetível é a aula do Tales.

A síntese pedida é material de leitura para quem pesquisa. O texto do artigo continua sendo seu, em linha com o slide "O que não delegar".

## Preparação

1. Crie uma pasta vazia fora deste repositório e abra no VS Code.
2. Rode o agente com configuração limpa, para que suas *skills* pessoais não disparem:

   ```bash
   CLAUDE_CONFIG_DIR="$HOME/.claude-demo" claude
   ```

   Faça login uma vez antes da aula e confira que a lista de *skills* está vazia. Se usar a extensão do VS Code, defina a mesma variável no ambiente em que o editor foi aberto.
3. Deixe o modo em Accept edits, para a demo não parar a cada arquivo. Comandos ainda pedem aprovação, e isso prepara o bloco "Quem decide?".
4. Deixe abertas a pasta [backup/](backup/) e a página do OpenAlex.

## O pedido

> Mapeie a literatura brasileira recente sobre Fundeb e desigualdade. Use a API do OpenAlex, selecione os 12 trabalhos mais pertinentes, faça uma ficha de cada um (pergunta, método, achado, limitação), gere um `.bib` e uma síntese de uma página, e me diga o que ficou de fora e por quê.

## Tempos

| Etapa | Min | O que fazer |
|---|---|---|
| Apresentar a pergunta e o percurso | 2 | Slide "Da pergunta à ficha" |
| Disparar e narrar | 6 | Comentar a busca, os erros e as correções, e as aprovações |
| Mostrar as entregas | 3 | Abrir uma ficha, a síntese e o `.bib` |
| Conferir | 7 | Slide "O que conferir" |
| Fechar | 2 | Slide do funil e fala de saída |

## O que conferir ao vivo

1. **Fácil.** Abra um DOI da lista. Ele existe e leva ao trabalho certo?
2. **Difícil.** Abra uma ficha ao lado do resumo original no OpenAlex. O achado está no resumo? O agente acrescentou algo? O resumo chega como `abstract_inverted_index`, e um registro sem resumo é o melhor lugar para procurar invenção.
3. **Mais difícil.** Peça a mesma busca com outro termo ou ordenada por citações e compare as listas. A resposta a "o que ficou de fora" depende da coleta.

## Contingência

Se o agente travar por 2 min ou a rede cair, pare e abra [backup/](backup/), que traz uma execução real completa, e siga para a conferência. O agente pode errar ao vivo: isso serve à aula, desde que você mostre o erro e como o encontrou.
