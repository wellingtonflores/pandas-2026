# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
# %%
## AMOSTRAS


df_clientes.head(n=10) # Cabeçalho

# %%
df_clientes.tail(n=10) # Final do DF

# %%
df_clientes.sample(n=10) # Aleatorio
# %%
df_clientes.shape # Atributo para saber numero de linhas e colunas
# %%
df_clientes.columns # Atributo com nomes das colunas
# %%
df_clientes.index # Atributo com indices
# %%
df_clientes.info(memory_usage="deep", max_cols=2) # Info do DataFrame
# %%
df_clientes.dtypes["DtCriacao"]
# %%
