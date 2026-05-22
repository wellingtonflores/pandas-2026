# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")

# %%
df.shape
# %%
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
renamed_columns = {
    "QtdePontos": "QtPontos", 
    "DescSistemaOrigem": "SistemaOrigem"
    }

#df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True) # inplace = True não precisa reeatribuir dataframe


# %%
df
# %%
colunas = ["IdCliente", "QtdePontos"]
df[colunas]
# %%

# SELECT * FROM df
df
# %%

# SELECT IdCliente from df

df[["IdCliente"]]
# %%

# SELECT IdCliente, Qtdepontos FROM df LIMIT 5

df[["IdCliente", "QtdePontos"]].tail(5)
# %%

# SELECT IdCliente, IdTransacao, QtdePontos
# FROM df
# LIMIT 5

df[["IdCliente", "IdTransacao", "QtdePontos"]].head(5)
# %%

colunas = df.columns.tolist()
colunas.sort()
colunas
# %%
df = df[colunas]
df
# %%
