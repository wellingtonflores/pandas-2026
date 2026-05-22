# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
df["pontos_100"] = df["qtdePontos"] + 100
# %%
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()
# %%
df["temEmailTwitch"] = df["flEmail"] * df["flTwitch"]
df.head()
# %%
df["qtdeSocial"] = (
    df["flEmail"]
    + df["flTwitch"]
    + df["flYouTube"]
    + df["flBlueSky"]
    + df["flInstagram"]
)
df.sample(5)

# %%
df["todas_social"] = (
    df["flEmail"]
    * df["flTwitch"]
    * df["flYouTube"]
    * df["flBlueSky"]
    * df["flInstagram"]
)
df.sample(5)

# %%
np.log(df["qtdePontos"] + 1)

# %%
