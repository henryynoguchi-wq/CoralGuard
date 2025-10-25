import pandas as pd

# === CoralGuard – versão inicial ===
# Este script carrega dados fictícios de recifes de coral
# e imprime as primeiras linhas. Futuras versões terão
# visualizações interativas e análises mais complexas.

df = pd.read_csv("../data/reefs.csv")
print(df.head())
