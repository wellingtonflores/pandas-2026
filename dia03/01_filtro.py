# %%

import pandas as pd


# %%

pontos = [1, 1, 1, 100, 50, 60, 30, 51]
filtro = []

for i in pontos:
    filtro.append(i>=50)


resultado = []
for i in range(len(filtro)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado
# %%

colunas_linhas = {"nome": ["teo", "wel", "mavi"], "idade": [32, 24, 1], "uf": ["sp", "rs", "rj"]}

brinquedo = pd.DataFrame(colunas_linhas)

filtro = brinquedo["idade"] >= 18
brinquedo[filtro]
# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")

filtro = df["QtdePontos"] >= 50
df[filtro]

# %%

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro]

# %%

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]
# %%

filtro = ((df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50)) | (df["DtCriacao"] >= "2025-01-01")
df[filtro]

# %%
