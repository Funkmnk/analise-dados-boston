# Autor: Igor Chagas
# Data: 06/10/2025
# H2: Cidades com menos educação (PTRATIO), tem maior o nível de criminalidade (CRIM) e distancia maior de centros de emprego (DIS).

# ----- Validação da Hipótese 2 -----
# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Carregando o Dataset tratado (imputação por mediana)
df = pd.read_csv('../data/HousingData_Tratado.csv')

# Parte 1: PTRATIO vs CRIM
var_independente = 'PTRATIO'
var_dependente = 'CRIM'

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
    print("A PRIMEIRA PARTE DA HIPÓTESE 2 é VÁLIDA de acordo com os dados.")
else:
    print(f"Como p-valor é maior que {alpha}, a correlação não é significativa.")
    print("A PRIMEIRA PARTE DA HIPÓTESE 2 NÃO É VÁLIDA de acordo com os dados")
    
# Plotando a dispersão
plt.figure(figsize=(10, 7))
sns.scatterplot(x=df[var_independente], y=df[var_dependente], alpha=0.6)
sns.regplot(x=df[var_independente], y=df[var_dependente], scatter=False, color='red')
plt.title(f"Relação entre proporção aluno-professor ({var_independente}) e criminalidade ({var_dependente})", fontsize=14)
plt.xlabel(f"Proporção aluno-professor ({var_independente})")
plt.ylabel(f"Taxa de criminalidade ({var_dependente})")
plt.grid(True)
# plt.savefig('../plot/h2_grafico_dispersao_PTRATIO_vs_CRIM.png')
plt.show()

# ========================================================================================================================
# Parte 2: PTRATIO vs DIS
var_independente = 'PTRATIO'
var_dependente = 'DIS'

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
    print("A SEGUNDA PARTE DA HIPÓTESE 2 é VÁLIDA de acordo com os dados.")
else:
    print(f"Como p-valor é maior que {alpha}, a correlação não é significativa.")
    print("A SEGUNDA PARTE DA HIPÓTESE 2 NÃO É VÁLIDA de acordo com os dados")
    
# Plotando a dispersão
plt.figure(figsize=(10, 7))
sns.scatterplot(x=df[var_independente], y=df[var_dependente], alpha=0.6)
sns.regplot(x=df[var_independente], y=df[var_dependente], scatter=False, color='red')
plt.title(f"Relação entre proporção aluno-professor ({var_independente}) e distância de centros de emprego ({var_dependente})", fontsize=14)
plt.xlabel(f"Proporção aluno-professor ({var_independente})")
plt.ylabel(f"Distância dos centros de emprego ({var_dependente})")
plt.grid(True)
# plt.savefig('../plot/h2_grafico_dispersao_PTRATIO_vs_DIS.png')
plt.show()