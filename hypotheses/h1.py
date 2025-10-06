# Autor: Igor Chagas
# Data: 05/10/2025
# H1: Cidades com taxas de criminalidade altas (CRIM), tendem a ter um valor mediano de imóveis (MEDV) mais baixo (desvalorização).


# ----- Validação da Hipótese 1: CRIM vs MEDV -----
# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregando o Dataset tratado (imputação por mediana)
df = pd.read_csv('../data/HousingData_Tratado.csv')

# Variáveis de análise
var_independente = 'CRIM'
var_dependente = 'MEDV'

# Correlação de Pearson e P-Valor
corr_valor, p_valor = stats.pearsonr(df[var_independente], df[var_dependente])
print(f"\n--- Análise de correlação de {var_independente} e {var_dependente} ---")
print(f"\nCoeficiente de correlação de Person(r): {corr_valor:.4f}")

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
    print("A HIPÓTESE 1 é VÁLIDA de acordo com os dados.")
else:
    print(f"Como p-valor é maior que {alpha}, a correlação não é significativa.")
    print("A HIPÓTESE 1 NÃO É VÁLIDA de acordo com os dados")
    
# Plotando a dispersão
plt.figure(figsize=(10, 7))
sns.scatterplot(x=df[var_independente], y=df[var_dependente], alpha=0.6)
sns.regplot(x=df[var_independente], y=df[var_dependente], scatter=False, color='red')
plt.title(f"Relação entre a taxa de criminalidade ({var_independente}) e o valor mediano do imóvel ({var_dependente})", fontsize=14)
plt.xlabel(f"Taxa de criminalidade ({var_independente})")
plt.ylabel(f"Valor mediano dos imóveis ({var_dependente})")
plt.grid(True)
# plt.savefig('../plot/h1_grafico_dispersao_CRIM_vs_MEDV.png')
plt.show()