#!/usr/bin/env python3
"""Baixa do OpenAlex, via curl e com paginação por número de página, as consultas do mapeamento.
(cursor= exige chave de API desde que testei; page= não exige, e os totais cabem nele.)
Grava o JSON bruto de cada página em dados/ e não envia mailto nem dado pessoal."""
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CAMPOS = ("id,doi,display_name,publication_year,publication_date,type,language,"
          "authorships,primary_location,best_oa_location,open_access,cited_by_count,"
          "biblio,abstract_inverted_index,has_fulltext")
CONSULTAS = {
    "q1_principal": "title_and_abstract.search:Fundeb AND (desigualdade OR desigualdades OR inequality OR inequalities OR equidade OR equity),from_publication_date:2018-01-01",
    "q2_complementar": "title_and_abstract.search:Fundeb AND (redistribuição OR redistributivo OR redistribution OR redistributive OR VAAT OR VAAR OR disparidades OR disparities OR iniquidade),from_publication_date:2018-01-01",
}


def pagina(filtro, n):
    cmd = ["curl", "-sS", "--fail-with-body", "-G", "https://api.openalex.org/works",
           "--data-urlencode", f"filter={filtro}",
           "--data-urlencode", "per-page=100",
           "--data-urlencode", f"page={n}",
           "--data-urlencode", f"select={CAMPOS}"]
    return json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True).stdout)


for nome, filtro in CONSULTAS.items():
    n, total, obtidos = 0, None, 0
    while True:
        dados = pagina(filtro, n + 1)
        if not dados["results"]:
            break
        n += 1
        total = dados["meta"]["count"]
        obtidos += len(dados["results"])
        (AQUI / f"{nome}_p{n}.json").write_text(json.dumps(dados, ensure_ascii=False), encoding="utf-8")
        if obtidos >= total:
            break
    print(nome, "total:", total, "obtidos:", obtidos, "páginas:", n, file=sys.stderr)
