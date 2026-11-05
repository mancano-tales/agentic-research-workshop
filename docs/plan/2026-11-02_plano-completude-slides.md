# Plano de completude dos slides (2026-11-02)

Issue: #3. Objetivo: deixar `aulas/agentes-ia-pesquisa.qmd` pronto (web e PDF Beamer) até sexta, 2026-11-06. A aula é na semana seguinte; o que só pode ser feito na véspera (preços, ensaio das demos) fica separado no fim.

## Onde estamos

- Fonte única das duas sessões, com tema `madrid-web`, site publicado pelo CI (PR #6 e `d7e4cf5`). PDF Beamer em `assets/` gerado em 2026-10-18.
- Sessão 1 completa nos cinco blocos. Sessão 2 completa nos cinco blocos, mais o aprofundamento.
- Mudança local ainda não commitada: dois slides sobre Barrie, Palmer e Spirling (2025), a variância na rubrica de avaliação e a retirada do slide de tese da abertura. O autor decidiu mantê-la.
- Não há registro de que a reunião de 2026-10-08 tenha validado as nove decisões do [plano de preparação](2026-10-06_plano-preparacao-aulas.md). Por isso, as demonstrações novas abaixo têm uma versão sem demo ao vivo.

## O que falta

### A. Conteúdo factual

1. **Barrie, Palmer e Spirling**: conferir na versão publicada (*AJPS*) os números do slide "Oito meses rodando a mesma tarefa" (a nota diz que seguem a versão de dezembro de 2024).
2. **Modelos e preços** ("Famílias de modelos", "Alternativas de pesos abertos", "Quanto custa?", "Custo de uma tarefa em lote"): atualizar para novembro, incluindo a versão do Haiku (a possível aposentadoria do 4.5 era a partir de 15/10), e trocar o carimbo `out/2026`.
3. **Custos em reais** (decisão 6): converter a tabela de custo em lote com câmbio datado e compará-la com o valor vigente da bolsa CAPES de mestrado, conferido na fonte.
4. **Links**: trocar o nome antigo do repositório (`2026-workshop-agentes-dcp-usp`) por `course-llm-agents-for-research` nos slides "Exemplo vivo" e "Uma revisão encontrou a brecha".

### B. Slides que dependem de demonstração

5. **Injeção inofensiva** (decisão 4): o slide hoje só tem a frase do PDF. Duas versões possíveis:
   - *com demo*: pasta descartável, PDF com texto em branco e um hook `PreToolUse` que bloqueia apagar resultados (o projeto de demonstração atual não bloqueia; só acusa depois);
   - *sem demo*: um slide com a sequência (sem regra, o agente apaga; com a regra, a ação é barrada), descrita a partir de um ensaio gravado ou de um relato documentado.
6. **Mesma tarefa no Codex** (decisão 5): ao menos um slide com o `AGENTS.md` como contrato portável entre harnesses. Demo ao vivo só se os três concordarem.

### C. Pontos de forma

7. **Tese**: com a saída do slide de abertura, conferir se "prosa orienta, regra garante" e "a verificação é o gargalo" aparecem com clareza nos slides "Para levar" das duas sessões.
8. **Tempo**: contar slides por bloco contra o cronograma de 90 minutos por sessão e marcar como aprofundamento o que não couber.

### D. Revisão e publicação

9. Revisão visual da versão web em 1280×720 e do PDF Beamer (tabelas cortadas, `.smaller` excessivo, notas vazias).
10. Revisão de texto (gramática, consistência de termos: *harness*, *skill*, *hook*).
11. PR com `@codex review`, tratamento dos achados, merge.
12. Render do PDF Beamer (`tools/render-slides.ps1`), commit em `assets/` e conferência do site publicado.

## Cronograma

| Dia | O quê |
|---|---|
| seg 02/11 | Plano; commit da mudança local numa branch de trabalho; mensagem aos coministrantes com as decisões pendentes (abaixo) |
| ter 03/11 | Itens 1 a 4 (conteúdo factual) |
| qua 04/11 | Itens 5 e 6 na versão que os coministrantes escolherem (sem resposta até quarta: versão sem demo); itens 7 e 8 |
| qui 05/11 | Itens 9 e 10; abrir o PR e pedir `@codex review`; enviar o link do site aos coministrantes |
| sex 06/11 | Incorporar achados e comentários; item 12; merge. Slides congelados, salvo números da véspera |

## Decisões pendentes (dos três ministrantes, até quarta 04/11)

1. Data, horário e local da aula; internet na sala.
2. Divisão de blocos e quem opera o terminal.
3. Agente e conta usados ao vivo.
4. Demos de injeção e no Codex: ao vivo, gravadas ou só em slide.

## Semana da aula (fora do prazo desta semana)

- Reconferir modelos, preços e câmbio na véspera; reemitir o PDF se algo mudar.
- Ensaio completo das demos numa máquina limpa (R e `jsonlite` instalados; WSL2 se for Windows), chave de API com limite baixo.
- Gravar o *backup* das demos.
- Folha de saída (`aulas/02-habilidades-praticas/folha-de-saida.md`) revisada e linkada no site.
