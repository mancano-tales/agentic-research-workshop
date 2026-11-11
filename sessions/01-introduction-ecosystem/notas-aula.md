# Sessão 1: Introdução aos Agentes de IA

Roteiro do instrutor para a primeira sessão (1h30). Acompanha o deck [llm-agents-for-research-session-1-slides.qmd](llm-agents-for-research-session-1-slides.qmd), cujas notas trazem o detalhe de cada slide. Os temas seguem a Seção 4 da [ementa](../../llm-agents-for-research-syllabus.qmd). A demonstração e a seção sobre delegar e verificar são acréscimos ligados à tese do curso.

Visão de conjunto: [docs/plan/plano-geral.md](../../docs/plan/plano-geral.md). Referências: [referencias.md](../../referencias.md).

**Distribuição de tempo (90 min):**

| Seção | Duração | Conteúdo |
|---|---|---|
| Abertura | 5 min | Plano geral, enquete, tese |
| 1. LLMs como agentes | 8 min | Do chat ao loop; o modelo pede, o *harness* executa |
| 2. Modelos e formas de usar | 12 min | Famílias; três janelas; tour de 3 min |
| 3. Delegar e verificar | 20 min | O que mudou desde 2025; custo; matriz de perigo; o que não delegar; quem responde |
| 4. Demonstração | 22 min | Fichamento com OpenAlex, da pergunta à conferência |
| 5. Limites: *harness* e regra | 12 min | Modos; o caso do e-mail; prosa e regra |
| Encerramento | 3 min | Para levar e ponte para a Sessão 2 |
| Reserva | 8 min | Atrasos da demonstração ou perguntas |

---

## Abertura (5 min)

**Enquete.** Mostre o QR no slide "Antes de começar" e dê um minuto enquanto se apresenta. Depois, abra `survey/results/` no projetor e compare com os números de Lyttelton, Massenkoff e Wilmers (2026), que têm amostra não representativa.

Antes da aula: confirme que o backend responde, rode `limpar()` e `abrir()` em [tools/survey-backend.gs](../../tools/survey-backend.gs) e deixe a aba de resultados aberta. Depois da aula, rode `encerrar()`.

**Plano B:** o slide "As perguntas" traz as quatro perguntas e as opções, para mão levantada.

Encerre com a tese: o gargalo deixou de ser a execução e passou a ser a verificação. O tom da aula não é de dúvida: os agentes já são muito bons em muitas tarefas, e a pergunta passou a ser como usar bem.

## 1. LLMs como agentes (8 min)

A mudança é de arquitetura, do chat supervisionado ao loop com autonomia delimitada. O *harness* tem a ver com as ferramentas disponíveis para o modelo: o chat também é um *harness*, que até faz buscas, mas é muito limitado. Defina janela de contexto no slide da anatomia, porque a abertura da Sessão 2 supõe esse conceito.

## 2. Modelos e formas de usar (12 min)

Situe os nomes em duas camadas, modelo e *harness*, e mostre que o mesmo agente aparece em janelas diferentes. Nomes e preços mudam em semanas: confira na véspera.

**Tour (3 min).** Prepare antes da aula uma cópia de [lab/tour-interfaces/partidos.csv](lab/tour-interfaces/partidos.csv) em pasta própria, com Git e sem conectores. Use perfil limpo, porque a barra lateral do app mostra projetos reais. Force o modo Manual, já que o Auto é o modo inicial em terminal e VS Code. Deixe as sessões prontas, paradas na aprovação.

| Janela | Modo | Passo |
|---|---|---|
| Terminal | Plan | Pedir a contagem das grafias da coluna `partido` e mostrar a proposta |
| VS Code | Manual | Pedir o arquivo limpo; aceitar um trecho e rejeitar o que junta PMDB e MDB |
| App | Manual | Abrir o *diff* e comentar uma linha |

Tratar PMDB e MDB como a mesma legenda é decisão de pesquisa, e o agente não deveria tomá-la sozinho. Com 20 segundos sem resposta, passe à janela seguinte.

## 3. Delegar e verificar (20 min)

Em "O que mudou desde 2025", a mensagem é que a dúvida ficou para trás: em 2025 o ganho parecia mais percepção do que realidade, e hoje parece muito real, ainda sem evidência sistemática. O quadro "Hoje" é avaliação dos ministrantes, e vale dizer isso em voz alta.

Em "Quanto custa?", o slide mostra os planos do Claude e do ChatGPT, que inclui o Codex. A conta via API e os preços por modelo estão nas notas do slide. Lembre que o tempo de validação humana domina o custo total.

A matriz de perigo é o centro da seção. "Difícil" significa exigir conhecimento especializado. Dar trabalho é outra coisa: codificar 2.000 discursos dá muito trabalho, mas cada discurso, isolado, é simples. As notas do slide trazem o que dizer sobre a Armadilha (erro correlacionado e validação cega).

Em "O que não delegar", o critério é o que você sabe sobre o que está delegando: a escrita e o que você ainda deveria aprender ficam com você; o que está consolidado pode ser delegado.

## 4. Demonstração (22 min)

Roteiro completo, pedido e contingência em [lab/demo-literature/README.md](lab/demo-literature/README.md).

A demonstração não usa *skills*, *hooks*, `AGENTS.md`, subagentes, Git nem o corpus de discursos. Rode com configuração limpa, porque suas *skills* pessoais de fichamento disparariam com esse pedido. A fala de saída é: como isso vira um protocolo repetível é a aula do Tales.

## 5. Limites: *harness* e regra (12 min)

As aprovações que apareceram na demonstração abrem "Quem decide?". A linha "Na prática" do esquema traz um alerta por modo; para tarefa nova ou grande, recomende começar pelo modo de planejamento. Diga em uma frase que autonomia total só cabe em ambiente isolado (contêiner ou máquina virtual), já que não há mais slide sobre isolamento.

Em "Um caso real: o e-mail", conte o caso do Galdino: ele usava o modo automático, e o agente enviou um e-mail sem autorização. As notas do slide trazem a tríade letal de Simon Willison em uma frase, porque a Sessão 2 retoma esse conceito.

A distinção entre prosa e regra é a base de *hooks* e *code as policy*, que ficam para a Sessão 2.

## Encerramento (3 min)

Retome a pergunta da matriz ("como eu saberia que está errado?") e deixe a pergunta da Sessão 2: o que precisa estar no projeto antes de o agente começar?

Leitura entre as sessões: Korinek (2025), *AI Agents for Economic Research*, introdução; e um texto da série de Cunningham.
