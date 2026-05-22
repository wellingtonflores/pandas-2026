# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

# filtro para achar o cliente com a qtdePontos mais alta
max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %%

# filtro para pegar os 5 primeiros
# by -> parametro que vai ser aplicado o sort
# ascending -> ordem do sort
top_5 = clientes.sort_values(by="qtdePontos", ascending=False).head(5)["idCliente"]
type(top_5)

# %%

# DF exemplo para ordenar por salario e se o salario for igual ordenar por idade mas o salario desc e a idade asc

brinquedo = pd.DataFrame(
    {
        "nome": ["wel", "rafa", "bel"],
        "idade": ["24", "20", "50"],
        "salario": ["800", "0", "800"],
    }
)
brinquedo

# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
