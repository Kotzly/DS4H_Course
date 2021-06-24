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

 - Caso você vá rodar o notebook principal do projeto, instale a linguagem R em sua máquina. A maneira mais fácil de fazer isso é instalando o [RStudio](https://www.rstudio.com/products/rstudio/download/#download), mas não há problema em instalar apenas o R.

## Como usar

É possível executar todas os passos de download, pré-processamento, processamento e análise de dados (feitos até a segunda entrega) [neste notebook](https://colab.research.google.com/github/Kotzly/DS4H_Course/blob/v1.1/notebooks/DS4H_full.ipynb) no Google Colab. Considera-se a entrega principal como sendo este notebook, que contém os racional das análises, além do código Python.

Para executar o notebook em sua própria máquina, primeiro siga todos os passos descritos em **Instalação**. Após isto, abra a linha de comando ou o Anaconda shell na pasta raiz do projeto e rode:

```
conda activate ds4h
jupyter notebook
```

Vá até a pasta `notebooks` e abra o notebook **DS4H_full.ipynb**.

