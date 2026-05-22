# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
produtos = pd.read_csv("../data/produtos.csv", sep=";")

# 03.01 - Quantas linhas há no arquivo clientes.csv?
linhas_clientes = clientes.shape[0]

# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv?
colunas_int_transacoes = transacoes.select_dtypes(include="int").shape[1]

# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv?
colunas_object_produtos = produtos.select_dtypes(include="object").shape[1]

# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv?
id_cliente_indice_4 = clientes.loc[4, "idCliente"]

# 03.05 - Qual o saldo de pontos do cliente na 10a posição sem ordenar?
saldo_10_posicao = clientes.iloc[9]["qtdePontos"]
