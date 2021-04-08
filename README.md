# Projeto `Impacto da pandemia da COVID-19 nos indicadores da saúde materna e perinatal nas mulheres em idade fértil do Estado de São Paulo.`

# Project `Impact of the COVID-19 pandemic on maternal and perinatal health indicators in women of childbearing potential in the state of São Paulo.`

# Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação [*Ciência e Visualização de Dados em Saúde*](https://github.com/datasci4health/home), oferecida no primeiro semestre de 2021, na Unicamp.


|Nome  | RA | Especialização|
|--|--|--|
|Charles M'poca Charles | 163383 | Saúde|
| Nome | 123456  | Computação|
| Débora Rocha Helfstein  | 234934  | Farmacêutica|
| Paulo Augusto | 263889 | Elétrica |


# Descrição Resumida do Projeto
Impacto da pandemia da COVID-19 nos indicadores da saúde materna e perinatal nas mulheres em idade fértil do Estado de São Paulo.

# Perguntas de Pesquisa
 - Qual foi o impacto da pandemia da COVID-19 na taxa de nascidos vivos no Estado de São Paulo?
 - É possível prever a taxa de nascidos vivos dos anos seguintes com os dados anteriores?

# Bases de Dados

 - [Sistema de Informação de Nascidos Vivo](https://datasus.saude.gov.br/transferencia-de-arquivos/) (SINASC/DATASUS), website do ministério da saúde

 - [Banco de Dados de Síndrome Respiratória Aguda Grave](https://opendatasus.saude.gov.br/dataset/bd-srag-2021) - incluindo dados da COVID-19

# Metodologia

Utilização de análise estatística para verificação da primeira pergunta de pesquisa.

Utilização de Aprendizado de Máquina e modelos estatísticos para predição de eventos futuros utilizando os dados à disposição.

## Variáveis de interesse

 - Tamanho da população do estado de São Paulo e dos municípios;
 - Tamanho da população do estado dos municípios de São Paulo;
 - Número de casos de COVID-19 no estado e por município de São Paulo;
 - Número de Óbitos no estado e por Município.
 - Dados da mãe:
 - Idade da mãe;
 - Escolaridade;
 - Status marital;
 - Cor de pele/raça.

## Tarefas previstas
 - Calcularemos a incidência da COVID-19 no estado e por Município;
 - Estimaremos a taxa de mortalidade e letalidade da COVID-19 no estado e no Município.

Tendo os dados:
 - Com o auxílio a linguagem Python podemos estabelecer um ranking dos municípios com base nos seguintes indicadores (incidência, taxa de mortalidade e letalidade da COVID-19)
 - Checar quais os municípios com piores indicadores.

Tendo o ranking dos municípios:
 - Podemos escolher os municípios com pior classificação (exemplo, 5 municípios e o município de são Paulo se este não fizer parte do Top 5).
 - Podemos checar dados de todos os municípios, mas tendo especial atenção para os 6 com piores indicadores.

Em seguida extrairemos dados de número de nascidos vivos (mês/mês) no geral (para os 6 municípios) e em função de:
 - Idade da mãe;
 - Escolaridade;
 - Status marital;
 - Cor de pele/raça.

# Ferramentas

Ferramenta | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Jupyter Notebook | https://jupyter.org/ | Documento virtual que permite execução de rotinas usuais de programação e documentação de todo o processo de produção do código. No projeto foi utilizado para o código de reestruturação da base de dados e para os modelos.
Google Colab | https://colab.research.google.com/ | Similar ao jupyter notebook, o Colab é uma lista de células que podem conter textos explicativos ou códigos executáveis e suas respectivas saídas. Para o projeto foi utilizado para as análise descritivas e modelo de AutoML da H2O.
SPSS Modeler 18.1 | https://www.ibm.com/br-pt/products/spss-modeler | Ambiente de trabalho de mineração de dados versátil que ajuda a criar modelos preditivos precisos de maneira rápida e intuitiva, sem programação.

# Cronograma

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
