# Análise Exploratória de Dados (AED) - Housing Dataset
# Autor: Igor Chagas
# Data: 04/10/2025

# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregando o dataset
df = pd.read_csv('./data/HousingData.csv')
# Lutando novamente contra meu maior inimigo
df.columns = df.columns.str.strip()

"""
- CRIM: taxa de criminalidade per capita por cidade
- ZN: proporção de terrenos residenciais zoneados para lotes com mais de 25.000 pés quadrados
- INDUS: proporção de acres de negócios não varejistas por cidade
- CHAS: variável dummy do rio Charles (1 se o terreno faz fronteira com o rio; 0 caso contrário)
- NOX: concentração de óxidos nítricos (partes por 10 milhões)
- RM: número médio de quartos por habitação
- AGE: proporção de unidades ocupadas pelo proprietário construídas antes de 1940
- DIS: distâncias ponderadas até cinco centros de emprego de Boston
- RAD: índice de acessibilidade a rodovias radiais
- TAX: taxa de imposto sobre a propriedade de valor total por $10.000
- PTRATIO: proporção aluno-professor por cidade
- B: 1000(Bk - 0.63)^2 onde Bk é a proporção de negros por cidade
- LSTAT: % de população de status inferior
- MEDV: Valor mediano de residências ocupadas pelo proprietário em $1000s
"""

# ----- Análise de concentração e distribuição das colunas numéricas  -----

# Visão geral do dataset
print("\n ##### Visão geral ##### \n")
df.info()
print("\n-----------------------------------------------")
print("##### Resumo inicial ##### \n")
print(df.describe()) # Termos valores no formato object, ta na hora da conversão, eu ouvi um amém imrãos?

# Convertendo as colunas object
colunas_para_converter = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'AGE', 'LSTAT']
for colunas in colunas_para_converter:
    df[colunas] = pd.to_numeric(df[colunas], errors='coerce') # Transforma "NA" em "NaN"
    
df.info()
print("\n##### Resumo inicial ##### \n")
print(df.describe())

# Ausentes
percentual_ausentes = (df.isnull().sum() / len(df)) * 100
print(percentual_ausentes.sort_values(ascending=False)) # Tudo juntin?

# Linhas ausentes
linhas_ausentes = df[df.isnull().any(axis=1)]
print(linhas_ausentes) # Os valores ausentes não estão agrupados, como pensei.

# Imputando mediana para tratamento
df.fillna(df.median(), inplace=True)
df.info() # Os valores estavam faltantes nas colunas object (convertidas), agora ta bnt.

# Moda CHAS (coluna categórica)
moda_chas = df['CHAS'].mode().values[0]
print(f"\n--- Análise de Moda: coluna CHAS ---")
print(f"A moda da coluna CHAS é: {moda_chas}")

if moda_chas == 0:
    significado = "não faz fronteira com o rio"
else:
    significado = "faz fronteira com o rio"

print(f"Isso significa que a maioria dos imóveis {significado}.")

for coluna_analise in df.select_dtypes(include=['float64', 'int64']).columns:
    print(f"\n===== Análise da Coluna: {coluna_analise.upper()} =====")
    
    # Análise de concentração e dispersão
    media = df[coluna_analise].mean()
    mediana = df[coluna_analise].median()
    moda = df[coluna_analise].mode().values[0]
    desvio_padrao = df[coluna_analise].std()
    variancia = df[coluna_analise].var()
    minimo = df[coluna_analise].min()
    maximo = df[coluna_analise].max()
    quartis = df[coluna_analise].quantile([0.25, 0.5, 0.75])

    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Variância: {variancia:.2f}")
    print(f"Mínimo: {minimo:.2f}")
    print(f"Máximo: {maximo:.2f}")
    print(f"Quartis: \n{quartis}\n")
    
    """
    CRIM: assimetria positiva mediana: 0.25, média: 3.48
    """
    
    # Plotando a distribuição e quartis
    plt.figure(figsize=(12, 6))
    
    # Historiograma
    plt.subplot(1, 2, 1)
    sns.histplot(df[coluna_analise], kde=True)
    plt.title(f"Histograma de {coluna_analise}")
    
    # Boxplot
    plt.subplot(1, 2, 2)
    sns.boxplot(y=df[coluna_analise])
    plt.title(f"Boxplot de {coluna_analise}")
    
    # Gráficos
    plt.tight_layout()
    plt.savefig(f'./plot/main_analise_{coluna_analise}.png')
    plt.show()

    # Análise de normalidade com Shapiro-Wilk
    stat_shapiro, p_valor_shapiro = stats.shapiro(df[coluna_analise].dropna())
    print(f"\nTeste de (Shapiro-Wilk)")
    print(f"Teste: {stat_shapiro:.4f}")
    print(f"P-Valor: {p_valor_shapiro:.4f}")
    
    if p_valor_shapiro > 0.05:
        print("Resultado: Os dados parecem ter uma distribuição NORMAL.")
    else:
        print("Resultado: Os dados apontam para uma distribuição ANORMAL.")

"""
----- Hipóteses -----

H1: Cidades com taxas de criminalidade altas CRIM, tendem a ter um valor mediano de imóveis mais baixo MEDV (desvalorização).
	- Assimetria positiva entre média e mediana no caso de crimes.

H2: Cidades com menos educação PTRATIO, tem maior o nível de criminalidade CRIM e distancia maior de centros de emprego DIS.

H3: Cidades com maior educação PTRATIO, tendem a ter um valor mediano de imóveis mais alto MEDV, menor criminalidade CRIM e 
distancia menor de centros de emprego DIS.

"""

# ----- Análise de correlação para as hipóteses  -----
print(f"\n--- Matriz de Correlação (Pearson) ---")
matriz_corr = df.corr()
print(matriz_corr)

# Plotando em heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.savefig('./plot/main_heatmap_correlacao.png')
plt.show()

# Exportando o DF para validação das hipóteses.
# df.to_csv('./data/HousingData_Tratado.csv', index=False)