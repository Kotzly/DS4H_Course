## Estrutura de arquivos e pastas

```text
DS4H_Course
├───assets                              <- Arquivos relacionados ao projeto.
│   └───excel                           <- Arquivos excel gerados durante o desenvolvimento.
├───data                                <- Dados utilizados no projeto.
│   ├───external
│   └───processed
│       └───indexes
├───documents                           <- Documentos relacionados ao projeto e aos dados.
├───notebooks                           <- Notebooks jupyter utilizados no projeto.
└───src                                 <- Código fonte do projeto.
    ├───ds4h                            <- Pacote python instalável.
    │   ├───data
    │   ├───orange
    │   ├───processing
    │   ├───scripts
    │   └───visualization
    └───orange                          <- Arquivos do Orange usados para visualização.
```
# Instalação

O projeto está sendo desenvolvido majoritariamente em Python 3.6, mas também foram utilizadas outras ferramentas como R, Orange, e Prism. É possível instalar o pacote do projeto (`ds4h`) seguindo os seguintes passos:
 - Instale o [Anaconda](https://www.anaconda.com/products/individual). Ele será usada para o gerenciamento do ambiente python.
 - Para rodar os scripts do Orange, instale-o na tela inicial do Anaconda. Para fazer isso, abra o Anaconda Navigator no seu computador, e clique em `install` no ícono do Orange.
 - Na linha de comando ou no Anaconda shell, crie o ambiente com:

```
conda env create -n ds4h python=3.6
conda activate ds4h
```

 - Na pasta raiz do projeto, instale o pacote com:

```
pip install ./src
```

 - Caso você vá rodar o notebook principal do projeto, instale a linguagem R em sua máquina. A maneira mais fácil de fazer isso é instalando o [RStudio](https://www.rstudio.com/products/rstudio/download/#download), mas não problema em instalar apenas o R.

## Como usar

É possível executar todas os passos de download, pré-processamento, processamento e análise de dados (feitos até a segunda entrega) [neste notebook](https://colab.research.google.com/github/Kotzly/DS4H_Course/blob/v1.0/notebooks/DS4H_full.ipynb) no Google Colab. Considera-se a entrega principal como sendo este notebook, que contém os racional das análises, além do código Python.

Para executar o notebook em sua própria máquina, primeiro siga todos os passos descritos em **Instalação**. Após isto, abra a linha de comando ou o Anaconda shell na pasta raiz do projeto e rode:

```
conda activate ds4h
jupyter notebook
```

Vá até a pasta `notebooks` e abra o notebook **DS4H_full.ipynb**.



# Projeto `Impacto da pandemia da COVID-19 nos indicadores da saúde materna e perinatal nas mulheres em idade fértil do Estado de São Paulo.`

## Project `Impact of the COVID-19 pandemic on maternal and perinatal health indicators in women of childbearing age in the state of São Paulo.`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2021, na Unicamp.


|Nome  | RA | Especialização|
|--|--|--|
|Charles M'poca Charles | 163383 | Saúde|
| Silvia Arantes Pereira Olivio | 224932  | Computação|
| Débora Rocha Helfstein  | 234934  | Farmacêutica|
| Paulo Augusto Alves Luz Viana | 263889 | Elétrica |

Você pode rodar o notebook com todas as análises atráves deste [Jupyter notebook no Google Colab!](https://colab.research.google.com/github/Kotzly/DS4H_Course/blob/v1.0/notebooks/DS4H_full.ipynb).

## Descrição Resumida do Projeto
Introdução: A pandemia da COVID-19 causada pelo vírus SARS_COV_2 tem tomado proporções alarmantes ao nível mundial. Atualmente (12/04/2021), ao nível global foram notificados cerca de 136,181,468, sendo o Brasil um dos países mais afetado pela pandemia, com aproximadamente 2,938,804 caso notificados. A pandemia tem afetado a população no geral sem distinção do sexo, raça, e estrato social com grande impacto no sistema de saúde. De entre os efeitos da pandemia no sistema de saúde, destacam-se a interrupção ou redução de provisão dos serviços de saúde materna e perinatal que podem influenciar negativamente nos seus indicadores, como é o caso do número de nascidos vivos. Objetivo: o presente estudo tem o objetivo de avaliar o impacto da pandemia da COVID-19 no número de nascidos vivos nos municípios do estado de São Paulo. Metodologia: será realizado uma análise de serie temporal, baseada em dados Sistema de Informações de Nascidos Vivos (SINASC/DATASUS) e do Banco de Dados de Síndrome Respiratória Aguda Grave (SRAG 2021), com o auxílio de métodos estatísticos  e de ferramentas inteligência artificial (métodos de aprendizado de maquinas) - Google Colab e  Jupyter Notebook - realizaremos a modelagem, análise da curva de nascimentos vivos nos últimos 10 anos prévios a pandemia e a predição do número de nascidos vivos esperados para o ano 2020.  Resultados esperados: através desta pesquisa esperamos obter os padrões das curvas de nascidos vivos e estabelecer uma correlação entre a pandemia e o indicador de saúde materna e perinatal para os diferentes municípios do estado de São Paulo.

## Abstract
Introduction: The COVID-19 pandemic caused by the SARS_COV_2 virus has reached alarming proportions worldwide. As of 21rst June 2021, 178,553,726 COVID-19 cases have been reported worldwide, Brazil being one of the most affected countries, with approximately 17,927,928 reported cases. The pandemic has affected the non-general population regardless of sex, race, and social strata, with a great impact on the health system. Among the effects of the pandemic on the health system, a significant disruption (interruption or reduction) in the provision of maternal and perinatal health services stand out.  The disruption of the sexual and reproductive health might have a significant negative impact on maternal and neonatal outcomes, such as the number of live births, preterm birth, and stillbirth and so on. Objective: This study aims was to assess the impact of the COVID-19 pandemic on the number of live births in the cities of the state of Sao Paulo. Methodology: a data-driven time series analysis (ecological study) was carried out, based on data from the Live Birth Information System (SINASC / DATASUS) and the Severe Acute Respiratory Syndrome Database (SRAG 2021). Using an artificial tools ( machine learning methods) - Google Colab and Jupyter Notebook - We conducted a statistical analysis based on  modelling, analysis of the curve of live births in the last 10 years prior to the pandemic and the prediction of the number of live births expected for the year 2020. Expected results: Through this research, we hope to obtain the patterns of the live birth curves and establish a correlation between the pandemic and the maternal and perinatal health indicator for the different municipalities of Sao Paulo state.

# Videos do Projeto  - Débora

## Vídeo da Proposta
Por favor, assista ao [vídeo](https://drive.google.com/file/d/1xz9lfkAAQFm5fQf4hEIceaY8FeVvwFCI/view?usp=sharing) de apresentação do projeto.

## Vídeo da Apresentação Final  - Falta


# Slides do Projeto

## Slides da Proposta - https://github.com/Kotzly/DS4H_Course/blob/main/Slides%20do%20Projeto
## Slides da Apresentação Final - apresentação entrega final (1).pptx

# Introdução e Referenciais de Teóricos 
A pandemia da COVID-19 causada pelo vírus SARS_COV_2 tem tomado proporções alarmantes ao nível mundial (1). Atualmente (21/06/2021), ao nível global foram notificados cerca de 178.553.726, sendo o Brasil um dos países mais afetado pela pandemia, com aproximadamente 17,927,928 caso notificados (2). A pandemia tem afetado a população no geral sem distinção do sexo, raça, e estrato social com grande impacto no sistema de saúde.
A implementação das medidas de mitigação da pandemia tais como a imposição de medidas restritivas para circulação de pessoas, encerramento de escolas e de atividade consideradas não essenciais, em locais onde são implementadas adequadamente, tem contribuído para a redução dos casos de infeção (3). 
No Brasil, apesar da existência de um sistema de saúde robusto, a implementação de medidas político administrativas contraproducentes para a mitigação dos feitos da pandemia e a redução do financiamento do sistema público de saúde, Sistema Único de Saúde (SUS), tem contribuído para os efeitos devastadores da pandemia no país (4,5). 
Os diversos sistemas de saúde, foram severamente afetados pela pandemia da COVID-19, e os efeitos foram mais significativos nos países de baixa e média renda, onde os recursos humanos, infraestruturas e o sistema de saúde são escassos e frágeis (6). Para reverter os efeitos da pandemia, os sistemas de saúde foram reorganizados a diferentes níveis, com redirecionamento de recursos humanos e infraestruturas para o enfretamento da pandemia (6).  
De entre os efeitos da pandemia no sistema de saúde, destacam-se a interrupção ou redução de provisão dos serviços de saúde materna e perinatal. Dados da literatura, indicam que ao nível mundial, os serviços de saúde sexual e reprodutiva, foram os mais severamente afetados.  Por exemplo, os dados do inquérito realizado pela Organização Mundial da Saúde (OMS) em 105 países, de diferentes regiões e continentes, sugerem que no início da pandemia provocou a redução ou interrupção do provimento dos serviços de saúde sexual e reprodutiva em mais de 50% dos países participantes (cerca de 68% dos serviços de planejamento familiar e 56% das consulta pré-natal) (7). 
A redução ou interrupção destes serviços essenciais violam os princípios fundamentais dos direitos humanos. Adicionalmente, colocam em perigo a saúde materna e perinatal com aumento considerável da incidência de gravidez não planejada, abortos inseguros, óbitos fetais morbidade e mortalidade materna, comprometendo deste modo os ganhos alcançados nas últimas duas décadas na área de saúde e os objetivos de desenvolvimento sustentável, agenda 2030 (8,9). 
Deste modo, o número de nascidos vivos pode ser um indicador chave para mensuração dos impactos da pandemia na saúde materna e perinatal. 

>
> Indicação (bastante resumida) da análise proposta
>
> Indicação (bastante resumida) dos resultados alcançados

## Perguntas de Pesquisa
 - Qual foi o impacto da pandemia da COVID-19 na taxa de nascidos vivos no Estado de São Paulo?
 - É possível prever a taxa de nascidos vivos dos anos seguintes com os dados anteriores?

# Objetivos do Projeto 
> Avaliar o impacto da pandemia da COVID-19 no número de nascidos vivos nos municípios do estado de São Paulo
> Desenhar modelos predictores de números de nascidos vivos com base em modelos matemáticos/machine learning. 

# Metodologia 

Utilização de análise estatística e testes de hipótese para verificação da primeira pergunta de pesquisa. Criação de modelos estatísticos para avaliação do impacto de diferentes variáveis populacionais no impacto do número de nascidos vivos.

Utilização de Aprendizado de Máquina e modelos estatísticos para predição de eventos futuros utilizando os dados à disposição. Análise do impacto das variáveis preditoras do número de nascidos vivos para explicação dos fenômenos encontrados.

## Análise estatística
Durante a análise dos dados, decidimos realizar um teste de hipóteses sobre os dados. A hipótese nula defende a ideia de que não existe diferença entre os anos sem e com pandemia.
A primeira dificuldade que encontramos foi a de achar um teste para um conjunto de dados pequeno e que pudesse ser usado por uma distribuição não normal. 
Após inúmeras pesquisas, descobrimos que os testes não paramétricos não supõem uma distribuição específica para a população, esses testes podem ser especialmente úteis quando você tem uma amostra pequena e destruição não normal, que se identificava com a nossa amostra.
Porém a exemplo dos testes que encontramos como o teste H de Kruskal-Wallis é uma versão não paramétrica da ANOVA, era necessário ter variáveis quantitativas, e o nosso modelo tem uma variável de resposta quantitativa e variáveis explicativa categórica.
Diante dessa segunda dificuldade optamos por utilizar o Teste one way anova, e apesar do modelo não ter uma distribuição normal, foi o teste que mais deu significância.
Portanto o teste escolhido foi One-way ANOVA que será executado levando em consideração as estratificações abaixo:
   - Divisão étnica/racial:
    - Apenas brancos;
    - Apenas não-brancos.
 - Divisão por escolaridade:
    - Até 7 anos de estudos;
    - 8 ou mais anos de estudos.
 - Divisão por estado civil:
    - Casada ou união estável;
    - Solteira.
 - Por idade:
    - Menos de 20 anos (A1);
    - De 20 anos à 35 anos (A2);
    - Mais de 35 anos (A3);

## Bases de Dados

 - [Sistema de Informação de Nascidos Vivos](https://datasus.saude.gov.br/transferencia-de-arquivos/) (SINASC/DATASUS), website do ministério da saúde

 - [Banco de Dados de Síndrome Respiratória Aguda Grave](https://opendatasus.saude.gov.br/dataset/bd-srag-2021) - incluindo dados da COVID-19
 
 - SP Contra o Novo Coronavírus (Seade/coronavírus) (https://www.saopaulo.sp.gov.br/coronavirus/)
 -
 - Biblioteca Virtual – São Paulo: população do municípios paulistas (http://www.bibliotecavirtual.sp.gov.br/temas/sao-paulo/sao-paulo-populacao-dos-municipios-paulistas.php)


## Variáveis de interesse  

 - Tamanho da população do estado de São Paulo e dos municípios;
 - Número de casos de COVID-19 no estado e por município de São Paulo;
 - Número de Óbitos no estado e por Município.
 - Dados da mãe:
 - Idade da mãe;
 - Escolaridade;
 - Status marital;
 - Cor de pele/raça;
 - Tipo de parto;

### Integração entre Bases e Análise Exploratória

## Análises Realizadas 

# Qualidade dos dados e Dados faltantes

Durante o processo de Análise Exploratória dos dados, utilizamos como premissa se os dados eram confiáveis e se a base estava limpa. 
Inicialmente já foi possível observar que para cada coluna existiam valores que não eram esperados, ou que eram equivalentes a valores faltantes. Por exemplo, para a coluna ESCMAE o valor 9 representa um valor ignorado, que não foi preenchido. Para a coluna IDADEMAE, o valor de 99 parece ser um erro, já que antes dele o maior valor de idade foi 65. Para a coluna QTDFILVIVO (quantidade de filhos vivos), apesar do número 30 também parecer absurdo, o número 99 também parece ser um erro.
Estes valores foram substituídos por NULL, bem como certo valores estranhos, como o valor de 99 na colunas IDADEMAE (idade da mãe). Para as colunas categóricas, as categorias foram codificadas de 1 até N, sendo N o número de categorias. Desta maneira Valores maiores que N foram transformados em NULL, para que depois pudessem ser descartados durante as análises.

	QTDFILVIVO: valores maiores que 30.
	QTDFILMORT: valores maiores que 30.
	IDADEMAE: valores maiores que 65.
	ESTCIVMAE: valores maiores que 5.
	PARTO: valores maiores que 2.
	IDANOMAL: valores maiores que 2.
	GESTACAO: valores maiores que 6.
	RACACOR: valores maiores que 5.
	RACACORMAE: valores maiores que 5.
	ESCMAE: valores maiores que 5.

Após essas alterações realizamos o cálculo de porcentagem de dados faltantes para cada variável, o maior valor observado estava na variável RACACORMAE que tinha 39% dos dados faltantes, as demais variáveis estavam entre 3 e 0%. Inicialmente optamos por utilizar o método complete-case analysis, que indica dropar os dados faltantes da base. Porém quando começamos a realizar a análise da qualidade dos dados, de afim validar possíveis discrepâncias e inconsistências, percebemos variáveis com valores 9 e 99, que segundo a descrição do dicionário de dados são valores ignorados, por isso substituímos estes valores por nulos.
Para que as demais varáveis não fossem comprometidas, decidimos manter os registros com valores nulos no dataset uma vez que a maioria dos métodos estatísticos em python já desconsideram estes valores.

Outro tratamento realizado nos dados, foi em relação a data. Os valores plotados estavam sem separação, por exemplo a data 24/05/2020 estava com o valor 24052020 no dataset, ou ainda a data 08/02/2020 estava plotada como 8022020. Para resolver esse caso criamos uma função em Python que transforma os valores para a formatação correta. As funções str_to_datetime, nullify criadas no módulo sinasc.py trata deste caso.

Em resumo, observamos um dataset bastante consistente em dados, e com porcentagens muito baixas de erro.


# Estatística e Graficos
Durante as análises estatísticas fizemos plots para ver a progressão do número de nascidos vivos para cada cidade, dos anos de 2010 à 2020. Verificamos, em algumas cidades, uma queda nos anos de 2016/2017. Essa queda pode ter se dado devido à pandemia do Zika vírus, durante a qual houve extensa propaganda para que as mães postergassem a gravidez, entretanto existem cidades em que esse comportamento não é observado. Ao mesmo tempo pode-se ver que tal comportamento não existe para 2020, pelo menos não para o balanço geral do ano.

Como a pandemia se iniciou por volta de março, caso haja alguma diferença no número de nascidos vivos, esperaríamos que ela aparecesse em novembro/dezembro. Ainda assim é necessário levar em consideração o mês do ano, já que certa sazonalidade no número de nascidos vivos.

O arquivos ./assets/AnalysisPrism.pdf mostra os mesmos plots, mas também as tabelas com os números absolutos e médios de nascidos vivos para cada mês, para cada ano. Ele também conta com as barras de desvio padrão para se avaliar a variabilidade destes valores, cidade por cidade.

Ao gerar os plots algumas observações foram geradas:

•	Proporcionalmente, mulheres que tiveram entre 8 e 11 anos de escolaridade são maioria, seguidas das que tiveram 12 ou mais. 
•	Observamos também que para todas as cidades avaliadas, exceto Barueri, a maioria dos bebês tem raça/cor registrada como Branca, seguido pelo pardo.
•	A cidade de São Paulo está pelo menos 1 ordem de grandeza acima das demais cidades. Para algumas cidades já é possível ver certa tendência de crescimento ou decrescimento no número.
•	A proporção de bebês registrados como brancos diminui, enquanto a de pardos e negros/pretos aumenta. O número de bebês registrados como brancos caiu 20 pontos percentuais no período.
•	O número de mães solteiras é muito próximo do número de mae que são casas, tendências que vem desde 2012. De 2017 para 2020 o número de mães registradas como estando em união estável pareceu aumentar.
•	O percentual de mães com mais de 12 anos de escolaridade vem aumentando aos poucos durante o período.
•	A proporção de partos que são feitos por cesárea é consistentemente similar à proporção de partos "normais".
•	O número de nascidos vivos em 2020 chega a ser 10% menor que o mesmo mês no ano anterior. Existe certa dúvida de se esse número seria o esperado para o período, dada a tendência dos anos, ou se esse número possa ser um resultado da pandemia de COVID-19. Esta dúvida é exatamente um dos questionamentos do projeto.
•	A raça/cor amarela (asiática) é a que mais tem mães acima de 35 anos, enquanto a indígena é a que mais tem mães abaixo de 20 anos.



# Paulo Modelos, analises estatística. 



## Ferramentas

### Ferramentas de software
Ferramenta | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Python | https://www.python.org/ | Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Utilizaremos extensivamento bibliotecas como [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [SciPy](https://www.scipy.org/) e [Scikit-learn](https://scikit-learn.org/stable/).
Jupyter Notebook | https://jupyter.org/ | Documento virtual que permite execução de rotinas usuais de programação e documentação de todo o processo de produção do código. No projeto será utilizado para o código de reestruturação da base de dados e para os modelos.
Google Colab | https://colab.research.google.com/ | Similar ao jupyter notebook, o Colab é uma lista de células que podem conter textos explicativos ou códigos executáveis e suas respectivas saídas.
R | https://www.rstudio.com/products/rstudio/download/#download | R é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica, fracamente tipada, voltada à manipulação, análise e visualização de dados. No projeto se utilizou o RStudio como meio de instalação do R.

### Ferramentas estatísticas
O ferramental estatístico utilizado será o apresentado durante as aulas, mais os que os componentes do grupo tiverem conhecimento e julgarem adequados. Como já foi descrito, iremos utilizar:
 - Regressão linear (no número de nascidos vivos).
 - Testes de hipótese (comparação entre os número de nascidos vivos, entre as proporções de nascidos vivos entre subamostras da população, testes de normalidade).
 - Aprendizado de máquina (técnicas de validação de modelos estatísticos, métricas, métodos explicáveis e métodos de [XAI](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence)).

# Resultados 
## Análise estatística.

A tabela abaixo resume o p-value anova para as cidades do ranking levando em consideração as estratificações definidas na modelagem.
Devido a dificuldade que encontramos para escolher um teste que se adequasse corretamente ao conjunto de dados, não conseguimos afirmar que o valor alto de p-value se refere a não negativa da hipótese nula ou se o resultado que se deu é devido a não adequação do teste ao conjunto de dados, porém ano analisar os dados através do gráficos e valores absolutos, observamos uma tendência de não rejeição da hipótese nula, não conseguimos identificar diferença entre os meses com e sem pandemia. 




| Cidade               | Brancos             | Não Brancos         |Até 7 anos de estudos|8 ou mais anos de estudos|Casada ou união estável|Solteira|A1     |A2     |A3|
| ---------------------| ------------------- | ------------------- | ------------------- |------------------------ |---------------------- |--------|-------|-----  |-----|
| Andradina            |  0.9348827514154132 | 0.17513080603908623 |0.04463085084860029  |0.5563699040316381       |0.4173882295531922     |0.17390938991860963|0.01069319940495801|0.7465306852325151|0.09651183439707238|
| Araçatuba            |0.6415888520718181|0.22667186160129166|0.07300371075550745|0.22330008513509036|0.9501226225546695|0.782918933672756|0.10313674412159318|0.8997025974823041|0.10703998647836391|
| Barueri              |0.3044513700445403|0.22111266328049684|0.04869239516627025|0.6355534071454625|0.3771867388024749|0.16956001837706222|0.015049475878195894|0.09588655925498574|0.35502898650621106|
| São Paulo            |0.9592703692450071|0.22369263962766847|0.09651717145315583|0.898503911622669|0.5741764992686036|0.10202734063378571|0.022574204103810943|0.013349831854615071|0.12545464295695066|
| Dracena              |0.6436491753251021|0.23357831808524507|0.03128676166492906|0.957264823839042|0.08051030418149387|0.13507637866578293|0.025406299687495956|0.415867669527038|0.12742786976771722|
| Guaíra               |0.9177353289298512|0.18649112624658404|0.1443583685289298|0.9543220144116332|0.8685382013239737|0.5250873607338962|0.016365713074422316|0.40544023304473664|0.2120467554031652|
| Jales                |0.46046695977722973|0.16288490449431692|0.057893547203380955|0.06587109369620811|0.1716469158184669|0.19415651763043026|0.00991052353725434|0.2691628094501288|0.019995111243597118|
| Santa Isabel         |0.7473338512707313|0.196446914811358|0.13973972416514244|0.83538051556331|0.3975422123889091|0.1639656852364353|0.01608256134909194|0.4095507642089896|0.0881615795674582|
| São Caetano do Sul   |0.4547108251534536|0.30886801842576805|0.0857526541567079|0.20017939238577281|0.22099725927055833|0.0856758742318781|0.010723327568025765|0.4887934026588501|0.08435094966870903|
| Santos               |0.5984503220252172|0.30997439343148586|0.1456983918285436|0.9908743161471665|0.5244430259057227|0.22940335798434358|0.14787876716911072|0.11056668576594232|0.08585957689119841|
| São José do Rio Preto|0.90546242355215|0.3453579222208589|0.08634419528026813|0.1079691244853812|0.14295300581063103|0.12494951515613205|0.00973959203277352|0.1243001841960537|0.05073157498192731|

# Discussão - Falta

# Conclusão - Falta

# Trabalhos Futuros 

A monitoria em tempo real dos impactos de eventos catastrófico na saúde e bem-estar da população afetada deve ser abordada de uma forma multifacetada. Por exemplo, o desenho e implementação de ferramentas de inteligência artificial através de modelagem matemática/ machine learning é fundamental para a monitoria em tempo real dos indicadores de saúde, principalmente dos grupos mais vulneráveis. A existência de dados/informações atempada e a possibilidade de obter predições acuradas desses indicadores possibilita a implementação e adequação de estratégias e políticas de saúde de acordo com a dinâmicas dos eventos catastróficos. 
Estamos cintes que o modelo predictor desenvolvido carecem de aprimoramento, por pretendemos, nos próximos trabalhos, avaliar outas potencias variáveis predictoras como a taxa de fecundidade, o índice de desenvolvimento humano, a taxa de uso de contraceptivos moderno durante a fase aguda dos eventos catastróficos etc. que possam melhorar a capacidade preditora do modelo.  

# Referências Bibliográficas 
1. Chen N, Zhou M, Dong X,  et al. Epidemiological and clinical characteristics of 99 cases of 2019 novel coronavirus pneumonia in Wuhan, China: a descriptive study. Lancet 2020;395:507-13.
2. Dong E, Du H, Gardner L. An interactive web-based dashboard to track COVID-19 in real time. Lancet Infect Dis 2020;20:533-4.
3. Nogueira J, Rocha DG, Akerman M. Políticas públicas adoptadas en la pandemia de la COVID-19 en tres países de América Latina: contribuciones de la Promoción de la Salud para no volver al mundo que existía. Global health Promotion 2020. Doi: https://doi.org/10.1177/1757975920977837
4. Rocha R, Atun R, Massuda A, et al. Effect of socioeconomic inequalities and vulnerabilities on health-system preparedness and response to COVID-19 in Brazil: a comprehensive analysis. Lancet Glob Health 2021:S2214-109X(21)00081-4.
5. Castro MC, Massuda A, Almeida G,  et al. Brazil's unified health system: the first 30 years and prospects for the future. Lancet 2019;394:345-56.
6. Charles CM, Amoah EM,  Kourouma KR,  et al. The SARS-CoV-2 pandemic scenario in Africa: What should be done to address the needs of pregnant women? Int J Gynaecol Obstet 2020;151:468-70.
7. World Health Organization. Pulse survey on continuity of essential health services during the COVID-19 pandemic: interim report, 27 August 2020. Geneva2020. Available at: https://www.who.int/publications/i/item/WHO-2019-nCoV-EHS_continuity-survey-2020.1.
8. WHO, UNICEF and UNFPA. Maternal mortality: Levels and trends 2000 to 2017. Geneva 2019. Avalible at: https://www.who.int/reproductivehealth/publications/maternal-mortality-2000-2017/en/.
9. Schaaf M, Boydell V, Belle SV, Brinkerhoff DW, George A. Accountability for SRHR in the context of the COVID-19 pandemic. Sex Reprod Health Matters 2020;28:1779634


## Tarefas 

### Realizadas
 - [x] Calcularemos a incidência da COVID-19 no estado e por Município;
 - [x] Estimaremos a taxa de mortalidade e letalidade da COVID-19 no estado e no Município.

Tendo os dados:
 - [x] Com o auxílio a linguagem Python podemos estabelecer um ranking dos municípios com base nos seguintes indicadores (incidência, taxa de mortalidade e letalidade da COVID-19)
 - [x] Checar quais os municípios com piores indicadores.

Tendo o ranking dos municípios:
 - [x] Podemos escolher os municípios com pior classificação (top 11), mais a capital (São Paulo); 
 - [x] Em seguida iremos extrair dados de número de nascidos vivos (mês/mês) no geral (para os 11 municípios) e;
 - [x] Obter as variáveis de interesse do DATASUS.

Com os dados obtidos:
 - [x] Realizar pré-processamento e limpeza dos dados.
    - [x] Verificação dos tipos das colunas, e se os valores são os esperados de acordo com o [dicionário de dados](./documents/Dicionario_de_Dados_SINASC.docx);
    - [x] *Parsing* das colunas (transformação de tipo, leitura de strings para inteiros, tipos de datas, etc);
    - [x] Análise de valores faltantes;
    - [x] Limpeza (remover valores absurdos).

Para a primeira entrega:
 - [x] Definição das perguntas de pesquisa;
 - [x] Definição da metodologia;
 - [x] Criação do repositório no GitHub.
 - [x] Documentação inicial, cronograma, verificação de banco de dados;

Para a segunda entrega:
 - EDA com:
    - [x] Plots das progressões do número de nascidos vivos durante os anos;
    - [x] Plots com os número de nascidos vivos, estratificados pelas variáveis categóricas do dataset;
    - [x] Correlação entre as variáveis numéricas do dataset.

### Previstas

 - [ ] Modelagem do número de nascidos vivos, com caráter preditivo.
    - [ ] Análise do impacto das variáveis de entrada na predição do modelo;
    - [ ] Verificação de se a modelagem muda para subamostras da população (apenas mulheres negras, ou apenas para alguma faixa etária, por exemplo);
    - [ ] Criação de modelos por cidade avaliada.
 - [ ] Verificação, por cidade, do impacto da pandemia do COVID-19 por cidade avaliada.


# Cronograma

## Previsto
|                                     Mês | Março |   |   |   | Abril |   |   |   | Maio |   |   |   | Junho |   |   |   | Julho |
|----------------------------------------:|-------|---|---|---|-------|---|---|---|------|---|---|---|-------|---|---|---|-------|
|                                  Semana | 1     | 2 | 3 | 4 | 1     | 2 | 3 | 4 | 1    | 2 | 3 | 4 | 1     | 2 | 3 | 4 | 1     |
| Definir o escopo da Pesquisa            |       |   |   | x | x     |   |   |   |      |   |   |   |       |   |   |   |       |
| Seleção de dados                        |       |   |   |   | x     | x | x |   |      |   |   |   |       |   |   |   |       |
| Pré-processamento dos dados             |       |   |   |   |       |   |   | x | x    |   |   |   |       |   |   |   |       |
| Processamento e transformação dos dados |       |   |   |   |       |   |   |   | x    | x |   |   |       |   |   |   |       |
| Data Mining                             |       |   |   |   |       |   |   |   |      | x | x | x | x     |   |   |   |       |
| Criação de modelos                      |       |   |   |   |       |   |   |   |      | x | x | x | x     |   |   |   |       |
| Análise estatística                     |       |   |   |   |       |   |   |   |      | x | x | x | x     |   |   |   |       |
| Avaliação dos modelos                   |       |   |   |   |       |   |   |   |      |   | x | x | x     | x | x | x |       |
| Documentação                            |       |   |   | x | x     | x | x | x | x    | x | x | x | x     | x | x | x | x     |
| Apresentação de resultados              |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   | x | x     |

# Real
|                                     Mês | Março |   |   |   | Abril |   |   |   | Maio |   |   |   | Junho |   |   |   | Julho |
|----------------------------------------:|-------|---|---|---|-------|---|---|---|------|---|---|---|-------|---|---|---|-------|
|                                  Semana | 1     | 2 | 3 | 4 | 1     | 2 | 3 | 4 | 1    | 2 | 3 | 4 | 1     | 2 | 3 | 4 | 1     |
| Definir o escopo da Pesquisa            |       |   |   | x | x     | x | x |   |      |   |   |   |       |   |   |   |       |
| Seleção de dados                        |       |   |   |   |       |   |   | x | x    |   |   |   |       |   |   |   |       |
| Pré-processamento dos dados             |       |   |   |   |       |   |   |   | x    | x | x |   |       |   |   |   |       |
| Processamento e transformação dos dados |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   |   |       |
| Data Mining                             |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   |   |       |
| Criação de modelos                      |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   |   |       |
| Análise estatística                     |       |   |   |   |       |   |   |   |      |   | x |   |       |   |   |   |       |
| Avaliação dos modelos                   |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   |   |       |
| Documentação                            |       |   |   | x | x     | x | x | x | x    | x | x |   |       |   |   |   |       |
| Apresentação de resultados              |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   |   |       |


