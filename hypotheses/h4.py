# Autor: Igor Chagas
# Data: 06/10/2025
# H4: Quanto maior o índice de acessibilidade a rodovias (RAD), maior o imposto (TAX).

# ----- Validação da Hipótese 4 -----
# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregando o Dataset tratado (imputação por mediana)
df = pd.read_csv('../data/HousingData_Tratado.csv')

def validar_correlacao(var_independente, var_dependente, hipotese_parte):
    
    # Correlação de Pearson e P-Valor
    corr_valor, p_valor = stats.pearsonr(df[var_independente], df[var_dependente])
    print(f"\n--- Análise de correlação ({hipotese_parte}): {var_independente} vs {var_dependente} ---")
    print(f"\nCoeficiente de correlação de Pearson(r): {corr_valor:.4f}")

    # Classificação de direção e força
    direcao = "positiva" if corr_valor > 0 else "negativa"

    if abs(corr_valor) >= 0.7:
        forca = "forte"
    elif abs(corr_valor) >= 0.3:
        forca = "moderada"
    else:
        forca = "fraca" 

    print(f"A correlação entre {var_independente} e {var_dependente} é {direcao} e {forca}.")

    # Testando a hipótese
    alpha = 0.05
    
    print(f"\nP-Valor do teste: {p_valor:.4f}")
    
    if p_valor < alpha:
        print(f"Como o p-valor é menor que {alpha}, a correlação é significativa.")
        print(f"A {hipotese_parte} DA HIPÓTESE 3 é VÁLIDA de acordo com os dados.")
    else:
        print(f"Como o p-valor é maior ou igual a {alpha}, a correlação não é significativa.")
        print(f"A {hipotese_parte} DA HIPÓTESE 3 NÃO É VÁLIDA de acordo com os dados.")
        
    # Plotando a dispersão
    nomes_variaveis = {
        'CRIM': 'Taxa de criminalidade per capita (CRIM)',
        'ZN': 'Proporção de terrenos residenciais com mais de 25.000 pés² (ZN)',
        'INDUS': 'Proporção de acres de negócios não varejistas (INDUS)',
        'CHAS': 'Margeia o Rio Charles (CHAS)',
        'NOX': 'Concentração de óxido nítrico (NOX)',
        'RM': 'Número médio de quartos por habitação (RM)',
        'AGE': 'Proporção de imóveis ocupados construídos antes de 1940 (AGE)',
        'DIS': 'Distância ponderada aos centros de emprego de Boston (DIS)',
        'RAD': 'Índice de acessibilidade a rodovias radiais (RAD)',
        'TAX': 'Alíquota do imposto sobre a propriedade (TAX)',
        'PTRATIO': 'Proporção aluno-professor (PTRATIO)',
        'B': 'Proporção de afro-americanos por cidade (B)',
        'LSTAT': 'Porcentagem de população de baixa renda (LSTAT)',
        'MEDV': 'Valor mediano dos imóveis (MEDV)'
    }
    
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x=df[var_independente], y=df[var_dependente], alpha=0.6)
    sns.regplot(x=df[var_independente], y=df[var_dependente], scatter=False, color='red')
    plt.title(f"Relação entre {var_independente} e {var_dependente}", fontsize=14)
    plt.xlabel(nomes_variaveis.get(var_independente, var_independente))
    plt.ylabel(nomes_variaveis.get(var_dependente, var_dependente))
    plt.grid(True)
    plt.savefig(f'../plot/h4_grafico_dispersap_{var_independente}_vs_{var_dependente}.png')
    plt.show()
    
# Validando H4
validar_correlacao('RAD', 'TAX', 'Hipótese 4')