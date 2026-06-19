# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")
# %%
df["twitchPoints"] = df["flTwitch"] * df["qtdePontos"]
df["logPontos"] = np.log1p(df["qtdePontos"])
# %%
df["qtdeSocial"] = (
    df["flEmail"]
    + df["flTwitch"]
    + df["flYouTube"]
    + df["flInstagram"]
    + df["flBlueSky"]
)

# %%
df

# %%
df.sort_values(by="qtdePontos", ascending=False).head(1)
# %%
df.sort_values(by="qtdePontos").head(1)
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
transacoes.sort_values(by="DtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
# %%
first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["IdCliente", "data"])


# %%
pd.concat([last, first])
# %%
