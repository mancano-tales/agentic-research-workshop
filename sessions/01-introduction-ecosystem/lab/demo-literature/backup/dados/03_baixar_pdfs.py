#!/usr/bin/env python3
"""Tenta baixar, com curl, o PDF aberto indicado pelo OpenAlex para cada trabalho selecionado
e extrai o texto com pdftotext. Cada PDF fica em sua própria subpasta de dados/pdfs/."""
import json
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
cand = {x["id"]: x for x in json.loads((AQUI / "candidatos.json").read_text(encoding="utf-8"))}
for linha in (AQUI / "selecionados.tsv").read_text(encoding="utf-8").splitlines():
    chave, wid = linha.split("\t")
    url = cand[wid]["pdf"]
    pasta = AQUI / "pdfs" / chave
    pasta.mkdir(parents=True, exist_ok=True)
    pdf = pasta / f"{chave}.pdf"
    if not url:
        print(chave, "sem URL de PDF no OpenAlex")
        continue
    r = subprocess.run(["curl", "-sSL", "--max-time", "90", "-A", "Mozilla/5.0", "-o", str(pdf), "-w", "%{http_code} %{content_type}", url],
                       capture_output=True, text=True)
    ok = pdf.exists() and pdf.read_bytes()[:5] == b"%PDF-"
    pags = ""
    if ok:
        subprocess.run(["pdftotext", "-layout", str(pdf), str(pasta / f"{chave}.txt")], check=False)
        pags = len((pasta / f"{chave}.txt").read_text(encoding="utf-8", errors="replace").split())
    print(chave, r.stdout, r.stderr.strip()[:100], "PDF" if ok else "NAO-PDF", pags, url)
