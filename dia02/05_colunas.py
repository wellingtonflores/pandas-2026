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
