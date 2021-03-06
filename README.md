# Projeto `Impacto da pandemia da COVID-19 no número de nascidos vivos do Estado de São Paulo.`

## Project `Impact of the COVID-19 pandemic on the number of live births in the State of São Paulo`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2021, na Unicamp.


|Nome  | RA | Especialização|
|--|--|--|
| Charles M'poca Charles | 163383 | Saúde|
| Silvia Arantes Pereira Olivio | 224932  | Computação|
| Débora Rocha Helfstein  | 234934  | Farmacêutica|
| Paulo Augusto Alves Luz Viana | 263889 | Elétrica |

Você pode rodar o notebook com todas as análises atráves deste [Jupyter notebook no Google Colab!](https://colab.research.google.com/github/Kotzly/DS4H_Course/blob/v2.0/notebooks/DS4H_full.ipynb).

## Descrição Resumida do Projeto
Introdução: A pandemia da COVID-19 causada pelo vírus SARS_COV_2 tem tomado proporções alarmantes ao nível mundial. Atualmente (12/04/2021), ao nível global foram notificados cerca de 136,181,468, sendo o Brasil um dos países mais afetado pela pandemia, com aproximadamente 2,938,804 caso notificados. A pandemia tem afetado a população no geral sem distinção do sexo, raça, e estrato social com grande impacto no sistema de saúde. De entre os efeitos da pandemia no sistema de saúde, destacam-se a interrupção ou redução de provisão dos serviços de saúde materna e perinatal que podem influenciar negativamente nos seus indicadores, como é o caso do número de nascidos vivos. Objetivo: o presente estudo tem o objetivo de avaliar o impacto da pandemia da COVID-19 no número de nascidos vivos nos municípios do estado de São Paulo. Metodologia: será realizado uma análise de serie temporal, baseada em dados Sistema de Informações de Nascidos Vivos (SINASC/DATASUS) e do Banco de Dados de Síndrome Respiratória Aguda Grave (SRAG 2021), com o auxílio de métodos estatísticos  e de ferramentas inteligência artificial (métodos de aprendizado de maquinas) - Google Colab e  Jupyter Notebook - realizaremos a modelagem, análise da curva de nascimentos vivos nos últimos 10 anos prévios a pandemia e a predição do número de nascidos vivos esperados para o ano 2020.  Resultados esperados: através desta pesquisa esperamos obter os padrões das curvas de nascidos vivos e estabelecer uma correlação entre a pandemia e o indicador de saúde materna e perinatal para os diferentes municípios do estado de São Paulo.

## Abstract
Introduction: The COVID-19 pandemic caused by the SARS_COV_2 virus has reached alarming proportions worldwide. As of 21rst June 2021, 178,553,726 COVID-19 cases have been reported worldwide, Brazil being one of the most affected countries, with approximately 17,927,928 reported cases. The pandemic has affected the non-general population regardless of sex, race, and social strata, with a great impact on the health system. Among the effects of the pandemic on the health system, a significant disruption (interruption or reduction) in the provision of maternal and perinatal health services stand out.  The disruption of the sexual and reproductive health might have a significant negative impact on maternal and neonatal outcomes, such as the number of live births, preterm birth, and stillbirth and so on. Objective: This study aims was to assess the impact of the COVID-19 pandemic on the number of live births in the cities of the state of Sao Paulo. Methodology: a data-driven time series analysis (ecological study) was carried out, based on data from the Live Birth Information System (SINASC / DATASUS) and the Severe Acute Respiratory Syndrome Database (SRAG 2021). Using an artificial tools ( machine learning methods) - Google Colab and Jupyter Notebook - We conducted a statistical analysis based on  modelling, analysis of the curve of live births in the last 10 years prior to the pandemic and the prediction of the number of live births expected for the year 2020. Expected results: Through this research, we hope to obtain the patterns of the live birth curves and establish a correlation between the pandemic and the maternal and perinatal health indicator for the different municipalities of Sao Paulo state.

## Videos do Projeto

### Vídeo da Proposta

Por favor, assista ao [vídeo](https://drive.google.com/file/d/1xz9lfkAAQFm5fQf4hEIceaY8FeVvwFCI/view?usp=sharing) de apresentação do projeto. 

### Vídeo da Apresentação Final

Assista o [**vídeo de Apresentação Final do projeto**](https://drive.google.com/file/d/1zpTE-o8FtsIkw8usp5e2mev-2MuZLujn/view?usp=sharing).

## Slides do Projeto


- [Slides da Proposta](./assets/powerpoint/ApresentaçãoGrupo.pptx)

- [**Apresentação para Entrega Final**](./assets/powerpoint/ApresentaçãoFinal.pptx)


## Estrutura de arquivos e pastas

```
├───assets                               <- Arquivos relacionados ao projeto.
├───data                                 <- Dados utilizados no projeto.
│   ├───external
│   └───processed
├───documents                            <- Documentos relacionados ao projeto e aos dados.
├───media                                <- Arquivos de mídia
│   ├───images
│   └───powerpoint
├───notebooks                            <- Notebooks jupyter utilizados no projeto.
└───src                                  <- Código fonte do projeto.
    ├───ds4h                             <- Pacote python instalável.                         
    │   ├───analysis
    │   ├───data
    │   ├───modelling
    │   ├───processing
    │   ├───scripts
    │   └───visualization
    └───orange
   
```

## Introdução e Referenciais de Teóricos 
A pandemia da COVID-19 causada pelo vírus SARS_COV_2 tem tomado proporções alarmantes ao nível mundial (1). Atualmente (21/06/2021), ao nível global foram notificados cerca de 178.553.726, sendo o Brasil um dos países mais afetado pela pandemia, com aproximadamente 17,927,928 caso notificados (2). A pandemia tem afetado a população no geral sem distinção do sexo, raça, e estrato social com grande impacto no sistema de saúde.
A implementação das medidas de mitigação da pandemia tais como a imposição de medidas restritivas para circulação de pessoas, encerramento de escolas e de atividade consideradas não essenciais, em locais onde são implementadas adequadamente, tem contribuído para a redução dos casos de infeção (3). 
No Brasil, apesar da existência de um sistema de saúde robusto, a implementação de medidas político administrativas contraproducentes para a mitigação dos feitos da pandemia e a redução do financiamento do sistema público de saúde, Sistema Único de Saúde (SUS), tem contribuído para os efeitos devastadores da pandemia no país (4,5). 
Os diversos sistemas de saúde, foram severamente afetados pela pandemia da COVID-19, e os efeitos foram mais significativos nos países de baixa e média renda, onde os recursos humanos, infraestruturas e o sistema de saúde são escassos e frágeis (6). Para reverter os efeitos da pandemia, os sistemas de saúde foram reorganizados a diferentes níveis, com redirecionamento de recursos humanos e infraestruturas para o enfretamento da pandemia (6).  
De entre os efeitos da pandemia no sistema de saúde, destacam-se a interrupção ou redução de provisão dos serviços de saúde materna e perinatal. Dados da literatura, indicam que ao nível mundial, os serviços de saúde sexual e reprodutiva, foram os mais severamente afetados.  Por exemplo, os dados do inquérito realizado pela Organização Mundial da Saúde (OMS) em 105 países, de diferentes regiões e continentes, sugerem que no início da pandemia provocou a redução ou interrupção do provimento dos serviços de saúde sexual e reprodutiva em mais de 50% dos países participantes (cerca de 68% dos serviços de planejamento familiar e 56% das consulta pré-natal) (7). 
A redução ou interrupção destes serviços essenciais violam os princípios fundamentais dos direitos humanos. Adicionalmente, colocam em perigo a saúde materna e perinatal com aumento considerável da incidência de gravidez não planejada, abortos inseguros, óbitos fetais morbidade e mortalidade materna, comprometendo deste modo os ganhos alcançados nas últimas duas décadas na área de saúde e os objetivos de desenvolvimento sustentável, agenda 2030 (8,9). 
Deste modo, o número de nascidos vivos pode ser um indicador chave para mensuração dos impactos da pandemia na saúde materna e perinatal. 



## Perguntas de Pesquisa
 - Qual foi o impacto da pandemia da COVID-19 na taxa de nascidos vivos no Estado de São Paulo?
 - É possível prever a taxa de nascidos vivos nos meses de pandemia utilizando os dados dos anos anteriores?

# Objetivos do Projeto 
> Avaliar o impacto da pandemia da COVID-19 no número de nascidos vivos nos municípios do estado de São Paulo
> Desenhar modelos predictores de números de nascidos vivos com base em modelos matemáticos/machine learning. 

# Metodologia
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

## Modelagem
Para a modelagem, utilizou-se um modelo linear baseado em recorrências. Uma amostra é o número de nascidos vivos em um mês de um determinado ano. O modelo é:
    ![model image](./assets/images/model.jpg)

    \hat{Y}_{year, month} = \sum _{i=1}^{N_{years}}  \left ( w^Y_i * Y_{year-i, month} \right ) + \sum _{i=1}^{N_{months}}  \left (  w^M_i * Y_{year, month-i} \right ) + \left ( w^T*(year - 2000) \right ) + \theta_{month} + \theta 

Onde w^Y_i e w^M_i são os parametros da recorrência dos anos anterioes e dos meses anterioes, respectivamente, w^Y é o parâmetro de tendência, \theta_{month} é um parâmetro relativo ao mês *month*, e \theta é o *intercept* do modelo.

Para que a equação acima faça sentido, temos as equivalências:
 - Y_{2020, -1} = Y{2019, 11}
 - Y_{2020, -2} = Y{2019, 10}
 - ...

Este modelo foi utilizado por utilizar duas recorrências interessantes, no mês e no ano. A recorrência nos valores do número de nascidos vivos dos meses anteriores faz com que o modelo capture características recentes do comportamento da série temporal, enquanto que a recorrência no número dos anos anteriores, para o mesmo mês, faz com que o modelo capture o comportamento daquele  mês especifico, para os anos anteriores (já que foi notado certa sazonalidade no número de nascidos vivos nos meses do ano). O parâmetro \theta_{month} também controlará o valor predito para cada mês especifico. O parâmetro *w^T* controla a tendência do número de nascidos vivos (e.g., se há uma tendência de decrescimento do número de nascidos vivos, todo mês, espera-se que *w^T* seja negativo). Por fim, \theta é o equivalente ao *intercept* desta modelagem.


Serão utilizados dois conjuntos treino:
    - O primeiro utilizará todos os anos e meses que temos dados, menos os anos do zika-vírus (2016/2017) e do corona vírus (segundo semestre de 2020) para o treino. O objetivo aqui é verificar como o modelo se sai sem a informação de um ano "anômalo", onde conhecidamente houve decréscimo no número de nascidos vivos devido à uma pandemia. Este será o chamado 'Fold 0';
    - O segundo conjunto utilizará todos os anos, menos o segundo semestre de 2020. Este será o chamado 'Fold 1';

Em ambos os casos, o conjunto de teste será o segundo semestre de 2020. Utilizaremos apenas o segundo semestre pois espera-se que haja um intervalo de pelo menos 8 meses desde o advento (começo do corona vírus) até vermos o impacto no número de nascidos vivos, devido ao número de meses que leva da concepção até o parto.

Será criado um modelo para cada cidade, pois foi visto na análise exploratória que cada cidade tem comportamentos diferentes de tendência entre os anos e de sazonalidade entre os meses. A análise de resultados será feita utilizando-se a hipótese de que se houve um bom ajuste de parâmetros no treino, este modelo representa bem os dados de treinos, e caso o modelo performe mal no teste, há a possibilidade de que os dados de teste realmente estão diferentes dos dados de treino, portanto houve certa diferença no número de nascidos vivos do teste.

Nas discussões sobre os resultados, nos referimos à um resultado como sendo "bom" quando ele apresenta mais que 50% de R² e menos de 20% de MAPE. Para o modelo ser considerado "bom" no teste utilizamos a regra do MAPE ter que estar abaixo de 10%, apenas. Esses valores foram escolhidos pois o R2 penaliza muito quando, apesar do resultado absoluto não estar muito diferente, o comportamento da curva está diferente, o que até faz sentido para verificar o ajuste do modelo, entretanto para o teste o que faz mais sentido é o valor absoluto do erro, neste caso o valor percentual. Primariamente se analisou os resultados no Fold 1, já que é o fold com mais dados de treinamento, mas também se tirou conclusões sobre o Fold 0.

Será criado um modelo, com a mesma estrutura apresentada, para cada cidade. Também serão realizados experimentos onde se selecionará apenas o número de nascidos vivos para certa parcela da população:
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

Esta divisão é realizada para se verificar se a diferença ou não-diferença entre o número de nascidos vivos durante a pandemia de COVID-19 tem diferença ao se separar estas variáveis.

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
 - Biblioteca Virtual – São Paulo: população do municípios paulistas (http://www.bibliotecavirtual.sp.gov.br/temas/sao-paulo/sao-paulo-populacao-dos-municipios-paulistas.php)


### Variáveis de interesse  

 - Tamanho da população do estado de São Paulo e dos municípios;
 - Número de casos de COVID-19 no estado e por município de São Paulo;
 - Número de Óbitos no estado e por Município.
 - Dados da mãe:
 - Idade da mãe;
 - Escolaridade;
 - Status marital;
 - Cor de pele/raça;
 - Tipo de parto;

## Integração entre Bases e Análise Exploratória

Por favor, veja o notebook com o código do Projeto para ver como as bases foram integradas, e para ver o EDA realizado neste projeto.

## Análises Realizadas 

### Qualidade dos dados e Dados faltantes

Durante o processo de Análise Exploratória dos dados, utilizamos como premissa se os dados eram confiáveis e se a base estava limpa. 
Inicialmente já foi possível observar que para cada coluna existiam valores que não eram esperados, ou que eram equivalentes a valores faltantes. Por exemplo, para a coluna ESCMAE o valor 9 representa um valor ignorado, que não foi preenchido. Para a coluna IDADEMAE, o valor de 99 parece ser um erro, já que antes dele o maior valor de idade foi 65. Para a coluna QTDFILVIVO (quantidade de filhos vivos), apesar do número 30 também parecer absurdo, o número 99 também parece ser um erro.
Estes valores foram substituídos por NULL, bem como certo valores estranhos, como o valor de 99 na colunas IDADEMAE (idade da mãe). Para as colunas categóricas, as categorias foram codificadas de 1 até N, sendo N o número de categorias. Desta maneira Valores maiores que N foram transformados em NULL, para que depois pudessem ser descartados durante as análises.

 - QTDFILVIVO: valores maiores que 30.
 - QTDFILMORT: valores maiores que 30.
 - IDADEMAE: valores maiores que 65.
 - ESTCIVMAE: valores maiores que 5.
 - PARTO: valores maiores que 2.
 - IDANOMAL: valores maiores que 2.
 - GESTACAO: valores maiores que 6.
 - RACACOR: valores maiores que 5.
 - RACACORMAE: valores maiores que 5.
 - ESCMAE: valores maiores que 5.

Após essas alterações realizamos o cálculo de porcentagem de dados faltantes para cada variável, o maior valor observado estava na variável RACACORMAE que tinha 39% dos dados faltantes, as demais variáveis estavam entre 6 e 0%. Inicialmente optamos por utilizar o método complete-case analysis, que indica dropar os dados faltantes da base. Porém quando começamos a realizar a análise da qualidade dos dados, de afim validar possíveis discrepâncias e inconsistências, percebemos variáveis com valores 9 e 99, que segundo a descrição do dicionário de dados são valores ignorados, por isso substituímos estes valores por nulos.
Para que as demais varáveis não fossem comprometidas, decidimos manter os registros com valores nulos no dataset uma vez que a maioria dos métodos estatísticos em python já desconsideram estes valores.

Outro tratamento realizado nos dados, foi em relação a data. Os valores plotados estavam sem separação, por exemplo a data 24/05/2020 estava com o valor 24052020 no dataset, ou ainda a data 08/02/2020 estava plotada como 8022020. Para resolver esse caso criamos uma função em Python que transforma os valores para a formatação correta. As funções str_to_datetime, nullify criadas no módulo sinasc.py trata deste caso.

Em resumo, observamos um dataset bastante consistente em dados, e com porcentagens muito baixas de erro.


### Estatística e Graficos
Durante as análises estatísticas fizemos plots para ver a progressão do número de nascidos vivos para cada cidade, dos anos de 2010 à 2020. Verificamos, em algumas cidades, uma queda nos anos de 2016/2017. Essa queda pode ter se dado devido à pandemia do Zika vírus, durante a qual houve extensa propaganda para que as mães postergassem a gravidez, entretanto existem cidades em que esse comportamento não é observado. Ao mesmo tempo pode-se ver que tal comportamento não existe para 2020, pelo menos não para o balanço geral do ano.

Como a pandemia se iniciou por volta de março, caso haja alguma diferença no número de nascidos vivos, esperaríamos que ela aparecesse em novembro/dezembro. Ainda assim é necessário levar em consideração o mês do ano, já que certa sazonalidade no número de nascidos vivos.

O arquivos ./assets/AnalysisPrism.pdf mostra os mesmos plots, mas também as tabelas com os números absolutos e médios de nascidos vivos para cada mês, para cada ano. Ele também conta com as barras de desvio padrão para se avaliar a variabilidade destes valores, cidade por cidade.

Ao gerar os plots algumas observações foram geradas:

 - Proporcionalmente, mulheres que tiveram entre 8 e 11 anos de escolaridade são maioria, seguidas das que tiveram 12 ou mais. 

 - Observamos também que para todas as cidades avaliadas, exceto Barueri, a maioria dos bebês tem raça/cor registrada como Branca, seguido pelo pardo.

 - A cidade de São Paulo está pelo menos 1 ordem de grandeza acima das demais cidades. Para algumas cidades já é possível ver certa tendência de crescimento ou decrescimento no número.

 - A proporção de bebês registrados como brancos diminui, enquanto a de pardos e negros/pretos aumenta. O número de bebês registrados como brancos caiu 20 pontos percentuais no período.

 - O número de mães solteiras é muito próximo do número de mae que são casas, tendências que vem desde 2012. De 2017 para 2020 o número de mães registradas como estando em união estável pareceu aumentar.

 - O percentual de mães com mais de 12 anos de escolaridade vem aumentando aos poucos durante o período.

 - A proporção de partos que são feitos por cesárea é consistentemente similar à proporção de partos "normais".

 - O número de nascidos vivos em 2020 chega a ser 10% menor que o mesmo mês no ano anterior. Existe certa dúvida de se esse número seria o esperado para o período, dada a tendência dos anos, ou se esse número possa ser um resultado da pandemia de COVID-19. Esta dúvida é exatamente um dos questionamentos do projeto.

 - A raça/cor amarela (asiática) é a que mais tem mães acima de 35 anos, enquanto a indígena é a que mais tem mães abaixo de 20 anos.

### Modelagem do número de nascidos vivos

A estrutura do modelo utilizado foi encontrada empiricamente. Discutimos que realmente seria interessante termos uma recorrência nos meses anteriores ao mês de predição, mas dificilmente este modelo era satisfatoriamente ajustado no treino (as métricas ficavam ruins). Ao se relembrar como a maioria das cidades apresenta certa sazonalidade no número de nascidos vivos, ou seja, a curva de todos os anos apresenta um "formato" parecido, pareceu-se interessante utilizar também componentes da recorrência com valores do mesmo mês, mas para anos anteriores.

Esta modelagem melhorou os resultados, isto é, mais modelos tiverem resultados satisfatórios no treino e alguns começaram a generalizar para o teste. Após isto, verificou-se que certas cidade tem crescimentos ou decrescimentos dos números mensais e anuais de nascidos vivos constante, então se adicionou um parâmetro ao próprio valor do ano. O esperado é que, se, por exemplo, todo ano em média o número de nascidos vivos de uma cidade cair em 100, o parâmetro que multiplica o ano (wT) no modelo seja -100/12, ou algo próximo a isso. Também adicionou-se um parâmetro fixo por mês, que esperava-se que capture-se também o comportamente sazonal do número de nascidos vivos. 

Com isto houve um número razoável de cidades que estavam sendo bem ajustadas ao treino, e que ainda conseguiam generalizar no teste. Para evitar um viés de escolha (remodelar o problema até termos bons resultados de teste), o ideal seria termos um conjunto de validação, onde validaríamos os nossos modelos, para no final termos o resultado no teste, mas como nosso objetivo de previsão era exatamente os 6 meses de pandemia e como temos 1 amostra por mês, seria impraticável diminuir ainda mais o conjunto de teste para separá-lo em validação (separar um pedaço do treino em validação seria inútil, já que o objetivo do modelo é predizer o número de NV durante a pandemia). Como isso não foi feito, tomou-se o cuidado de se passar por poucas rodadas de melhora do modelo, mas ainda é altamente provável que haja um viés ou estocasticidade de performance do modelo (o modelo funciona bem para uma cidade por "sorte", e não porque representa bem a realidade).

Entretanto, considera-se a análise feita completamente válida, já que o modelo utilizado é relativamente simples, o que daria menos chance de ocorrer o overfitting do modelo, mas também não é tão simples (dado o número de amostras), o que também diminui a chance dele ir bem no teste por "sorte". Na seção de Discussão mostraremos como a análise feita se traduz para os valores reais utilizando também um pouco de visualização dos números por mês.

## Ferramentas

### Ferramentas de software
Ferramenta | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Python | https://www.python.org/ | Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Utilizaremos extensivamento bibliotecas como [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [SciPy](https://www.scipy.org/) e [Scikit-learn](https://scikit-learn.org/stable/).
Jupyter Notebook | https://jupyter.org/ | Documento virtual que permite execução de rotinas usuais de programação e documentação de todo o processo de produção do código. No projeto será utilizado para o código de reestruturação da base de dados e para os modelos.
Google Colab | https://colab.research.google.com/ | Similar ao jupyter notebook, o Colab é uma lista de células que podem conter textos explicativos ou códigos executáveis e suas respectivas saídas.
R | https://www.rstudio.com/products/rstudio/download/#download | R é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica, fracamente tipada, voltada à manipulação, análise e visualização de dados. No projeto se utilizou o RStudio como meio de instalação do R.
Orange | https://orangedatamining.com/ | Orange é uma toolbox voltada para data mining, aprendizado de máquina e visualização. Nele é possível criar workflows de análises de dados, de processamento e visualizações.

### Ferramentas estatísticas
O ferramental estatístico utilizado será o apresentado durante as aulas, mais os que os componentes do grupo tiverem conhecimento e julgarem adequados. Como já foi descrito, iremos utilizar:
 - Regressão linear (no número de nascidos vivos).
 - Testes de hipótese (comparação entre os número de nascidos vivos, entre as proporções de nascidos vivos entre subamostras da população, testes de normalidade).
 - Aprendizado de máquina (técnicas de validação de modelos estatísticos, métricas, métodos explicáveis (https://en.wikipedia.org/wiki/Explainable_artificial_intelligence)).

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




## Modelos

Na análise dos modelos criados se utilizou duas métricas avaliação, o R² e o MAPE (*Mean absolute percentage error*). A escolha do MAPE foi feita para se poder comparar diferentes cidades na mesma escala, o que não poderia ser feito com o MSE ou o MAE, por exemplo.

### Sem estratificação

Aqui não houve filtragem do dataset por nenhuma variável demográfica. Esta modelagem é interessante para verificar como o modelo se comporta para a população como um todo.
Pode-se ver que as cidades de Santos e São Paulo tiverem as melhores métricas de R2 no teste, e São José do Rio Preto e Araçatuba tiveram boas métricas de MAPE. Indicando que para estas 4 cidades o comportamento do segundo semestre de 2020 foi semelhante aos anos anteriores.
Também percebe-se que apenas para São Caetano houve diferença do treino para o teste, indicando diferença do segundo semestre de 2020 para os anos anteriores. Para Araçatuba, Barueri, São Paulo, Jales, Santos e São José do Rio Preto não foi detectada mudança entre os períodos. Para o restante, a análise foi inconclusiva.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                      0.459  |                         0.109 |                     -0.414 |                        0.141 |                       0.445 |                         0.11  |                     -0.857 |                        0.164 |
|  1 | Araçatuba             |                       0.591 |                         0.057 |                      0.454 |                        0.035 |                       0.576 |                         0.06  |                      0.247 |                        0.045 |
|  2 | Barueri               |                       0.839 |                         0.047 |                      0.377 |                        0.084 |                       0.832 |                         0.047 |                      0.329 |                        0.086 |
|  3 | São Paulo             |                       0.915 |                         0.018 |                      0.613 |                        0.018 |                       0.898 |                         0.018 |                      0.529 |                        0.019 |
|  4 | Dracena               |                       0.404 |                         0.133 |                     -0.371 |                        0.074 |                       0.414 |                         0.138 |                     -0.796 |                        0.089 |
|  5 | Guaíra                |                       0.386 |                         0.147 |                     -0.73  |                        0.187 |                       0.397 |                         0.139 |                     -0.834 |                        0.185 |
|  6 | Jales                 |                       0.626 |                         0.082 |                      0.156 |                        0.064 |                       0.583 |                         0.086 |                     -0.083 |                        0.07  |
|  7 | Santa Isabel          |                       0.408 |                         0.112 |                     -0.382 |                        0.162 |                       0.389 |                         0.113 |                     -0.736 |                        0.181 |
|  8 | Santos                |                       0.849 |                         0.036 |                      0.802 |                        0.038 |                       0.837 |                         0.036 |                      0.783 |                        0.036 |
|  9 | São Caetano do Sul    |                       0.734 |                         0.093 |                      0.027 |                        0.175 |                       0.703 |                         0.093 |                     -0.117 |                        0.187 |
| 10 | São José do Rio Preto |                       0.898 |                         0.035 |                      0.236 |                        0.027 |                       0.89  |                         0.036 |                      0.134 |                        0.03  |
| 11 | Todas cidades         |                       0.915 |                         0.018 |                      0.816 |                        0.013 |                       0.899 |                         0.018 |                      0.785 |                        0.014 |

### RACACOR = White

No resultado apenas para as mães auto-declaradas brancas, foi identificado que houve mudança para Santa Isabel e São Caetano do Sul. Para Guaíra e Jales os resultados foram inconclusivos, e para o restante das cidades não foi apontada mudança no número de nascidos vivos.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.532 |                         0.124 |                     -1.758 |                        0.071 |                       0.505 |                         0.129 |                     -2.026 |                        0.079 |
|  1 | Araçatuba             |                       0.732 |                         0.079 |                      0.592 |                        0.058 |                       0.729 |                         0.083 |                      0.569 |                        0.062 |
|  2 | Barueri               |                       0.906 |                         0.1   |                      0.182 |                        0.099 |                       0.889 |                         0.097 |                      0.122 |                        0.1   |
|  3 | São Paulo             |                       0.966 |                         0.024 |                      0.173 |                        0.028 |                       0.961 |                         0.025 |                     -0.029 |                        0.03  |
|  4 | Dracena               |                       0.528 |                         0.167 |                     -1.836 |                        0.071 |                       0.547 |                         0.176 |                     -2.966 |                        0.09  |
|  5 | Guaíra                |                       0.369 |                         0.19  |                     -0.027 |                        0.19  |                       0.399 |                         0.186 |                     -0.163 |                        0.194 |
|  6 | Jales                 |                       0.499 |                         0.105 |                      0.155 |                        0.11  |                       0.467 |                         0.106 |                      0.011 |                        0.12  |
|  7 | Santa Isabel          |                       0.653 |                         0.165 |                     -0.122 |                        0.353 |                       0.63  |                         0.154 |                     -0.361 |                        0.374 |
|  8 | Santos                |                       0.917 |                         0.052 |                      0.776 |                        0.061 |                       0.907 |                         0.052 |                      0.764 |                        0.064 |
|  9 | São Caetano do Sul    |                       0.686 |                         0.115 |                      0.212 |                        0.219 |                       0.664 |                         0.118 |                      0.079 |                        0.239 |
| 10 | São José do Rio Preto |                       0.78  |                         0.036 |                     -0.111 |                        0.035 |                       0.772 |                         0.037 |                     -0.397 |                        0.037 |
| 11 | Todas cidades         |                       0.968 |                         0.022 |                      0.511 |                        0.022 |                       0.963 |                         0.023 |                      0.369 |                        0.024 |

As figuras abaixo mostram o gráfico de nascidos vivos para os últimos cinco anos, a fim de mostrar como são as características desses dados que fizeram que a análise feita chegasse na conclusão que se chegou. Por exemplo, temos a cidade de Santa Isabel, para a qual foi apontada mudança do número de nascidos vivos, e Dracena, para a qual foi apontado que não houve mudança.

![Santa Isabel](./assets/images/santaisabelwhite.png)
![Dracena](./assets/images/dracenawhite.png)


### RACACOR != White

Para a população não-branca, incluindo Pardos, Pretos, Negros, Índigenas e Amarelos, a análise indicou que houve mudança de comportamento no número de nascidos vivos para a cidade de Barueri. Para Araçatuba, São Paulo, Santos e São José do Rio Preto não foi detectada diferença entre os períodos, e para as demais cidades o resultado foi inconclusivo.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.668 |                         0.258 |                      0.271 |                        0.299 |                       0.702 |                         0.267 |                      0.09  |                        0.342 |
|  1 | Araçatuba             |                       0.903 |                         0.145 |                     -1.054 |                        0.069 |                       0.911 |                         0.155 |                     -1.193 |                        0.072 |
|  2 | Barueri               |                       0.707 |                         0.096 |                      0.058 |                        0.125 |                       0.684 |                         0.099 |                     -0.114 |                        0.134 |
|  3 | São Paulo             |                       0.967 |                         0.023 |                      0.54  |                        0.019 |                       0.969 |                         0.025 |                      0.425 |                        0.02  |
|  4 | Dracena               |                       0.274 |                         0.38  |                      0.474 |                        0.261 |                       0.253 |                         0.402 |                      0.341 |                        0.289 |
|  5 | Guaíra                |                       0.226 |                         0.449 |                     -0.182 |                        0.384 |                       0.274 |                         0.425 |                     -0.306 |                        0.413 |
|  6 | Jales                 |                       0.522 |                         0.251 |                     -0.083 |                        0.273 |                       0.498 |                         0.267 |                     -0.267 |                        0.29  |
|  7 | Santa Isabel          |                       0.618 |                         0.343 |                     -0.159 |                        0.138 |                       0.648 |                         0.372 |                     -0.768 |                        0.172 |
|  8 | Santos                |                       0.894 |                         0.067 |                      0.356 |                        0.063 |                       0.905 |                         0.071 |                      0.262 |                        0.066 |
|  9 | São Caetano do Sul    |                       0.729 |                         0.285 |                     -0.328 |                        0.142 |                       0.72  |                         0.32  |                     -0.604 |                        0.158 |
| 10 | São José do Rio Preto |                       0.958 |                         0.101 |                      0.219 |                        0.031 |                       0.954 |                         0.108 |                      0.075 |                        0.035 |
| 11 | Todas cidades         |                       0.971 |                         0.023 |                      0.574 |                        0.019 |                       0.972 |                         0.025 |                      0.502 |                        0.022 |


### ESCMAE <= 7 anos

Para esta população, indicou-se mudança no número de nascidos vivos para as cidades de Araçatuba, Barueri, Santos e São José do Rio Preto, e não houve mudança em São Paulo. Para as demais cidades, o resultado foi inconclusivo.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.587 |                         0.574 |                     -1.518 |                        0.855 |                       0.529 |                         0.557 |                     -2.468 |                        0.988 |
|  1 | Araçatuba             |                       0.799 |                         0.193 |                      0.309 |                        0.266 |                       0.768 |                         0.185 |                      0.04  |                        0.313 |
|  2 | Barueri               |                       0.89  |                         0.189 |                      0.064 |                        0.31  |                       0.878 |                         0.178 |                     -0.262 |                        0.362 |
|  3 | São Paulo             |                       0.99  |                         0.036 |                     -0.194 |                        0.046 |                       0.989 |                         0.037 |                     -0.624 |                        0.053 |
|  4 | Dracena               |                       0.471 |                         0.47  |                    nan     |                        1.165 |                       0.431 |                         0.458 |                    nan     |                        1.437 |
|  5 | Guaíra                |                       0.634 |                         0.48  |                      0     |                        0.157 |                       0.616 |                         0.484 |                      0     |                        0.105 |
|  6 | Jales                 |                       0.642 |                         0.403 |                     -0.511 |                        0.439 |                       0.598 |                         0.385 |                     -0.485 |                        0.455 |
|  7 | Santa Isabel          |                       0.684 |                         0.319 |                      0     |                        0.276 |                       0.637 |                         0.315 |                      0     |                        0.294 |
|  8 | Santos                |                       0.888 |                         0.143 |                     -0.27  |                        0.221 |                       0.879 |                         0.135 |                     -0.682 |                        0.258 |
|  9 | São Caetano do Sul    |                       0.618 |                         0.517 |                    nan     |                        0.206 |                       0.548 |                         0.49  |                    nan     |                        0.387 |
| 10 | São José do Rio Preto |                       0.709 |                         0.115 |                     -0.087 |                        0.116 |                       0.702 |                         0.112 |                     -0.344 |                        0.119 |
| 11 | Todas cidades         |                       0.99  |                         0.035 |                      0.303 |                        0.037 |                       0.989 |                         0.036 |                     -0.054 |                        0.047 |

A seguir se tem os plots do número de nascidos vivos de Barueri e de São Paulo, para a população de mulheres com 7 ou menos anos de estudos.

![Barueri](./assets/images/barueriest7.png)
![São Paulo](./assets/images/saopauloest7.png)

### ESCMAE >= 8 anos

Para esta estratificação foi detectada mudança para as cidades de Andradina e São Caetano do Sul. Para Dracena, Guaíra e Santo Isabel os resultados foram inconclusivos, e para as demais cidades não foi detectada mudança.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.521 |                         0.115 |                     -0.565 |                        0.146 |                       0.507 |                         0.118 |                     -1.176 |                        0.18  |
|  1 | Araçatuba             |                       0.682 |                         0.058 |                      0.236 |                        0.045 |                       0.669 |                         0.06  |                     -0.069 |                        0.057 |
|  2 | Barueri               |                       0.659 |                         0.055 |                      0.364 |                        0.076 |                       0.662 |                         0.056 |                      0.313 |                        0.076 |
|  3 | São Paulo             |                       0.904 |                         0.019 |                      0.652 |                        0.018 |                       0.899 |                         0.019 |                      0.599 |                        0.019 |
|  4 | Dracena               |                       0.32  |                         0.146 |                     -0.289 |                        0.085 |                       0.337 |                         0.151 |                     -0.496 |                        0.088 |
|  5 | Guaíra                |                       0.283 |                         0.164 |                     -0.964 |                        0.234 |                       0.283 |                         0.158 |                     -1.052 |                        0.241 |
|  6 | Jales                 |                       0.709 |                         0.097 |                      0.001 |                        0.069 |                       0.667 |                         0.102 |                     -0.281 |                        0.077 |
|  7 | Santa Isabel          |                       0.352 |                         0.125 |                     -0.19  |                        0.192 |                       0.362 |                         0.127 |                     -0.452 |                        0.205 |
|  8 | Santos                |                       0.812 |                         0.038 |                      0.786 |                        0.038 |                       0.803 |                         0.038 |                      0.767 |                        0.037 |
|  9 | São Caetano do Sul    |                       0.808 |                         0.098 |                      0.001 |                        0.171 |                       0.787 |                         0.099 |                     -0.146 |                        0.183 |
| 10 | São José do Rio Preto |                       0.922 |                         0.037 |                     -0.175 |                        0.029 |                       0.916 |                         0.039 |                     -0.363 |                        0.032 |
| 11 | Todas cidades         |                       0.911 |                         0.018 |                      0.847 |                        0.012 |                       0.906 |                         0.019 |                      0.837 |                        0.012 |

### ESTCIVMAE = Casada ou União estável

Para o caso de mães casadas ou em união estável, apenas detectou-se mudança na cidade de Santos. Para São José do Rio Preto, Barueri e São Paulo, não se detectou alteração no número de nascidos vivos. Para as demais cidades, o resultado de treino não foi bom, portanto inconclusivo.


|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.293 |                         0.138 |                     -0.525 |                        0.215 |                       0.272 |                         0.141 |                     -1.173 |                        0.26  |
|  1 | Araçatuba             |                       0.436 |                         0.077 |                      0.303 |                        0.084 |                       0.406 |                         0.079 |                      0.17  |                        0.093 |
|  2 | Barueri               |                       0.588 |                         0.072 |                      0.32  |                        0.093 |                       0.573 |                         0.071 |                      0.266 |                        0.095 |
|  3 | São Paulo             |                       0.886 |                         0.023 |                      0.638 |                        0.027 |                       0.857 |                         0.023 |                      0.505 |                        0.031 |
|  4 | Dracena               |                       0.287 |                         0.199 |                     -0.59  |                        0.289 |                       0.296 |                         0.194 |                     -0.757 |                        0.302 |
|  5 | Guaíra                |                       0.227 |                         0.252 |                     -0.431 |                        0.536 |                       0.233 |                         0.238 |                     -0.632 |                        0.55  |
|  6 | Jales                 |                       0.471 |                         0.141 |                      0.071 |                        0.129 |                       0.451 |                         0.138 |                     -0.19  |                        0.146 |
|  7 | Santa Isabel          |                       0.256 |                         0.181 |                     -0.273 |                        0.234 |                       0.261 |                         0.184 |                     -0.688 |                        0.274 |
|  8 | Santos                |                       0.802 |                         0.045 |                      0.801 |                        0.042 |                       0.767 |                         0.047 |                      0.755 |                        0.046 |
|  9 | São Caetano do Sul    |                       0.826 |                         0.158 |                      0.011 |                        0.186 |                       0.798 |                         0.162 |                     -0.111 |                        0.197 |
| 10 | São José do Rio Preto |                       0.835 |                         0.046 |                      0.008 |                        0.037 |                       0.819 |                         0.048 |                     -0.161 |                        0.041 |
| 11 | Todas cidades         |                       0.888 |                         0.021 |                      0.751 |                        0.022 |                       0.861 |                         0.022 |                      0.647 |                        0.024 |

A seguir se tem os plots do número de nascidos vivos de Santos e São José do Rio Preto, para a estratificação apresentada.

![Santos](./assets/images/santoscasada.png)
![São José do Rio Preto](./assets/images/saojosecasada.png)


### ESTCIVMAE = Solteira

Para as mães solteira, apenas em Barueri se detectou diferença no número de nascidos vivos. Para Araçatuba, São Paulo, Santos e São José do Rio Preto não se detectou mudança, e para as demais cidades o resultado foi inconclusivo.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.407 |                         0.154 |                     -0.028 |                        0.155 |                       0.393 |                         0.153 |                     -0.239 |                        0.174 |
|  1 | Araçatuba             |                       0.692 |                         0.107 |                     -0.283 |                        0.081 |                       0.706 |                         0.112 |                     -0.389 |                        0.08  |
|  2 | Barueri               |                       0.714 |                         0.122 |                     -2.319 |                        0.104 |                       0.724 |                         0.126 |                     -3.036 |                        0.113 |
|  3 | São Paulo             |                       0.975 |                         0.025 |                      0.505 |                        0.017 |                       0.973 |                         0.025 |                      0.381 |                        0.02  |
|  4 | Dracena               |                       0.745 |                         0.425 |                     -1.26  |                        0.471 |                       0.754 |                         0.414 |                     -2.193 |                        0.572 |
|  5 | Guaíra                |                       0.519 |                         0.514 |                     -0.504 |                        0.425 |                       0.571 |                         0.485 |                     -0.708 |                        0.446 |
|  6 | Jales                 |                       0.854 |                         0.335 |                     -0.106 |                        0.224 |                       0.865 |                         0.324 |                     -0.491 |                        0.253 |
|  7 | Santa Isabel          |                       0.778 |                         0.283 |                     -0.79  |                        0.34  |                       0.767 |                         0.286 |                     -1.078 |                        0.333 |
|  8 | Santos                |                       0.806 |                         0.05  |                      0.718 |                        0.049 |                       0.794 |                         0.049 |                      0.681 |                        0.051 |
|  9 | São Caetano do Sul    |                       0.279 |                         0.113 |                      0.055 |                        0.178 |                       0.291 |                         0.112 |                     -0.144 |                        0.203 |
| 10 | São José do Rio Preto |                       0.818 |                         0.047 |                      0.144 |                        0.033 |                       0.807 |                         0.047 |                      0.01  |                        0.035 |
| 11 | Todas cidades         |                       0.972 |                         0.024 |                      0.598 |                        0.015 |                       0.969 |                         0.025 |                      0.504 |                        0.017 |

### AGEGROUP = A1

Detectou-se mudança no comportamento do número de nascidos vivos para as cidades de Araçatuba, Barueri, Santos e São José do Rio Preto. Não se detectou mudança para São Paulo, apenas. Para as demais seis cidades não se chegou a conclusão devido aos resultados ruins de ajuste no treino do modelo.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.432 |                         0.327 |                     -0.469 |                        0.292 |                       0.367 |                         0.316 |                     -1.116 |                        0.363 |
|  1 | Araçatuba             |                       0.558 |                         0.141 |                      0.138 |                        0.162 |                       0.526 |                         0.136 |                     -0.006 |                        0.176 |
|  2 | Barueri               |                       0.837 |                         0.105 |                     -0.106 |                        0.205 |                       0.816 |                         0.101 |                     -0.295 |                        0.225 |
|  3 | São Paulo             |                       0.97  |                         0.029 |                      0.036 |                        0.043 |                       0.962 |                         0.028 |                     -0.234 |                        0.048 |
|  4 | Dracena               |                       0.403 |                         0.427 |                      0.397 |                        0.664 |                       0.357 |                         0.413 |                      0.325 |                        0.71  |
|  5 | Guaíra                |                       0.369 |                         0.509 |                      0.008 |                        0.921 |                       0.35  |                         0.482 |                     -0.051 |                        0.909 |
|  6 | Jales                 |                       0.298 |                         0.259 |                      0.039 |                        0.269 |                       0.25  |                         0.266 |                     -0.275 |                        0.306 |
|  7 | Santa Isabel          |                       0.407 |                         0.371 |                      0.104 |                        1.091 |                       0.371 |                         0.347 |                     -0.051 |                        1.206 |
|  8 | Santos                |                       0.756 |                         0.105 |                     -0.346 |                        0.11  |                       0.707 |                         0.103 |                     -0.578 |                        0.118 |
|  9 | São Caetano do Sul    |                       0.506 |                         0.352 |                     -1.208 |                        1.166 |                       0.47  |                         0.33  |                     -1.694 |                        1.297 |
| 10 | São José do Rio Preto |                       0.551 |                         0.094 |                     -3.293 |                        0.1   |                       0.531 |                         0.095 |                     -3.724 |                        0.108 |
| 11 | Todas cidades         |                       0.974 |                         0.027 |                     -0.299 |                        0.044 |                       0.968 |                         0.026 |                     -0.552 |                        0.049 |

### AGEGROUP = A2

Neste caso se detectou mudança no comportamento do número de nascidos vivos apenas para São Caetano do Sul. Não foi apontada diferença do número para as cidades de Barueri, São Paulo, Jales, Santos e São José do Rio Preto.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.371 |                         0.127 |                     -0.337 |                        0.176 |                       0.372 |                         0.127 |                     -0.733 |                        0.206 |
|  1 | Araçatuba             |                       0.448 |                         0.076 |                      0.354 |                        0.056 |                       0.436 |                         0.078 |                      0.131 |                        0.068 |
|  2 | Barueri               |                       0.823 |                         0.047 |                      0.442 |                        0.073 |                       0.809 |                         0.047 |                      0.39  |                        0.076 |
|  3 | São Paulo             |                       0.935 |                         0.018 |                      0.606 |                        0.015 |                       0.919 |                         0.018 |                      0.529 |                        0.016 |
|  4 | Dracena               |                       0.41  |                         0.164 |                     -0.056 |                        0.082 |                       0.418 |                         0.168 |                     -0.464 |                        0.106 |
|  5 | Guaíra                |                       0.307 |                         0.159 |                     -0.013 |                        0.124 |                       0.322 |                         0.157 |                     -0.184 |                        0.139 |
|  6 | Jales                 |                       0.54  |                         0.096 |                      0.358 |                        0.074 |                       0.515 |                         0.099 |                      0.265 |                        0.077 |
|  7 | Santa Isabel          |                       0.263 |                         0.139 |                      0.119 |                        0.232 |                       0.247 |                         0.14  |                     -0.128 |                        0.256 |
|  8 | Santos                |                       0.876 |                         0.04  |                      0.828 |                        0.041 |                       0.857 |                         0.04  |                      0.816 |                        0.042 |
|  9 | São Caetano do Sul    |                       0.59  |                         0.109 |                      0.039 |                        0.176 |                       0.559 |                         0.105 |                     -0.119 |                        0.189 |
| 10 | São José do Rio Preto |                       0.839 |                         0.042 |                     -0.246 |                        0.041 |                       0.831 |                         0.042 |                     -0.428 |                        0.044 |
| 11 | Todas cidades         |                       0.93  |                         0.018 |                      0.873 |                        0.01  |                       0.913 |                         0.019 |                      0.849 |                        0.01  |

### AGEGROUP = A3

Para o AGEGROUP A3 as cidades de Andradina, Dracena, Guaíra, Jales, Santa Isabel e São Caetano do Sul não obtiveram bons resultados de treino, levando à resultados inconclusivos. Detectou-se mudança para Araçatuba e Barueri, e não detectou-se mudança para São Paulo, Santos e São José do Rio Preto.

|    | Cidade    |   Fold 0, Train, R2 |   Fold 0, Train, MAPE |   Fold 0, Test, R2 |   Fold 0, Test, MAPE |   Fold 1, Train, R2 |   Fold 1, Train, MAPE |   Fold 1, Test, R2 |   Fold 1, Test, MAPE |
|---:|:----------------------|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|----------------------------:|------------------------------:|---------------------------:|-----------------------------:|
|  0 | Andradina             |                       0.464 |                         0.256 |                     -0.251 |                        0.234 |                       0.455 |                         0.254 |                     -0.542 |                        0.259 |
|  1 | Araçatuba             |                       0.666 |                         0.154 |                      0.032 |                        0.117 |                       0.649 |                         0.155 |                     -0.179 |                        0.129 |
|  2 | Barueri               |                       0.669 |                         0.104 |                      0.438 |                        0.128 |                       0.671 |                         0.107 |                      0.383 |                        0.134 |
|  3 | São Paulo             |                       0.943 |                         0.026 |                      0.543 |                        0.026 |                       0.944 |                         0.026 |                      0.405 |                        0.029 |
|  4 | Dracena               |                       0.23  |                         0.383 |                     -0.589 |                        0.276 |                       0.211 |                         0.415 |                     -0.765 |                        0.283 |
|  5 | Guaíra                |                       0.253 |                         0.558 |                     -0.028 |                        0.949 |                       0.241 |                         0.543 |                     -0.092 |                        0.962 |
|  6 | Jales                 |                       0.577 |                         0.287 |                      0.533 |                        0.218 |                       0.556 |                         0.287 |                      0.468 |                        0.229 |
|  7 | Santa Isabel          |                       0.264 |                         0.329 |                      0.129 |                        0.41  |                       0.252 |                         0.338 |                     -0.114 |                        0.463 |
|  8 | Santos                |                       0.746 |                         0.067 |                      0.505 |                        0.076 |                       0.748 |                         0.068 |                      0.286 |                        0.096 |
|  9 | São Caetano do Sul    |                       0.831 |                         0.205 |                     -0.281 |                        0.235 |                       0.806 |                         0.22  |                     -0.485 |                        0.249 |
| 10 | São José do Rio Preto |                       0.903 |                         0.082 |                      0.181 |                        0.052 |                       0.89  |                         0.086 |                      0.061 |                        0.057 |
| 11 | Todas cidades         |                       0.953 |                         0.025 |                      0.597 |                        0.029 |                       0.953 |                         0.025 |                      0.474 |                        0.033 |



# Discussão

Cidades como Guaíra, Dracena e Jales tiveram maus ajustes de parâmetros de treino para a maioria das estratificações, o que não nos permite tirar muitas conclusões sobre o comportamento do número de nascidos vivos destas cidades. O que se pode afirmar é o modelo escolhido provavelmente não é adequado para estas cidades, ou porque ele não captura a dinâmica do número de NV delas ou porque este número é demasiadamente ruidoso ou aleatório. Para verificarmos isso, podemos observar os gráficos dos números de nascidos vivos durante os anos de 2006 à 2020 para Santos e São Paulo (cidades com bons ajustes), e Dracena e Guaíra (cidade com ajustes majoritariamente ruins):

![Sâo Paulo](./assets/images/saopaulo.png)
![Santos](./assets/images/santos.png)
![Dracena](./assets/images/dracena.png)
![Guaíra](./assets/images/guaira.png)

 
Claramente se vê que São Paulo e Santos seguem um padrão e há uma sazonalidade relativamente comportada entre os meses. Por exemplo, quase todos os anos, em Santos, o número de nascidos vivos cai a partir no mês de junho até novembro, e sobe novamente em dezembro. Dito isso, pode-se ver também que é mais difícil detectar certo padrão nos números de Guaíra e Dracena, e isto muito provavelmente se dá pela ordem de grandeza do número de nascidos vivos destas duas cidades, tendo no máximo pouco mais de 80 nascidos vivos no mês. Esse pouco número de NV o torna altamente sujeito a aleatoriedades e eventos esporádicos, tornando o modelo incapaz de se ajustar bem aos dados devido à alta incerteza. Esta incerteza pode se tornar ainda maior ao se estratificar o *dataset*, já que o número de NV em uma amostra será ainda menor.


Para visualizarmos graficamente o que a análise feita pode indicar, vamos usar as cidades de São Paulo e São Caetano do Sul como exemplo, e os anos de 2015 à 2020.

![São Paulo a partir de 2015](./assets/images/spfull.png)
![São Caetano do Sul a partir de 2015](./assets/images/saocaetanofull.png)

Segundo à análise feita, o número de NV para São Paulo em 2020 foi o esperado pelo modelo. Pelo gráfico realmente os valores reais de 2020 parecem como esperado, há um decréscimo do número de todos os meses, como já bem acontecendo há alguns anos e o "formato" da curva do ano como um todo parece similar aos anos anteriores. Na mesma análise, São Caetano do Sul deu indícios de mudança de comportamento em 2020. Esse acontecimento é claramente visto no gráfico do número de NV da cidade: há um crescimento anormal no segundo semestre de 2020, principalmente no mês 10, que pode (ou não) ser consequência da pandemia. Isso é completamente discutível, já que o lockdown se deu na maioria das cidades brasileiras a partir de março, que fica exatamente 7 meses antes do mês 10.

Outro exemplo é para a cidade de Santos, para AGEGROUP igual à A1 (mulheres com menos de 20 anos). Na análise concluimos que houve um diferença para esta cidade, no segundo semestre de 2020. O gráfico abaixo mostra o número por mês, a partir de 2015:
 
![Santos a partir de 2015, AGEGROUP A1](./assets/images/santosa1.png)

Não se vê claramente uma diferença, apesar da análise a ter apontado. Isto poderia pedir por análise mais detalhadas, por mais visualizações ou pela pesquisa de diferentes modelos.

Uma coisa interessante a se nota é para quase todos os casos de estratificação o uso do Fold 1, que tem mais dados, prejudica as métricas para o conjunto de treino. Isso pode indicar que os anos que ficam de fora no Fold 0 (2016 e 2017) realmente tem uma distribuição diferente (e têm, devido ao zika vírus), o modelo não é flexível o suficiente e tem dificuldades de se ajustar à esses anos anômalos. Entretanto, viu-se no teste novamente um pequena piora das métricas, mesmo usando os anos de zika vírus, que supostamente teriam maior semelhança com os meses de pandemia de 2020. Isto pode indicar, entre outras coisas:
 - Que o modelo não teve capacidade de generalizar o conhecimento dos nos anos de zika vírus;
 - ou que a distribuição dos dados nos anos de zika vírus é diferente do que do segundo semestre de 2020;

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

Finalmente, a tabela a seguir mostra a conclusão de cada uma das análises. O símbolo de zero cortado indica que a análise foi inconclusiva, o sinal verde indica que houve mudança e o sinal vermelho indica que não houve mudança no número de nascidos vivos. Pode-se ver, por exemplo, que São Paulo não teve mudança em nenhuma das estratificações avaliadas, que Guaíra não teve resultado conclusivo em nenhuma das estratificações (provavelmente porque tem muitos poucos habitantes), e que há algumas cidades para as quais se detectou mudanças para algumas das estratificações e para outras não.

![Resumo](./assets/images/resumo.jpg)


# Conclusão

Há diversas conclusões, reflexões e discussões que pode-se ter baseando-se nos resultados obtidos. Primeiramente, as cidade de São Paulo e Santos, quase que em todas análises, tiveram bons ajustes e boas métricas no teste, mesmo para as estratificações do dataset. Isto pode indicar que realmente o número de nascidos vivos não se alterou durante o semestre de 2020 para estas cidades.

Cidades como Guaíra, Dracena, Jales e Santa Isabel foram prejudicadas por terem poucos resultados conclusivos. Isso indica que para estas cidades o modelo utilizado não representa a dinâmica do número de nascidos vivos destas cidades, e talvez deveria-se buscar novas features, mudar a estrutura do modelo ou até se realizar outro tipo de análise.

A estratificação que apresentou mais mudanças foi a de mães com 7 ou menos anos de estudos, e também mães com menos de 20 anos de idade, para as cidades de Araçatuba, Barueri, Santos e São José do Rio Preto. Este resultado, entretanto, não indica que a causa desta diferença deu-se por causa da pandemia ou do COVID-19, mas que no período houve a diferença. Outra coisa interessante é que para São Caetano do sul detectou-se diferença para todas as estratificações nas quais o resultado foi conclusivo, e como se viu pelo gráfico, é visível a disparidade do segundo semestre de 2020 com os anos anteriores. Barueri também é uma cidade que teve diferença detectada para cinco estratificações, então também é uma cidade de interesse.

Conclui-se que a análise feita realmente teve sua utilidade para detectar anomalias no número de nascidos vivos, e realmente foram detectadas essas mudanças ou não mudanças para parte das cidades e para certas estratificações. Percebeu-se como a metodologia utilizada pode ser uma saída para a pouca quantidade de dados, o que nos prejudicou na hora de realizar as análises estatísticas. Entretanto não se deve confiar cegamente nos resultados do modelo, já que ele não utiliza todos os dados que poderiam ser considerados importantes para o problema proposto mas que não tinhamos acesso, e como qualquer modelo ele pode possuir vieses devido aos anos escolhidos para treinamento ou devido a sua própria estrutura.

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


# Cronograma

## Tarefas Realizadas

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

Entrega final:
 - [x] Modelagem do número de nascidos vivos, com caráter preditivo.
    - [x] Análise do impacto das variáveis de entrada na predição do modelo;
    - [x] Verificação de se a modelagem muda para subamostras da população (apenas mulheres negras, ou apenas para alguma faixa etária, por exemplo);
    - [x] Criação de modelos por cidade avaliada.
 - [x] Verificação, por cidade, do impacto da pandemia do COVID-19 por cidade avaliada.


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

## Real
|                                     Mês | Março |   |   |   | Abril |   |   |   | Maio |   |   |   | Junho |   |   |   | Julho |
|----------------------------------------:|-------|---|---|---|-------|---|---|---|------|---|---|---|-------|---|---|---|-------|
|                                  Semana | 1     | 2 | 3 | 4 | 1     | 2 | 3 | 4 | 1    | 2 | 3 | 4 | 1     | 2 | 3 | 4 | 1     |
| Definir o escopo da Pesquisa            |       |   |   | x | x     | x | x |   |      |   |   |   |       |   |   |   |       |
| Seleção de dados                        |       |   |   |   |       |   |   | x | x    |   |   |   |       |   |   |   |       |
| Pré-processamento dos dados             |       |   |   |   |       |   |   |   | x    | x | x |   |       |   |   |   |       |
| Processamento e transformação dos dados |       |   |   |   |       |   |   |   | x    | x | x |   |       |   |   |   |       |
| Data Mining                             |       |   |   |   |       |   |   |   |      |   | x |   |       | x | x |   |       |
| Criação de modelos                      |       |   |   |   |       |   |   |   |      |   |   |   |       | x | x |   |       |
| Análise estatística                     |       |   |   |   |       |   |   |   |      |   | x |   |       | x | x |   |       |
| Avaliação dos modelos                   |       |   |   |   |       |   |   |   |      |   |   |   |       | x | x |   |       |
| Documentação                            |       |   |   | x | x     | x | x | x | x    | x | x |   |   x   | x | x | x |       |
| Apresentação de resultados              |       |   |   |   |       |   |   |   |      |   |   |   |       |   |   | x |   x   |


