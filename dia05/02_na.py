# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
# %%
clientes.head()
# %%
clientes.dropna(how="all")
# %%
df = pd.DataFrame(
    {
        "nome": ["Rafa", None, "Wel", "Bel"],
        "idade": [None, None, 24, 50],
        "salario": [None, None, 800, 10000],
    }
)

df
# %%
df.dropna(how="all", subset=["idade", "nome"])
# %%

df["idade"] = df["idade"].fillna(-1)
df["nome"] = df["nome"].fillna("Não identificado")
df["salario"] = df["salario"].fillna(0)
df
# %%
df.fillna({"nome": "Não identificado", "idade": -1})
# %%
medias = df[["idade", "salario"]].mean()
df.fillna(medias)
# %%
