"""
Leia o arquivo transacoes.csv com a formatação correta;
Adicione uma coluna com valores 1;
Salve o dataframe com nome: transacoes_1.csv
"""

# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df["valores 1"] = 1
df.to_csv("../data/transacoes_1.csv")
# %%
