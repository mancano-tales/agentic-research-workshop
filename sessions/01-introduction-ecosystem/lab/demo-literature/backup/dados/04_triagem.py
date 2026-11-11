#!/usr/bin/env python3
"""Registra a triagem manual dos candidatos (código de exclusão por ID), confere se todo
candidato recebeu exatamente uma decisão e grava dados/triagem.tsv.
Os códigos foram atribuídos por leitura; o script só registra e confere."""
import csv
import json
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
COD = {
 "S": "Sem resumo utilizável (sem abstract no OpenAlex ou texto que não é resumo)",
 "D": "Registro duplicado (versão, tradução, dataset ou depósito de trabalho já listado)",
 "N": "Não é pesquisa original (índice, editorial, apresentação de dossiê, resenha)",
 "E": "Fora do recorte Brasil",
 "T": "Fundeb tangencial: citado, mas o objeto é outro (ICMS Educacional, Salário-Educação, FPM, gestão, política educacional em geral)",
 "O": "Fundeb central, mas a desigualdade não é o objeto (valorização docente, escolha de diretores, condicionalidades, etapa específica, disputa política)",
 "L": "Estudo de um único município ou de recorte local, sem comparação entre entes",
 "R": "Revisão, ensaio ou análise normativa sem dados próprios sobre desigualdade",
 "P": "Pertinente ao tema, mas preterido na comparação com os 12 selecionados (motivo individual)",
}
T = {
"S":"W4415122364 W7120276700 W7171959659 W4205386499 W3110544612 W3046158089 W7120829475 W7197398669",
"D":"W7125472110 W7125610558 W4393072619 W4394404145 W7119251394 W4312364861 W4394407561",
"N":"W4319780543 W3109968057 W4413124173 W7113904120 W4225568608 W3202550330",
"E":"W2890071566",
"T":"""W7140105106 W7147147531 W7162167438 W7162198600 W7162454027 W7162762515 W7170199906 W7201928808 W7213416800 W7215355024 W7216702350 W7221133052 W7222794329 W7223238549
W4410982981 W4412982822 W4413015571 W4413784474 W4413926713 W4414651887 W4415642295 W4416186246 W4416225945 W4417200879 W4417516410 W7105144514 W7117450816 W7124312045 W7203801042 W7215547231
W4400652748 W4401679719 W4403935078 W4404716917 W7215601972 W4328128683 W4380849158 W4387882432 W4390938668 W7120646912 W4226143962 W4312789578 W3188138117 W3202542279 W4386940143 W7120731795
W3011319746 W3022837137 W3027740100 W3030147263 W3109867188 W3110674847 W7120399850 W7120745024 W7214742744 W2732268556 W2947708273 W3034674256 W4413040981 W7120505026 W4412024657 W4415292407 W2978721604""",
"O":"""W7125613596 W7160143710 W7160187162 W7160829170 W7161988791 W7166292924 W7172249946 W7202041011 W7203918564 W7213461590 W7220678744 W7225317801 W4410967330 W4416751786
W7120323889 W7120876325 W7127420895 W7144334836 W7217268066 W7220156730 W4390492803 W4391876409 W4391876536 W4393103494 W4401880817 W4402411770 W4403246435 W4404373963 W4328098886 W4328129337
W4365804315 W4380563478 W4389474408 W4391956331 W7119256638 W7120672523 W7120854995 W4225985730 W4313164178 W3201968722 W3023486966 W3091333754 W2981798549 W2984298422 W3091713855 W4387857286 W4399117428""",
"L":"""W7125162926 W7164809665 W7215711426 W7222887150 W4416716796 W4402984722 W7119430878 W4318686667 W7217295351 W4280612498 W4205343846 W3168447673 W4413427542 W7220955114 W7212081534 W3154860363""",
"R":"""W7127080420 W7131659663 W7203877572 W7208722141 W7214979354 W7217860341 W4407333237 W4410761608 W4410882736 W4411269103 W4411747713 W4417136547 W7121699562 W7124564187 W7128424429 W7215205093 W7215240132
W4327711808 W4385804741 W4386136593 W4387106743 W4387463952 W4396682927 W4391666348 W7219934761 W3148105631 W3195083162 W4236470603 W4294968928 W3134610252 W7220606120 W2984187806 W2986059011 W3007072887 W3011206733
W2901183625 W4409292515 W4393189516 W7204262935""",
}
P = {
"W7160281470":"Dois municípios cearenses; a questão demográfica é mais estreita que a de desigualdade",
"W7115181222":"Parte qualitativa com dados preliminares de um território baiano; VAAR já coberto por Silva e Schlegel (2025)",
"W4220863908":"Panorama descritivo do VAAT; o resumo não traz medida de desigualdade",
"W4400652765":"Análise documental do desenho do novo Fundeb, sem medir desigualdade",
"W4389474377":"Abrangência do VAAT em 2023; mesmo autor de Silva (2023), que mede desigualdade diretamente",
"W4391436292":"Preprint; o Ideb como desfecho já está em Silva Júnior et al. (2025), com revisão por pares",
"W7214782343":"Dissertação qualitativa; o tema de capacidade estatal já está em Silva e Schlegel (2025), com dados de repasse",
"W7137902959":"Mesmos autores e mesmo objeto de Silva e Schlegel (2025); ficou uma versão",
"W4231620962":"Dez municípios baianos em um ano; recorte estadual já representado com maior cobertura",
"W3163679273":"Propostas normativas sem dados; a pauta racial ficou em Tripodi et al. (2022), que propõe medida",
"W4391758525":"Quatro municípios paulistas; escala já tratada em Nascimento e Pinto (2024)",
"W4404716897":"Análise documental da condicionalidade III do VAAR, sem medir efeito",
"W2974754194":"Relatório de propostas pré-reforma, superado pela regulamentação de 2020",
"W2991125360":"Simulação pré-reforma de proposta específica; simulações do desenho aprovado foram priorizadas",
"W4225277669":"Fatores de ponderação simulados; Senkevics et al. (2026) cobre os ponderadores atuais",
"W3020287430":"Dissertação que origina o IERRE; ficou o artigo que aplica o indicador ao novo Fundeb (Santos et al., 2022)",
"W7120360561":"Dissertação qualitativa sobre Goiás, sem medida de desigualdade no resumo",
"W7119286926":"Dissertação sobre Piauí (2008-2018); sem PDF aberto indicado no OpenAlex e recorte estadual já representado",
"W2971695435":"Minas Gerais, série 2000-2015 com foco em receitas fora do Fundeb",
"W2979566336":"Dissertação com dados de 2015, sem PDF indicado; diagnóstico já coberto por Alves e Pinto (2020)",
"W4377087909":"Mesmo autor e estado de Silva (2023); versão anterior e menos direta",
"W4328127664":"Mesmo autor e estado de Silva (2023); foco em VAAT e valorização docente",
"W2883516159":"Rio Grande do Sul, 2005-2014, anterior à reforma; achado análogo já em Encinas e Duenhas (2020)",
"W2888577150":"Simulação de ponderadores para creche e pré-escola, anterior ao novo desenho",
"W4404228161":"Dissertação do mesmo autor de Nascimento e Pinto (2024), com 12 municípios",
"W4410795389":"Roraima em 2021, comparação de dois extremos",
"W2921711393":"Minas Gerais em 2017; cenário com e sem Fundeb já tratado em âmbito nacional por Hirata et al. (2022)",
"W7221773342":"Região de Araguaína; Fundeb como moderador do Ideb, sem medir desigualdade entre redes",
"W4361861006":"Comparação de despesas estaduais; o foco é a qualidade dos dados do Siope",
"W2950815256":"Dados de 2005-2009 e DOI que indica edição de 2011, embora o OpenAlex registre 2019; não é recente",
"W4409554632":"Métricas de resultado no financiamento; o VAAR já está coberto por trabalhos com dados de repasse",
"W4413818081":"Dissertação sobre mesorregiões do Amazonas; recorte estadual já representado",
"W7164879099":"Pará; recorte estadual já representado por Silva (2023) e Encinas e Duenhas (2020)",
"W4405511654":"Comunicação em congresso, recorte de dissertação; evidência menos detalhada que os artigos selecionados",
"W4411203072":"Dissertação sobre o primeiro ano do VAAR; ficou o artigo correspondente (Silva e Schlegel, 2025)",
"W7120764834":"Tese sobre financiamento e proficiência no Saeb (2010-2019); sem PDF aberto indicado pelo OpenAlex; o desfecho de aprendizagem já está em Hirata et al. (2022) e Silva Júnior et al. (2025)",
"W3213277631":"Estudo de caso institucional do Banco Mundial; descreve o sistema de transferências",
"W4200593871":"Foco na vinculação de 50% do VAAT à educação infantil",
"W3128899856":"Dissertação sobre Fundeb e acesso à educação infantil; sem PDF aberto indicado pelo OpenAlex",
"W3031582527":"Dissertação sobre Maranhão; recorte estadual já representado",
"W3209786975":"Panorama para leitor estrangeiro; síntese, não estudo novo",
"W2815125898":"Efeitos redistributivos em artigo de 2018 sobre o regime de colaboração; recorte anterior à reforma",
}
SEL = [l.split("\t") for l in (AQUI / "selecionados.tsv").read_text(encoding="utf-8").splitlines()]
sel = {w: k for k, w in SEL}
cand = json.loads((AQUI / "candidatos.json").read_text(encoding="utf-8"))
ids = {c["id"] for c in cand}
dec = {}
for cod, txt in T.items():
    for i in txt.split():
        assert i not in dec, ("duplicado", i)
        dec[i] = cod
for i in P:
    assert i not in dec, ("duplicado", i)
    dec[i] = "P"
for i in sel:
    assert i not in dec, ("selecionado também excluído", i)
    dec[i] = "SELECIONADO"
print("sem decisão:", sorted(ids - set(dec)))
print("decisão sem candidato:", sorted(set(dec) - ids))
assert ids == set(dec)
ct = Counter(dec.values())
print(ct, sum(ct.values()))
por_id = {c["id"]: c for c in cand}
with open(AQUI / "triagem.tsv", "w", newline="", encoding="utf-8") as f:
    o = csv.writer(f, delimiter="\t")
    o.writerow(["id", "decisao", "chave_ficha", "motivo", "ano", "tipo", "titulo"])
    for c in sorted(cand, key=lambda x: (dec[x["id"]], -x["ano"], x["id"])):
        d = dec[c["id"]]
        o.writerow([c["id"], d, sel.get(c["id"], ""), P.get(c["id"], COD.get(d, "")), c["ano"], c["tipo"], c["titulo"]])
print("resumo não vazio:", sum(bool(c["resumo"]) for c in cand), "de", len(cand))
print("q1:", sum("q1_principal" in c["consultas"] for c in cand), "só q2:", sum(c["consultas"] == ["q2_complementar"] for c in cand), "em ambas:", sum(len(c["consultas"]) == 2 for c in cand))
json.dump({"COD": COD, "P": P, "ct": ct}, open(AQUI / "triagem_meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
