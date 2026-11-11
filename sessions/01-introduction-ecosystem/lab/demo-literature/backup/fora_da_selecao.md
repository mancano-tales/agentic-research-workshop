# O que ficou de fora e por quê

Dos 241 candidatos examinados, 12 entraram na seleção e 229 ficaram de fora. A tabela traz o critério que excluiu cada grupo; cada trabalho recebeu um único motivo, o primeiro que se aplicou.

| Critério de exclusão | Trabalhos |
|---|---:|
| Fundeb tangencial: citado, mas o objeto é outro (ICMS Educacional, Salário-Educação, FPM, gestão, política educacional em geral) | 63 |
| Fundeb central, mas a desigualdade não é o objeto (valorização docente, escolha de diretores, condicionalidades, etapa específica, disputa política) | 47 |
| Pertinente ao tema, mas preterido na comparação com os 12 selecionados (motivo individual) | 42 |
| Revisão, ensaio ou análise normativa sem dados próprios sobre desigualdade | 39 |
| Estudo de um único município ou de recorte local, sem comparação entre entes | 16 |
| Sem resumo utilizável (sem abstract no OpenAlex ou texto que não é resumo) | 8 |
| Registro duplicado (versão, tradução, dataset ou depósito de trabalho já listado) | 7 |
| Não é pesquisa original (índice, editorial, apresentação de dossiê, resenha) | 6 |
| Fora do recorte Brasil | 1 |
| **Total** | **229** |

## Busca e funil

- **Fonte:** API pública do OpenAlex (`/works`), via `curl`, em 2026-11-09. Só título e resumo (`title_and_abstract.search`), a partir de 2018-01-01. O recorte temporal inclui o período anterior à EC 108/2020 para permitir comparação.
- **Consulta principal:** `title_and_abstract.search:Fundeb AND (desigualdade OR desigualdades OR inequality OR inequalities OR equidade OR equity),from_publication_date:2018-01-01`. Total: 185 trabalhos.
- **Consulta complementar:** `title_and_abstract.search:Fundeb AND (redistribuição OR redistributivo OR redistribution OR redistributive OR VAAT OR VAAR OR disparidades OR disparities OR iniquidade),from_publication_date:2018-01-01`. Total: 127 trabalhos, dos quais 71 já estavam na principal e 56 eram novos.
- **Funil:** 241 registros únicos, identificados pelo ID do OpenAlex; 236 com resumo não vazio (180 dos 185 da consulta principal); 60 na lista curta, dos quais 57 com resumo disponível e lidos na íntegra; 12 selecionados, todos com PDF aberto.
- **Paginação:** a API recusou `cursor=` sem chave de API (HTTP 401). Usei `page=`, que dispensa chave e alcança os totais. Não criei chave nem enviei dado pessoal.

## Limites desta triagem

- Os 181 candidatos fora da lista curta foram avaliados por título, início do resumo e frase sobre desigualdade, não pelo resumo inteiro. Alguns motivos podem mudar numa leitura completa.
- A seleção é um julgamento de um único leitor, sem segundo codificador.
- A preferência dos 12 foi por objeto direto (Fundeb e desigualdade), dados próprios identificáveis, cobertura de eixos distintos (nacional, interestadual, intraestadual, novo Fundeb, VAAR e raça) e texto completo aberto.
- A busca depende do OpenAlex e da sigla "Fundeb" no título ou resumo. Trabalhos sem a sigla, ou que o OpenAlex não indexa, não aparecem; nada foi buscado diretamente em SciELO, BDTD ou CAPES.
- Três registros com `abstract_inverted_index` não trazem resumo de fato (agradecimentos ou nome de orientadora) e foram contados no critério "sem resumo utilizável".
- Teses e dissertações sem PDF aberto indicado pelo OpenAlex foram preteridas; podem ter texto completo em repositórios institucionais. A de maior interesse é W7120764834 (USP), que declara usar um modelo causal.

## Pertinentes, mas preteridos (42)

- Instrumentos para estimular a equidade racial em educação: o que aprendemos com o primeiro ano da Complementação- VAAR do Novo Fundeb (2026, W7137902959): Mesmos autores e mesmo objeto de Silva e Schlegel (2025); ficou uma versão.
- Fundeb e transição demográfica: Efeitos distributivos e sustentabilidade financeira das redes municipais de educação em Caucaia e Eusébio, Ceará, Brasil (2026, W7160281470): Dois municípios cearenses; a questão demográfica é mais estreita que a de desigualdade.
- A dupla camada de exclusão no novo FUNDEB: entre a barreira técnica do VAAT e o custo político do VAAR (2026, W7214782343): Dissertação qualitativa; o tema de capacidade estatal já está em Silva e Schlegel (2025), com dados de repasse.
- Desenvolvimento Desigual e Combinado na RIIA: Uma Análise do Ideb a Partir da Moderação entre IDHM e Investimento por Aluno (2026, W7221773342): Região de Araguaína; Fundeb como moderador do Ideb, sem medir desigualdade entre redes.
- Financiamento da Educação Básica (2025, W4409554632): Métricas de resultado no financiamento; o VAAR já está coberto por trabalhos com dados de repasse.
- O Gasto Aluno-Ano no Estado de Roraima e a Diferença dos Valores Máximo e Mínimo (2025, W4410795389): Roraima em 2021, comparação de dois extremos.
- Fundo de manutenção e desenvolvimento da educação básica – FUNDEB e sua contribuição na qualidade do ensino dos municípios amazonenses (2025, W4413818081): Dissertação sobre mesorregiões do Amazonas; recorte estadual já representado.
- O Novo Fundeb e a Redução das Desigualdades Educacionais: uma análise a partir da complementação VAAR (2025, W7115181222): Parte qualitativa com dados preliminares de um território baiano; VAAR já coberto por Silva e Schlegel (2025).
- O Novo Fundeb permanente e seus efeitos nas redes de ensino do Pará (2025, W7164879099): Pará; recorte estadual já representado por Silva (2023) e Encinas e Duenhas (2020).
- Desigualdade educacional e valorização docente: uma análise de convergência do Ideb condicionado ao financiamento da Educação Básica pública (2024, W4391436292): Preprint; o Ideb como desfecho já está em Silva Júnior et al. (2025), com revisão por pares.
- Tão próximos e tão distintos: análise do financiamento educacional em quatro municípios do interior paulista (2024, W4391758525): Quatro municípios paulistas; escala já tratada em Nascimento e Pinto (2024).
- O Novo Fundeb e a Sistemática de Redistribuição dos Recursos (2024, W4400652765): Análise documental do desenho do novo Fundeb, sem medir desigualdade.
- Análise do gasto-aluno em um grupo de municípios de pequeno porte do Estado de São Paulo (2024, W4404228161): Dissertação do mesmo autor de Nascimento e Pinto (2024), com 12 municípios.
- Valor Aluno Ano Redução de Desigualdades – VAAR (!) (2024, W4404716897): Análise documental da condicionalidade III do VAAR, sem medir efeito.
- SUBFINANCIAMENTO E DESIGUALDADES NA EDUCAÇÃO BÁSICA BRASILEIRA: LIMITES E POSSIBILIDADES DO FUNDEB (2024, W4405511654): Comunicação em congresso, recorte de dissertação; evidência menos detalhada que os artigos selecionados.
- Primeiro ano de implementação da Complementação-VAAR do Novo Fundeb: desafios e legados para uma educação com equidade (2024, W4411203072): Dissertação sobre o primeiro ano do VAAR; ficou o artigo correspondente (Silva e Schlegel, 2025).
- O VAAT no financiamento da educação dos municípios da Paraíba no ano de 2021: elementos para o debate sobre democracia e valorização docente (2023, W4328127664): Mesmo autor e estado de Silva (2023); foco em VAAT e valorização docente.
- Fundeb e complementação financeira da União: perspectivas a partir da abrangência do VAAT nos municípios da Paraíba (2023, W4377087909): Mesmo autor e estado de Silva (2023); versão anterior e menos direta.
- Complementação financeira da União ao Fundeb: um estudo sobre o VAAT em 2023 (2023, W4389474377): Abrangência do VAAT em 2023; mesmo autor de Silva (2023), que mede desigualdade diretamente.
- O financiamento do ensino fundamental público no estado do Piauí : o desafio da equidade intermunicipal (2023, W7119286926): Dissertação sobre Piauí (2008-2018); sem PDF aberto indicado no OpenAlex e recorte estadual já representado.
- Reflections on the effect of the new Fundeb on the equity of basic education in the municipalities of Goiás (2023, W7120360561): Dissertação qualitativa sobre Goiás, sem medida de desigualdade no resumo.
- Desigualdade no Financiamento da Educação Básica: panorama do valor anual total por aluno (VAAT) para o novo Fundeb (2022, W4220863908): Panorama descritivo do VAAT; o resumo não traz medida de desigualdade.
- Análise dos estudos e das propostas de alterações dos fatores de ponderação do Fundeb (2022, W4225277669): Fatores de ponderação simulados; Senkevics et al. (2026) cobre os ponderadores atuais.
- Elementary Education in Brazilian municipalities: possible relationships between quality, funding, organization and socioeconomic contexts (2022, W7120764834): Tese sobre financiamento e proficiência no Saeb (2010-2019); sem PDF aberto indicado pelo OpenAlex; o desfecho de aprendizagem já está em Hirata et al. (2022) e Silva Júnior et al. (2025).
- Racismo e Equalização: o Novo Fundeb e o Direito à Educação Escolar Indígena e Quilombola e em Territórios de Vulnerabilidade Social (2021, W3163679273): Propostas normativas sem dados; a pauta racial ficou em Tripodi et al. (2022), que propõe medida.
- Brazil Case Study (2021, W3213277631): Estudo de caso institucional do Banco Mundial; descreve o sistema de transferências.
- A educação infantil e sua vinculação à nova complementação da União ao Fundeb (2021, W4200593871): Foco na vinculação de 50% do VAAT à educação infantil.
- A política de fundos na educação básica brasileira: efeito redistributivo do Fundeb em municípios baianos (2021, W4231620962): Dez municípios baianos em um ano; recorte estadual já representado com maior cobertura.
- Comparação das despesas estaduais por etapa de ensino e os desafios para avançar no novo Fundeb (2021, W4361861006): Comparação de despesas estaduais; o foco é a qualidade dos dados do Siope.
- Equidade educacional na Federação brasileira: o papel das transferências federais aos municípios (2020, W3020287430): Dissertação que origina o IERRE; ficou o artigo que aplica o indicador ao novo Fundeb (Santos et al., 2022).
- Dilemas federativos e construção de capacidades em nível local : uma análise dos fatores associados ao FUNDEB na educação infantil (2020, W3128899856): Dissertação sobre Fundeb e acesso à educação infantil; sem PDF aberto indicado pelo OpenAlex.
- Repercussões do FUNDEB em Municípios Mineiros: aportes para a discussão sobre um FUNDEB permanente (2019, W2921711393): Minas Gerais em 2017; cenário com e sem Fundeb já tratado em âmbito nacional por Hirata et al. (2022).
- EDUCAÇAO E DESIGUALDADES REGIONAIS: OS IMPACTOS DO FUNDEB NO BRASIL (2019, W2950815256): Dados de 2005-2009 e DOI que indica edição de 2011, embora o OpenAlex registre 2019; não é recente.
- Desigualdades no Financiamento da Educação Escolar em Minas Gerais (2019, W2971695435): Minas Gerais, série 2000-2015 com foco em receitas fora do Fundeb.
- Novo Fundeb: Prós e contras das propostas em debate (2019, W2974754194): Relatório de propostas pré-reforma, superado pela regulamentação de 2020.
- Texto para discussão n. 33: aprimorando a equidade no fundo de manutenção e desenvolvimento da educação básica e de valorização dos profissionais da educação (Fundeb) (2019, W2991125360): Simulação pré-reforma de proposta específica; simulações do desenho aprovado foram priorizadas.
- As transferências fiscais no federalismo brasileiro: sobre o repasse do FUNDEB ao Estado do Maranhão (2019, W3031582527): Dissertação sobre Maranhão; recorte estadual já representado.
- A política de fundos no Brasil para o financiamento da educação e os desafios da equidade e qualidade (2019, W3209786975): Panorama para leitor estrangeiro; síntese, não estudo novo.
- O REGIME DE COOPERAÇÃO FEDERATIVA DA POLÍTICA EDUCACIONAL: uma análise a partir dos efeitos redistributivos do FUNDEF e do FUNDEB (2018, W2815125898): Efeitos redistributivos em artigo de 2018 sobre o regime de colaboração; recorte anterior à reforma.
- A Política de Fundos (Fundef/Fundeb) e suas Disparidades no Financiamento da Educação Básica no Estado do Rio Grande do Sul (2018, W2883516159): Rio Grande do Sul, 2005-2014, anterior à reforma; achado análogo já em Encinas e Duenhas (2020).
- Potencial redistributivo dos fatores de ponderação : o Fundeb diante da demanda dos municípios (2018, W2888577150): Simulação de ponderadores para creche e pré-escola, anterior ao novo desenho.
- Federalismo e financiamento da educação pública: uma análise da equidade fiscal na educação infantil e ensino fundamental nos municípios brasileiros (2018, W2979566336): Dissertação com dados de 2015, sem PDF indicado; diagnóstico já coberto por Alves e Pinto (2020).

## Fundeb tangencial: citado, mas o objeto é outro (ICMS Educacional, Salário-Educação, FPM, gestão, política educacional em geral) (63)

- TENSÕES E CONTRADIÇÕES DA MUNICIPALIZAÇÃO DA EDUCAÇÃO BÁSICA NO BRASIL: UMA REVISÃO DE LITERATURA COM ÊNFASE EM MINAS GERAIS (2026, W7140105106)
- POLÍTICAS PÚBLICAS EDUCACIONAIS E QUALIDADE DO ENSINO NA EDUCAÇÃO BÁSICA NO BRASIL: DESAFIOS PARA A EFETIVAÇÃO DE UMA EDUCAÇÃO (2026, W7147147531)
- ICMS educacional : Análise da tramitação da lei nº 15.766 – ICMS cota educação, na Assembleia Legislativa do Estado do Rio Grande do Sul (2026, W7162167438)
- Políticas públicas e gestão democrática na educação municipal: desafios e estratégias para uma educação de qualidade (2026, W7162198600)
- A EFETIVIDADE DO DIREITO À EDUCAÇÃO NO BRASIL: DO PRECEITO CONSTITUCIONAL À APLICABILIDADE (2026, W7162454027)
- A educação para as relações étnico-raciais na educação infantil (2026, W7162762515)
- DEMOCRATIZAÇÃO DA EDUCAÇÃO NO BRASIL NO SÉCULO XXI: UMA ANÁLISE DAS POLÍTICAS EDUCACIONAIS DO GOVERNO LULA (2026, W7170199906)
- Educação, Estado, trabalho: carreira docente em debate (2026, W7201928808)
- A GOVERNANÇA ALGORÍTMICA NO FEDERALISMO FISCAL: FALHAS DE DESENHO E A NULIDADE DE ATOS ADMINISTRATIVOS BASEADOS EM DADOS EDUCACIONAIS (2026, W7213416800)
- SISTEMA NACIONAL DE EDUCAÇÃO (SNE): A REPARTIÇÃO DE COMPETÊNCIAS PARA COMBATER DESIGUALDADES REGIONAIS (2026, W7215355024)
- Arcabouço Institucional da Educação e sua Aplicação (2026, W7216702350)
- The Financing of Early Childhood Education and the initial Quality Student Cost in Brazil (2014 to 2024) (2026, W7221133052)
- O PAPEL DAS POLÍTICAS PÚBLICAS DE EDUCAÇÃO NA INCLUSÃO E ASCENSÃO SOCIAL NO BRASIL (2026, W7222794329)
- A trajetória do Plano Nacional de Educação na escala do Rio Grande do Norte (2026, W7223238549)
- Educação e Igualdade: O Impacto das Políticas Públicas na Redução das Desigualdades Sociais no Brasil (2025, W4410982981)
- A EDUCAÇÃO INFANTIL COMO COMPROMISSO DOS MUNICÍPIOS: RESPONSABILIDADE, DESAFIOS E COMPROMISSOS NA PRIMEIRA ETAPA DA EDUCAÇÃO BÁSICA (2025, W4412982822)
- Políticas Públicas em Educação e a Qualidade do Ensino (2025, W4413015571)
- Texto para Discussão 3143 (2025, W4413040981)
- BARÔMETRO DA CIÊNCIA: O QUE PENSAM OS JOVENS BRASILEIROS SOBRE TECNOLOGIA E CONHECIMENTO (2025, W4413784474)
- Expressões da privatização da oferta na educação municipal no Estado de São Paulo (2025, W4413926713)
- DESAFIOS E AVANÇOS NAS POLÍTICAS PÚBLICAS DE EDUCAÇÃO: UM ESTUDO SOBRE O ANALFABETISMO NO BRASIL (2025, W4414651887)
- ICMS educacional: Variações na definição de equidade em normas estaduais (2025, W4415292407)
- Gestão educacional: dos conceitos simples aos complexos (2025, W4415642295)
- DESIGUALDADES EDUCACIONAIS NO BRASIL E AS POLÍTICAS PÚBLICAS DE INCLUSÃO (2025, W4416186246)
- A implementação do atendimento à Educação Infantil no município de Teresina – PI: da política de financiamento à política de convênios (2025, W4416225945)
- POLÍTICAS PÚBLICAS EDUCACIONAIS BRASILEIRAS: ANÁLISE E COMPARAÇÃO DE SUA DIMENSÃO JURÍDICO-NORMATIVA E SUA EFETIVAÇÃO (2025, W4417200879)
- PUBLIC POLICIES IN BRAZILIAN EDUCATION (2025, W4417516410)
- POLÍTICAS PÚBLICAS DE PLANEJAMENTO EDUCACIONAL, PROMOÇÃO DA IGUALDADE E O RECONHECIMENTO DAS DIFERENÇAS: DESAFIOS PARA A ARTICULAÇÃO INTERSETORIAL E INTERSECCIONALIDADE (2025, W7105144514)
- Exploratory Analysis regarding educational indicators, financial resources, and socioeconomic conditions of Pernambuco: A Cluster Analysis (2025, W7117450816)
- Objetivo 17 (2025, W7124312045)
- Educação, suas desigualdades e desempenho, no RS e no Brasil (2025, W7203801042)
- As POLÍTICAS EDUCACIONAIS, ESTADO E SOCIEDADE: Uma análise crítica (2025, W7215547231)
- O ICMS Educacional nos estados da Bahia e de Santa Catarina: entre conformidades, contradições e desigualdades (2024, W4400652748)
- Fatores determinantes do IDHM - Educação nos municípios nordestinos nos anos de 2000 e 2010 (2024, W4401679719)
- PROJETO TRILHAS DE FUTURO: a atuação de grupos educacionais privados na formação profissional em Minas Gerais (2024, W4403935078)
- A distribuição do ICMS-Educação no Estado do Paraná: uma problematização inicial em 12 municípios da região metropolitana de Curitiba (2024, W4404716917)
- POLÍTICAS PARA O FINANCIAMENTO DA EDUCAÇÃO INFANTIL IMPLEMENTADAS NA REGIÃO METROPOLITANA DE CAMPINA GRANDE NO CONTEXTO DO FUNDEB (2024, W7215601972)
- Financiamento da educação e o desafio de superar políticas de austeridade para valorizar o magistério: dilemas nas formas de racionalização do Estado (2023, W4328128683)
- Federalismo de cooperação, municipalização de e universalização da educação (2023, W4380849158)
- Avaliação do impacto da distribuição dos recursos do Salário-Educação, após a implementação do E-Social, quanto à equalização das desigualdades educacionais entre os estados brasileiros (2023, W4387882432)
- O ICMS Educacional como instrumento para a institucionalização e gestão dos sistemas municipais de educação tocantinenses (2023, W4390938668)
- DA DESIGUALDADE A EQUIDADE ESCOLAR: OS EFEITOS DE UMA POLÍTICA EDUCACIONAL EM UM TERRITÓRIO VULNERAVEL BRASILEIRO (2023, W4412024657)
- State capacity in policy delivery: Minas Gerais municipalities and basic education (2023, W7120646912)
- Riscos iminentes de privatização da educação básica (2022, W4226143962)
- POLÍTICAS PÚBLICAS CONTEMPORÂNEAS, DE EDUCAÇÃO E SAÚDE: O DESAFIO DE REDUÇÃO DE DESIGUALDADES (2022, W4312789578)
- Desenho e implementação de políticas públicas: desigualdade e equidade nas políticas de educação e saúde (2022, W7120505026)
- Os conceitos de Educação e Aprendizagem ao Longo da Vida: aspectos históricos e a Educação Especial Brasileira (2021, W3188138117)
- A disputa dos recursos públicos da educação básica, os arranjos do estado com o mercado e seus impactos na gestão democrática e participativa da educação no âmbito dos municípios (2021, W3202542279)
- Deslizamentos nos sentidos de pobreza em discursos educacionais brasileiros: da administração à gestão do social (2021, W4386940143)
- Formation and distribution of the Municipality Participation Fund – FPM and its implications for the socioeconomic development of Brazilian municipalities (2021, W7120731795)
- O serviço público educacional no Brasil e seus contextos de administração: centralização, descentralização, federalização e desigualdades - 1824 a 2019 (2020, W3011319746)
- Fatores determinantes do desempenho educacional no Sudeste Brasileiro (2020, W3022837137)
- POLÍTICAS EDUCACIONAIS E DOCÊNCIA NO ENSINO FUNDAMENTAL DE NOVE ANOS (2020, W3027740100)
- Implicações do novo regime fiscal no setor público da União: revisão integrada de literatura (2020, W3030147263)
- A Agenda do Sistema Nacional de Educação e suas instâncias de pactuação : uma análise das propostas (2020, W3109867188)
- VULNERABILIDADE EDUCACIONAL EM TEMPOS DE PANDEMIA (2020, W3110674847)
- Education financing: governance challenges in the implementation of education programs in Brazil (2020, W7120399850)
- Uso de uma abordagem multicritério para composição de um índice geral de gestão financeira dos municípios do estado de Pernambuco (2020, W7120745024)
- PRINCÍPIOS CONSTITUCIONAIS E A ARRECADAÇÃO DOS TRIBUTOS COMO FINANCIADORES DAS POLÍTICAS EDUCACIONAIS (2020, W7214742744)
- O salário-educação: fragilidades e incoerências (2019, W2732268556)
- Pressupostos do paradigma do Capital Humano aplicados à Primeira Infância (2019, W2947708273)
- Análise das disparidades nos indicadores educacionais municipais de Pernambuco: uma análise de aglomerados (2019, W3034674256)
- Reflexo da aplicação dos recursos públicos no desempenho educacional dos Municípios Catarinenses (2018, W2978721604)

## Fundeb central, mas a desigualdade não é o objeto (valorização docente, escolha de diretores, condicionalidades, etapa específica, disputa política) (47)

- VALORIZAÇÃO SALARIAL DOCENTE E QUALIDADE DA EDUCAÇÃO BÁSICA NO BRASIL: LIMITES E POTENCIALIDADES DO FUNDEB NO SETOR PÚBLICO E DA ATUAÇÃO SINDICAL NO SETOR PRIVADO (2026, W7125613596)
- A GESTÃO DOS RECURSOS DO FUNDEB E SEUS IMPACTOS NA QUALIDADE DA EDUCAÇÃO PÚBLICA (2026, W7160143710)
- O PAPEL DO FUNDEB NO FINANCIAMENTO DA EDUCAÇÃO BÁSICA: DESAFIOS E POSSIBILIDADES NA GESTÃO DOS RECURSOS (2026, W7160187162)
- VAAR e gestão meritocrática (2026, W7160829170)
- FINANCIAMENTO DA EDUCAÇÃO E O FUNDEB NO CEARÁ (2026, W7161988791)
- VALORIZAÇÃO SALARIAL DOCENTE E QUALIDADE DA EDUCAÇÃO PÚBLICA NO BRASIL: FUNDAMENTOS, DESAFIOS E PERSPECTIVAS (2026, W7166292924)
- Remuneração docente em Mato Grosso do Sul a partir do FUNDEB (2007-2020): o que dizem as produções? (2026, W7172249946)
- Políticas Educacionais e Valorização Docente: Avanços, Desafios e Perspectivas para a Educação Brasileira (2026, W7202041011)
- Números do Financiamento da Educação: uma breve análise do novo Fundeb e dos programas de financiamento da Educação do Campo no Brasil (2026, W7203918564)
- A ascensão cearense: o FUNDEB impulsiona os efeitos positivos do ICMS-Educação no ensino básico da região? (2026, W7213461590)
- REVISÃO INTRA-EXERCÍCIO DOS PARÂMETROS DO FUNDEB: FREQUÊNCIA E MAGNITUDE DOS AJUSTES DE VAAF, VAAT E VAAR NAS PORTARIAS INTERMINISTERIAIS DE 2021 A 2026 (2026, W7220678744)
- Gestão democrática e financiamento da educação do sistema municipal de ensino no Seridó Oriental (RN) (2026, W7225317801)
- O (não) lugar do ensino médio na política de financiamento para a educação (2025, W4410967330)
- POLÍTICAS DE VALORIZAÇÃO SALARIAL NO CONTEXTO DO FUNDEB E SEUS EFEITOS NA MOTIVAÇÃO DOS SERVIDORES MUNICIPAIS (2025, W4416751786)
- Public financing for basic education: implications for the implementation process of the new FUNDEB (2025, W7120323889)
- Democratization of school management in a municipality in the high Sertão of Paraíba: limits and possibilities from the Municipal Education Plan (2015-2025). (2025, W7120876325)
- A SELEÇÃO DE GESTORES ESCOLARES NO MUNICÍPIO DE LAGO DO JUNCO-MA A PARTIR DE 2022 (2025, W7127420895)
- GESTÃO DEMOCRÁTICA E VAAR: A LÓGICA DE CONDICIONALIDADES NO FINANCIAMENTO DA EDUCAÇÃO BÁSICA PÚBLICA (2025, W7144334836)
- Os Desafios da Gestão Escolar Mediante o Fundeb no Médio Mearim – Maranhão (2025, W7217268066)
- AS CONDICIONALIDADES DO FUNDEB PERMANENTE: IMPACTOS DO MARCO LEGISLATIVO DE SANTA CATARINA NO SISTEMA MUNICIPAL DE ENSINO (2025, W7220156730)
- RELAÇÕES ENTRE GESTÃO DEMOCRÁTICA E AS EXIGÊNCIAS DO NOVO FUNDEB EM MUNICÍPIOS PARANAENSES (2024, W4390492803)
- AS DESIGUALDADES DE FINANCIAMENTO DOS ENTES FEDERADOS E AS POLÍTICAS DE VALORIZAÇÃO DOCENTE (2024, W4391876409)
- FUNDEB: POLÍTICA PÚBLICA COMO INSTRUMENTO DE VALORIZAÇÃO DO MAGISTÉRIO. (2024, W4391876536)
- Análise da produtividade na alocação de recursos do FUNDEB no estado do AMAPÁ entre 2010 e 2019 (2024, W4393103494)
- A Meta 19 do PNE e a complementação do Fundeb categoria Vaar (2024, W4399117428)
- Disputas entre atores no financiamento da educação: o caso do Fundeb permanente e sua regulamentação (2015-2021) (2024, W4401880817)
- O FUNDEB PERMANENTE: COMO UMA POLÍTICA PÚBLICA IMPORTANTE PARA FINANCIAR A REMUNERAÇÃO DO MAGISTÉRIO DA EDUCAÇÃO BÁSICA (2024, W4402411770)
- Reflexões sobre as condicionalidades impostas pelo novo Fundeb e a inserção das escolas públicas na competição mercadológica (2024, W4403246435)
- O novo Fundeb e o processo de escolha de diretores e vice-diretores no município de Marabá – PA: análise sobre o atendimento da condicionalidade I nos termos da lei 14.113/20 (2024, W4404373963)
- Um balanço do Fundeb no estado de Mato Grosso do Sul (2009 a 2020) (2023, W4328098886)
- O financiamento da educação de jovens e adultos no estado do Pará – desafios históricos (2023, W4328129337)
- ARTICLE - WHAT IS THE VALUE OF A QUALITY EARLY CHILDHOOD EDUCATION? (2023, W4365804315)
- O VAAR E A GESTÃO DA SALA DE AULA: A APLICACABILIDADE DA CONDICIONALIDADE III DA LEI 14. 113/2020 NO CONTEXTO DA AVALIAÇÃO DA APRENDIZAGEM NAS REDES PÚBLICAS DE ENSINO (2023, W4380563478)
- O Fundeb permanente e as condicionalidades do VAAR em municípios tocantinenses (2023, W4387857286)
- Financiamento do Direito à Educação: disputas sobre a PEC n. 15/2015 (2023, W4389474408)
- Proposta metodológica de cálculo dos custos médios do Fundeb e o novo PNE (2023, W4391956331)
- Accounting information for the social control of Basic Education in the state of Rio de Janeiro: case study of the Social Control and Monitoring Council of Fundeb/RJ in COVID-19 public health emergency period (2023, W7119256638)
- Financiamento da educação básica pública e o novo FUNBEB: um estudo de caso sobre a capacidade de investimento dos municípios do Consórcio Intermunicipal de Educação e Ensino do Paraná (Ciedepar) (2023, W7120672523)
- Planos de cargos, carreira e remuneração dos professores das redes municipais de educação de Cametá/PA e Oeiras do Pará: a carreira e os recursos do Fundeb na remuneração (2007-2020) (2023, W7120854995)
- Trabalho docente no Brasil pós-pandêmico (2022, W4225985730)
- DIREITO À EDUCAÇÃO DO CAMPO NA POLÍTICA DE FINANCIAMENTO DA EDUCAÇÃO BÁSICA: AVANÇOS E LIMITES A PARTIR DAS POLÍTICAS DE FUNDOS REDISTRIBUTIVOS (2022, W4313164178)
- Financiamento e expansão do ensino médio: o caso da diversificação da oferta no Ceará (2021, W3201968722)
- O FINANCIAMENTO NA EDUCAÇÃO INFANTIL: EM FOCO O FUNDEB E OS DESDOBRAMENTOS COM O FIM DA VIGÊNCIA DA LEI (2020, W3023486966)
- Educação infantil e a política de fundos: como tem caminhado essa etapa educacional, em especial com a aprovação do Fundeb? (2020, W3091333754)
- Contribuições para um Balanço do Fundeb: redistribuição dos recursos, despesas com remuneração e vínculo de trabalho docente (2020, W3091713855)
- Um estudo sobre a inclusão escolar e os recursos financeiros para o atendimento dos alunos com deficiência, no município de Marabá-PA (2019, W2981798549)
- Da lógica do gasto à do custo: financiamento do ensino médio integral (2019, W2984298422)

## Revisão, ensaio ou análise normativa sem dados próprios sobre desigualdade (39)

- O FINANCIAMENTO DA EDUCAÇÃO PÚBLICA NO BRASIL: DESAFIOS, DESIGUALDADES E SUSTENTABILIDADE DO SISTEMA (2026, W7127080420)
- Financiamento da Educação Básica: conceitos, lugares e mecanismo (2026, W7131659663)
- Fundo de Manutenção e Desenvolvimento da Educação Básica e de Valorização dos Profissionais da Educação: uma avaliação dos resultados alcançados pelo Fundeb entre 2007 e 2020 (2026, W7203877572)
- O novo FUNDEB e a meritocracia por meio do VAAR no contexto da Educação Básica Brasileira (2026, W7204262935)
- A política de financiamento da educação básica como vetor da qualidade de ensino: investimento calcado em resultados (2026, W7208722141)
- GOVERNANÇA DO FUNDEB E SUSTENTABILIDADE DO FINANCIAMENTO DA EDUCAÇÃO BÁSICA: DESAFIOS CONTEMPORÂNEOS PARA A GESTÃO EDUCACIONAL BRASILEIRA (2026, W7214979354)
- O NOVO FUNDEB E O DIREITO À EDUCAÇÃO: AVANÇOS NA POLÍTICA DE FINANCIAMENTO? (2026, W7217860341)
- FUNDEB (2025, W4407333237)
- A relação entre o FUNDEB e a relação das desigualdades sociais (2025, W4409292515)
- Avanços e Desafios da Educação Básica no Brasil: da criação dos fundos de financiamento ao FUNDEB permanente (2025, W4410761608)
- FUNDEB: FUNDO REVOLUCIONÁRIO OU COSPLAY DE FUNDEF? (2025, W4410882736)
- POLÍTICAS PÚBLICAS E O FINANCIAMENTO DA EDUCAÇÃO NO BRASIL: FUNDEF E FUNDEB (2025, W4411269103)
- REFLEXÃO ACERCA DA GARANTIA DA POLÍTICA DE GESTÃO EDUCACIONAL NO BRASIL (2025, W4411747713)
- FINANCIAMENTO DA EDUCAÇÃO PÚBLICA NO BRASIL: ANÁLISE COMPARATIVA ENTRE FUNDEF E FUNDEB (2025, W4417136547)
- O Fundeb e a concretização do direito à educação (2025, W7121699562)
- POLÍTICAS PÚBLICAS E GESTÃO NA EDUCAÇÃO: O FINANCIAMENTO DA EDUCAÇÃO BÁSICA E SEUS IMPACTOS NA GESTÃO ESCOLAR NO ESTADO DE SÃO PAULO (2025, W7124564187)
- política de financiamento a partir do Novo Fundeb: (2025, W7128424429)
- FINANCIAMENTO DA EDUCAÇÃO BÁSICA NO BRASIL: CONFIGURAÇÕES HISTÓRICAS, DESAFIOS E PERSPECTIVAS (2025, W7215205093)
- O ESTADO FEDERATIVO E O FINANCIAMENTO DA EDUCAÇÃO BÁSICA: entre princípios e desigualdades (2025, W7215240132)
- NOVO FUNDEB E A COMPLEMENTAÇÃO DO VALOR ALUNO ANO RESULTADO: CENÁRIO DE DESIGUALDADE SOCIAL E EDUCACIONAL (2024, W4393189516)
- As complementações da união (VAAT e VAAR) à luz do novo FUNDEB (2023, W4327711808)
- NOVO FUNDEB: UMA INCURSÃO SOBRE SEUS POSSÍVEIS AVANÇOS (2023, W4385804741)
- Evolução do FUNDEB e sua constitucionalização permanente: percepções epistemológicas e os benefícios acadêmicos, sociais e econômicos (2023, W4386136593)
- FINANCIAMENTO DA EDUCAÇÃO BÁSICA: PRINCIPAIS PROGRAMAS, IMPACTOS E SEUS DESAFIOS (2023, W4387106743)
- (DES)CAMINHOS DA POLÍTICA DE FUNDOS NO FINANCIAMENTO DA EDUCAÇÃO BÁSICA NO BRASIL (2023, W4387463952)
- Políticas públicas de financiamento da educação no Brasil (2023, W4396682927)
- O novo Fundeb e o Direito à Educação: avanços, retrocessos e impactos normativos (2022, W4391666348)
- O (DES) regulamento do novo Fundeb: aplicações e contradições (2022, W7219934761)
- NOVO FUNDEB E GARANTIAS CONSTITUCIONAIS QUANTO AO DIREITO EDUCACIONAL: BUSCA PELA REDUÇÃO DAS DESIGUALDADES SOCIAIS (2021, W3148105631)
- O financiamento da educação básica no Brasil contemporâneo: avanços e contradições revelados nos gastos da educação de Santo André (2021, W3195083162)
- Financiamento da educação básica de qualidade: os caminhos e descaminhos até o novo Fundeb (2021, W4236470603)
- UM PANORAMA A RESPEITO DA POLÍTICA DE FUNDOS PARA O FINANCIAMENTO DA EDUCAÇÃO NO BRASIL – DO FUNDEF AO FUNDEB (2021, W4294968928)
- A DURA BATALHA PELA MANUTENÇÃO DO FUNDEB (2020, W3134610252)
- DIREITO À EDUCAÇÃO: O DESENHO JURÍDICO DO FUNDEB (2020, W7220606120)
- O “Novo” Fundeb: o CAQi na encruzilhada (2019, W2984187806)
- Federalismo, Vinculação, Fundeb, VAAT e CAQ (2019, W2986059011)
- Os rumos do FUNDEB (2019, W3007072887)
- O financiamento da educação (2019, W3011206733)
- O FINANCIAMENTO DA EDUCAÇÃO NA CONSTITUIÇÃO FEDERAL DE 1988: 30 ANOS DE MOBILIZAÇÃO SOCIAL (2018, W2901183625)

## Estudo de um único município ou de recorte local, sem comparação entre entes (16)

- ANÁLISE DO NOVO FUNDEB NA EDUCAÇÃO BÁSICA DO MUNICÍPIO DE MARAVILHA-SC (2026, W7125162926)
- Gestão dos recursos do FUNDEB em Beberibe: análise da relação com os indicadores de aprendizagem na rede pública municipal (2026, W7164809665)
- IMPLEMENTAÇÃO E FINANCIAMENTO DA EQUIDADE RACIAL NA EDUCAÇÃO BÁSICA: O CASO DO VAAR/FUNDEB EM IRARÁ (BA) (2026, W7212081534)
- GOVERNANÇA E FINANCIAMENTO DA EDUCAÇÃO PÚBLICA MUNICIPAL: DESIGUALDADES TERRITORIAIS NA COBERTURA DA REDE DE ENSINO NO MUNICÍPIO DE JUARA, MATO GROSSO (2026, W7215711426)
- FUNDEB E FINANCIAMENTO DA EDUCAÇÃO MUNICIPAL DE PORTO VELHO: SUFICIÊNCIA, EQUIDADE E QUALIDADE DO GASTO (2026, W7220955114)
- O financiamento da educação básica municipal: um estudo dos impactos do novo Fundeb dos três maiores municípios do Sul de Minas Gerais, Brasil (2026, W7222887150)
- Efeito redistributivo do Fundeb no município de Cachoeira do Piriá/PA: possibilidades e limites do regime de colaboração (2025, W4413427542)
- Financiamento da Educação Básica em um município baiano: Análise da Evolução do FUNDEB nos últimos anos (2025, W4416716796)
- Contradições entre os objetivos do Fundeb e da austeridade fiscal: o caso de Curitiba-PR (2017-2019) (2024, W4402984722)
- Desafios e perspectivas da educação do campo em Alegre/ES: análise da efetividade do fundeb permanente como instrumento de financiamento para promoção da equidade e justiça social (2024, W7119430878)
- IMPACTO DOS REPASSES CONSTITUCIONAIS (FUNDEB) NA QUALIDADE DA EDUCAÇÃO PÚBLICA NO MUNICÍPIO DE TEIXEIRA DE FREITAS, BAHIA (2023, W4318686667)
- ART FINANCIAMENTO DA EDUCAÇÃO NO MUNICÍPIO DE TANGARÁ DA SERRA/MT E O PISO SALARIAL PROFISSIONAL NACIONAL (2023, W7217295351)
- Políticas Educacionais e o Financiamento à Creche em São Gonçalo/RJ: um estudo de caso (2011-2020) (2022, W4280612498)
- O Financiamento da Educação Infantil nos municípios da região do Jalapão – Tocantins: (in)capacidades e desigualdades no atendimento da meta 1 do PNE/PME (2021, W4205343846)
- A Política de Financiamento da Educação Básica no Município de Cascavel - Paraná (2008-2019) (2020, W3168447673)
- Análise das diferenças do gasto/aluno nas escolas de uma rede municipal à luz do princípio da equidade (2019, W3154860363)

## Sem resumo utilizável (sem abstract no OpenAlex ou texto que não é resumo) (8)

- CAPACIDADES ESTATAIS E EQUIDADE NO NOVO FUNDEB: UMA ANÁLISE DA HABILITAÇÃO AO VAAR 2024 NOS MUNICÍPIOS DO CIMBAJU (2026, W7171959659)
- Public spending and pupils' achievement: Evidence from public elementary schools in Brazil (2025, W4415122364)
- The role of federal government supplementation in the permanent FUNDEB (National Fund for Basic Education Development) for reducing intra-state inequality in fund resources in Maranhão (2025, W7120276700)
- O acesso à educação infantil no contexto da implementação do FUNDEB permanente e da complementação VAAT (2024, W7120829475)
- Fundeb permanente : uma análise qualitativa das produções sobre o tema diante das desigualdades educacionais (2023, W7197398669)
- The Education System of Brazil: Financing of Education in Brazil (2021, W4205386499)
- Financing of Education in Brazil (2020, W3110544612)
- O federalismo fiscal brasileiro e a experiência do FUNDEB: aplicação do modelo de equalização fiscal (2019, W3046158089)

## Registro duplicado (versão, tradução, dataset ou depósito de trabalho já listado) (7)

- ANALYSIS OF THE NEW FUNDEB IN BASIC EDUCATION IN THE MUNICIPALITY OF MARAVILHA-SC (2026, W7125472110)
- Teacher Salary Appreciation and the Quality of Basic Education in Brazil: Limits and Possibilities of Fundeb in the Public Sector and of Trade Union Action in the Private Sector (2026, W7125610558)
- Productivity analysis in resource allocation of FUNDEB in the state of Amapa between 2010 and 2019 (2024, W4393072619)
- ARTICLE - WHAT IS THE VALUE OF A QUALITY EARLY CHILDHOOD EDUCATION? (2023, W4394404145)
- Qual é o valor de uma educação infantil de qualidade? (2023, W7119251394)
- AFFIRMATIVE ACTION IN BASIC EDUCATION: SUBSIDIES FOR THE FUNDEB EQUITY MEASURE (2022, W4312364861)
- O Fundeb e a questão da equidade (2022, W4394407561)

## Não é pesquisa original (índice, editorial, apresentação de dossiê, resenha) (6)

- Apresentação (2025, W4413124173)
- SOUSA, Sandra Zákia; Lopes, Valéria Virgínia. Avaliação Educacional de Aprendizagem, Institucional e em larga escala. São Paulo: Contexto: 2024 (2025, W7113904120)
- Index (2023, W4319780543)
- Os desafios do financiamento da educação básica no Brasil em perspectiva multidisciplinar (2022, W4225568608)
- Dossiê Financiamento da educação contemporânea: desafios e impasses (2021, W3202550330)
- REVISTA FINEDUCA – 10 ANOS DE CONTRIBUIÇÃO À PESQUISA EM FINANCIAMENTO DA EDUCAÇÃO (2020, W3109968057)

## Fora do recorte Brasil (1)

- School Finance in Latin America: A Conceptual Framework and a Review of Policies (2018, W2890071566)
