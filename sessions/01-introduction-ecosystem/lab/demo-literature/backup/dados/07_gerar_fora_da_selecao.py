#!/usr/bin/env python3
"""Gera fora_da_selecao.md a partir de dados/triagem.tsv e dados/triagem_meta.json."""
import csv
import json
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
meta = json.loads((AQUI / "triagem_meta.json").read_text(encoding="utf-8"))
COD, ct = meta["COD"], meta["ct"]
linhas = list(csv.DictReader(open(AQUI / "triagem.tsv", encoding="utf-8"), delimiter="\t"))
por = defaultdict(list)
for l in linhas:
    por[l["decisao"]].append(l)
excl = len(linhas) - ct["SELECIONADO"]
ORDEM = ["T", "O", "P", "R", "L", "S", "D", "N", "E"]
md = ["# O que ficou de fora e por quê\n",
f"Dos 241 candidatos examinados, 12 entraram na seleção e {excl} ficaram de fora. A tabela traz o critério que excluiu cada grupo; cada trabalho recebeu um único motivo, o primeiro que se aplicou.\n",
"| Critério de exclusão | Trabalhos |", "|---|---:|"]
for c in ORDEM:
    md.append(f"| {COD[c]} | {ct[c]} |")
md.append(f"| **Total** | **{excl}** |\n")
md += ["## Busca e funil\n",
"- **Fonte:** API pública do OpenAlex (`/works`), via `curl`, em 2026-11-09. Só título e resumo (`title_and_abstract.search`), a partir de 2018-01-01. O recorte temporal inclui o período anterior à EC 108/2020 para permitir comparação.",
"- **Consulta principal:** `title_and_abstract.search:Fundeb AND (desigualdade OR desigualdades OR inequality OR inequalities OR equidade OR equity),from_publication_date:2018-01-01`. Total: 185 trabalhos.",
"- **Consulta complementar:** `title_and_abstract.search:Fundeb AND (redistribuição OR redistributivo OR redistribution OR redistributive OR VAAT OR VAAR OR disparidades OR disparities OR iniquidade),from_publication_date:2018-01-01`. Total: 127 trabalhos, dos quais 71 já estavam na principal e 56 eram novos.",
"- **Funil:** 241 registros únicos, identificados pelo ID do OpenAlex; 236 com resumo não vazio (180 dos 185 da consulta principal); 60 na lista curta, dos quais 57 com resumo disponível e lidos na íntegra; 12 selecionados, todos com PDF aberto.",
"- **Paginação:** a API recusou `cursor=` sem chave de API (HTTP 401). Usei `page=`, que dispensa chave e alcança os totais. Não criei chave nem enviei dado pessoal.\n",
"## Limites desta triagem\n",
"- Os 181 candidatos fora da lista curta foram avaliados por título, início do resumo e frase sobre desigualdade, não pelo resumo inteiro. Alguns motivos podem mudar numa leitura completa.",
"- A seleção é um julgamento de um único leitor, sem segundo codificador.",
"- A preferência dos 12 foi por objeto direto (Fundeb e desigualdade), dados próprios identificáveis, cobertura de eixos distintos (nacional, interestadual, intraestadual, novo Fundeb, VAAR e raça) e texto completo aberto.",
"- A busca depende do OpenAlex e da sigla \"Fundeb\" no título ou resumo. Trabalhos sem a sigla, ou que o OpenAlex não indexa, não aparecem; nada foi buscado diretamente em SciELO, BDTD ou CAPES.",
"- Três registros com `abstract_inverted_index` não trazem resumo de fato (agradecimentos ou nome de orientadora) e foram contados no critério \"sem resumo utilizável\".",
"- Teses e dissertações sem PDF aberto indicado pelo OpenAlex foram preteridas; podem ter texto completo em repositórios institucionais. A de maior interesse é W7120764834 (USP), que declara usar um modelo causal.\n",
f"## Pertinentes, mas preteridos ({ct['P']})\n"]
for l in por["P"]:
    md.append(f"- {l['titulo']} ({l['ano']}, {l['id']}): {l['motivo']}.")
for c in ORDEM:
    if c == "P":
        continue
    md.append(f"\n## {COD[c]} ({ct[c]})\n")
    for l in por[c]:
        md.append(f"- {l['titulo']} ({l['ano']}, {l['id']})")
(AQUI.parent / "fora_da_selecao.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print("ok", excl)
