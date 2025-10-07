# Análise de Dados do Mercado Imobiliário de Boston

## Visão Geral

Este projeto realiza uma análise exploratória de dados sobre o mercado imobiliário de Boston, utilizando o dataset "[HousingData.csv](https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset)". O objetivo principal é investigar as relações entre diversas variáveis e o valor mediano dos imóveis (MEDV), além de outras características socioeconômicas da região.

A análise segue uma abordagem estruturada que inclui:
- Tratamento de dados ausentes por meio de imputação pela mediana.
- Análise de concentração e distribuição para todas as variáveis numéricas, com estatísticas descritivas e visualizações (histogramas e boxplots).
- Análise de moda para variáveis categóricas.
- Investigação aprofundada das correlações entre pares de variáveis.
- Formulação e validação de hipóteses por meio de testes estatísticos (correlação de Pearson) e gráficos de dispersão.

## Hipóteses Analisadas

As seguintes hipóteses foram criadas e validadas durante a análise:

* **Hipótese 1:** Cidades com maiores taxas de criminalidade (`CRIM`) tendem a ter um valor mediano de imóveis (`MEDV`) mais baixo.
* **Hipótese 2:** Cidades com uma maior proporção de alunos por professor (`PTRATIO`) apresentam maiores taxas de criminalidade (`CRIM`) e estão mais distantes dos principais centros de emprego (`DIS`).
* **Hipótese 3:** Cidades com uma menor proporção de alunos por professor (`PTRATIO`) estão correlacionadas com um maior valor mediano dos imóveis (`MEDV`), menor criminalidade (`CRIM`) e menor distância dos centros de emprego (`DIS`).
* **Hipótese 4:** Quanto maior o índice de acessibilidade às rodovias (`RAD`), maior o valor do imposto sobre a propriedade (`TAX`).

## Como Executar o Projeto

1.  **Pré-requisitos:**
    * Python 3.x
    * Bibliotecas: `pandas`, `matplotlib`, `seaborn`, `scipy`

2.  **Execução:**
    * Clone o repositório.
    * Instale as dependências necessárias.
    * Execute o script principal para uma análise geral: `python main.py`
    * Para validar as hipóteses individualmente, execute os scripts na pasta `hypotheses/`:
        * `python hypotheses/h1.py`
        * `python hypotheses/h2.py`
        * `python hypotheses/h3.py`
        * `python hypotheses/h4.py`

Os resultados numéricos serão exibidos no console e os gráficos gerados serão salvos na pasta `plot/`.