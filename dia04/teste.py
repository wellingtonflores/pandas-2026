#  %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
max_pontos = clientes["qtdePontos"].max()
max_pontos
# %%
top_5 = clientes.sort_values(by="qtdePontos", ascending=False).head(5)["idCliente"]
top_5
# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["wel", "rafa", "bel"],
        "idade": ["24", "20", "50"],
        "salario": ["800", "0", "800"],
    }
)
brinquedo

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacao_produto.head()

top_5_transacoes = transacao_produto.sort_values(
    by="vlProduto", ascending=False
).head()["IdProduto"]
# %%
