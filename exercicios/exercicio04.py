import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

# 04.01 - Quantos clientes tem vínculo com a Twitch?
filtro_clientes_twitch = df_clientes["flTwitch"] == 1
n_clientes_vinculo_twitch = df_clientes[filtro_clientes_twitch].shape[0]

# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
filtro_clientes_saldo_maior_1000 = df_clientes["qtdePontos"] > 1000
n_clientes_saldo_maior_1000 = df_clientes[filtro_clientes_saldo_maior_1000].shape[0]

# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
df_transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
filtro_transacoes_data = df_transacoes["DtCriacao"] == "2025-02-01"
n_transacoes_dia = df_transacoes[filtro_transacoes_data].shape[0]
