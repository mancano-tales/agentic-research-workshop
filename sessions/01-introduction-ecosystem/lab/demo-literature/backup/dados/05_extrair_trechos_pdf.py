import re,sys,pathlib
base=pathlib.Path('pdfs')
keys=sys.argv[1:]
H=re.compile(r'^\s*(\d+(\.\d+)*\.?\s+)?(metodolog|m[ée]todo|procedimentos? metod|dados e|base de dados|dados\b|estrat[ée]gia emp|simula|considera[çc][õo]es finais|conclus|resultados)',re.I)
REF=re.compile(r'^\s*(refer[êe]ncias|references)\b',re.I)
LIM=re.compile(r'limita[çc]|ressalva|cautela|n[ãa]o foi poss[íi]vel|n[ãa]o permite|agenda de pesquisa|pesquisas futuras|estudos futuros',re.I)
for k in keys:
    t=(base/k/f'{k}.txt').read_text(errors='replace').splitlines()
    t=[re.sub(r'\s+',' ',l).strip() for l in t]
    end=next((i for i in range(len(t)-1,0,-1) if REF.match(t[i])),len(t))
    print('\n=========',k,'linhas',len(t),'refs em',end)
    heads=[(i,t[i]) for i in range(end) if H.match(t[i]) and len(t[i])<90]
    print('HEADS',[(i,h[:50]) for i,h in heads][:25])
    # conclusão: tudo desde o último head de conclusão/considerações até refs
    conc=[i for i,h in heads if re.search(r'considera|conclus',h,re.I)]
    c0=conc[-1] if conc else max(0,end-120)
    print('--- CONCLUSAO'); print(' '.join(x for x in t[c0:end] if x)[:7000])
    print('--- LIMITES')
    for i in range(end):
        if LIM.search(t[i]): print(i,' '.join(t[max(0,i-1):i+2])[:320])
