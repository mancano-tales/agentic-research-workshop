#!/usr/bin/env python3
"""Consolida as páginas brutas, deduplica por ID do OpenAlex, reconstrói os resumos
a partir de abstract_inverted_index e grava candidatos.json e candidatos.tsv."""
import csv
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def resumo(ii):
    if not ii:
        return ""
    pos = {i: p for p, l in ii.items() for i in l}
    return " ".join(pos[i] for i in sorted(pos))


vistos = {}
for q in ("q1_principal", "q2_complementar"):
    n = 0
    for f in sorted(AQUI.glob(f"{q}_p*.json")):
        for w in json.loads(f.read_text(encoding="utf-8"))["results"]:
            n += 1
            if w["id"] in vistos:
                vistos[w["id"]]["consultas"].append(q)
                continue
            vistos[w["id"]] = {
                "id": w["id"].rsplit("/", 1)[-1], "doi": w.get("doi"),
                "titulo": w["display_name"], "ano": w["publication_year"],
                "data": w.get("publication_date"), "tipo": w["type"], "idioma": w.get("language"),
                "autores": [a["author"]["display_name"] for a in w.get("authorships", [])],
                "paises": sorted({c for a in w.get("authorships", []) for c in (a.get("countries") or [])}),
                "fonte": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
                "url": (w.get("primary_location") or {}).get("landing_page_url"),
                "pdf": (w.get("best_oa_location") or {}).get("pdf_url"),
                "citacoes": w.get("cited_by_count"), "biblio": w.get("biblio"),
                "resumo": resumo(w.get("abstract_inverted_index")), "consultas": [q],
            }
    print(q, "registros:", n)
c = sorted(vistos.values(), key=lambda x: x["id"])
(AQUI / "candidatos.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
with open(AQUI / "candidatos.tsv", "w", newline="", encoding="utf-8") as f:
    o = csv.writer(f, delimiter="\t")
    o.writerow("id ano tipo idioma citacoes consultas tem_resumo n_palavras fonte titulo".split())
    for x in c:
        o.writerow([x["id"], x["ano"], x["tipo"], x["idioma"], x["citacoes"], "+".join(x["consultas"]),
                    bool(x["resumo"]), len(x["resumo"].split()), x["fonte"], x["titulo"]])
print("únicos:", len(c), "com resumo:", sum(bool(x["resumo"]) for x in c))
