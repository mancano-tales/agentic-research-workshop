# Agentes de IA para Pesquisa — folha de saída

*Workshop Agentes, Seminário Discente DCP-USP 2026. Rascunho para a reunião dos ministrantes de 2026-10-08 (decisão 8 do plano de preparação).*

**Prosa orienta. Regra garante.** O que afeta validade, replicação, sigilo ou integridade dos dados se protege com regra, não com pedido.

## Checklist

1. Comece por uma tarefa **repetitiva, volumosa e verificável**.
2. Rode o agente numa **pasta de projeto**, nunca no computador inteiro. Autonomia ampla só em contêiner ou máquina virtual.
3. Escreva um **`AGENTS.md` curto**, com o que só você sabe sobre o projeto (modelo abaixo).
4. Transforme em ***skill*** o protocolo que você repetiria a cada assistente novo (modelo abaixo).
5. Transforme em **regra executável** — script de validação, *hook*, check no GitHub — o que não pode falhar. Uma regra só não basta: combine uma guarda (antes), um sensor (depois) e o controle de versão (para restaurar).
6. Guarde uma **amostra codificada por humanos**, às cegas, para validar qualquer variável produzida por LLM.
7. **Registre** modelo, versão, data e instrução de toda etapa automatizada.
8. **Audite com contexto limpo**: outro agente, outra linguagem, outra pessoa. Quem fez não revisa.

## Modelo de `AGENTS.md`

```markdown
# AGENTS.md — <nome do projeto>

## O projeto
<Duas linhas: pergunta de pesquisa e o que o agente vai produzir.>

## Estrutura
- `dados/brutos/` — dados originais. Somente leitura.
- `dados/processados/` — tudo o que for gerado.
- `<livro-de-codigos.md>` — autoridade sobre categorias e formato.
- `R/` (ou `python/`) — scripts de análise e validação.

## Como trabalhar
- Antes de dar uma tarefa como concluída, rode `<comando de validação>` e mostre a saída.
- Se algo estiver ambíguo, pergunte em vez de decidir sozinho.
- Registre decisões metodológicas em `<arquivo ou issue>`, com data.

## O que nunca fazer
- Modificar, mover ou apagar arquivos em `dados/brutos/`.
- Inventar citações ou referências: toda evidência é cópia literal da fonte.
- Ler ou exibir arquivos de credenciais (`.env`, chaves).
```

## Modelo de *skill* (`.claude/skills/<nome>/SKILL.md` ou equivalente)

```markdown
---
name: <nome-curto>
description: <O que a skill faz e quando usar — é só isto que o agente lê antes de decidir carregá-la.>
---

# <Nome da tarefa>

Esta skill é prosa: orienta o julgamento. As regras que não podem falhar estão em
`<script de validação>` e nos hooks do projeto.

## Passos
1. Leia `<livro de códigos ou protocolo>` inteiro antes de começar.
2. <Passo da tarefa.>
3. Grave o resultado em `dados/processados/<arquivo>`, no formato do livro de códigos.
4. Rode `<comando de validação>`; se houver erro, corrija e grave de novo.
5. Gere a amostra de validação humana: <critério>, com semente registrada, sem o código do modelo.
6. Informe: quantos itens, distribuição por categoria, casos de baixa confiança.

## O que não fazer
- Não alterar o livro de códigos para encaixar um caso difícil: registre e avise.
- Não auditar o próprio trabalho como se fosse revisão independente.
```

## Para continuar

- Projeto de demonstração do curso: `sessions/02-practical-skills/lab/demo-project/` no repositório [github.com/mancano-tales/2026-workshop-agentes-dcp-usp](https://github.com/mancano-tales/2026-workshop-agentes-dcp-usp).
- Scott Cunningham, série "Claude Code" (causalinf.substack.com) e repositório MixtapeTools (protocolo Referee 2; *hook* `protect-raw-data`).
- Chris Blattman, claudeblattman.com — para quem não programa.
- Pedro Sant'Anna, `claude-code-my-workflow` — *template* avançado para acadêmicos.
- Anthropic Academy (gratuita): *Claude Code in Action*, *Introduction to Agent Skills*, *AI Fluency*.
