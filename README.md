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
Introdução: A pandemia da COVID-19 causada pelo vírus SARS_COV_2 tem tomado proporções alarmantes ao nível mundial. Atualmente (12/04/2021), ao nível global foram notificados cerca de 136,181,468, sendo o Brasil um dos países mais afetado pela pandemia, com aproximadamente 2,938,804 caso notificados. A pandemia tem afetado a população no geral sem distinção do sexo, raça, e estrato social com grande impacto no sistema de saúde. De entre os efeitos da pandemia no sistema de saúde, destacam-se a interrupção ou redução de provisão dos serviços de saúde materna e perinatal que podem influenciar negativamente nos seus indicadores, como é o caso do número de nascidos vivos. Objetivo: o presente estudo tem o objetivo de avaliar o impacto da pandemia da COVID-19 no número de nascidos vivos nos municípios do estado de São Paulo. Metodologia: será realizado uma análise de serie temporal, baseada em dados Sistema de Informações de Nascidos Vivos (SINASC/DATASUS) e do Banco de Dados de Síndrome Respiratória Aguda Grave (SRAG 2021), com o auxílio de métodos estatísticos  e de ferramentas inteligência artificial (métodos de aprendizado de maquinas) - SPSS Modeler 18.1, Google Colab e  Jupyter Notebook - realizaremos a modelagem, análise da curva de nascimentos vivos nos últimos 10 anos prévios a pandemia e a predição do número de nascidos vivos esperados para o ano 2020.  Resultados esperados: através desta pesquisa esperamos obter os padrões das curvas de nascidos vivos e estabelecer uma correlação entre a pandemia e o indicador de saúde materna e perinatal para os diferentes municípios do estado de São Paulo.



## Abstract

Introduction: The COVID-19 pandemic caused by the SARS_COV_2 virus has taken on alarming proportions worldwide. Currently (12/04/2021), at the global level, about 136,181,468 have been notified, with Brazil being one of the countries most affected by the pandemic, with approximately 2,938,804 reported cases. The pandemic has affected the general population regardless of sex, race, and social strata, with a great impact on the health system. Among the effects of the pandemic on the health system, the interruption or reduction in the provision of maternal and perinatal health services stand out, which can negatively influence its indicators, such as the number of live births. Objective: This study aims to assess the impact of the COVID-19 pandemic on the number of live births in the cities of the state of São Paulo. Methodology: a time series analysis will be carried out, based on data from the Live Birth Information System (SINASC/DATASUS) and the Severe Acute Respiratory Syndrome Database (SRAG 2021), with the aid of statistical methods and artificial intelligence tools (machine learning methods) - SPSS Modeler 18.1, Google Colab and Jupyter Notebook - we will carry out the modeling, analysis of the curve of live births in the last 10 years prior to the pandemic and the prediction of the number of live births expected for the year 2020. Results Expected: through this research we hope to obtain the patterns of the curves of live births and establish a correlation between the pandemic and the maternal and perinatal health indicator for the different cities of the state of São Paulo

Please watch the project presentation [video](https://drive.google.com/file/d/1xz9lfkAAQFm5fQf4hEIceaY8FeVvwFCI/view?usp=sharing).

# Videos do Projeto

## Vídeo da Proposta
Por favor, assista ao [vídeo](https://drive.google.com/file/d/1xz9lfkAAQFm5fQf4hEIceaY8FeVvwFCI/view?usp=sharing) de apresentação do projeto.

## Vídeo da Apresentação Final
????

# Slides do Projeto

## Slides da Proposta
## Slides da Apresentação Final

# Introdução e Referenciais de Teóricos
> Contextualização do projeto
>
> Caracterização do problema
>
> Motivação
>
> Relevância
>
> Trabalhos relacionados
>
> Indicação (bastante resumida) da análise proposta
>
> Indicação (bastante resumida) dos resultados alcançados

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

## Perguntas de Pesquisa
 - Qual foi o impacto da pandemia da COVID-19 na taxa de nascidos vivos no Estado de São Paulo?
 - É possível prever a taxa de nascidos vivos dos anos seguintes com os dados anteriores?

# Metodologia

Utilização de análise estatística e testes de hipótese para verificação da primeira pergunta de pesquisa. Criação de modelos estatísticos para avaliação do impacto de diferentes variáveis populacionais no impacto do número de nascidos vivos.

Utilização de Aprendizado de Máquina e modelos estatísticos para predição de eventos futuros utilizando os dados à disposição. Análise do impacto das variáveis preditoras do número de nascidos vivos para explicação dos fenômenos encontrados.


## Bases de Dados

 - [Sistema de Informação de Nascidos Vivos](https://datasus.saude.gov.br/transferencia-de-arquivos/) (SINASC/DATASUS), website do ministério da saúde

 - [Banco de Dados de Síndrome Respiratória Aguda Grave](https://opendatasus.saude.gov.br/dataset/bd-srag-2021) - incluindo dados da COVID-19

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
 - Se nasceu com anomalia;
 - Número de filhos vivos;
 - Número de filhos mortos.

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

## Evolução do Projeto

## Resultados e Discussão

## Conclusões

## Trabalhos Futuros

## Referências
