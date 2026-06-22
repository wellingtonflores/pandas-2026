# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Criamos um "disfarce" dizendo que somos um navegador comum
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Passamos os headers dentro de storage_options
dfs = pd.read_html(url, storage_options=headers)
uf = dfs[1]

# %%


def str_to_float(x: str):
    x = x.replace(" ", "").replace(",", ".").replace("\xa0", "")
    return float(x)


# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)

# %%
uf
# %%
x = "73,9 anos"


def exp_to_anos(exp):
    return float(x.replace(",", ".").replace("anos", ""))


uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)
# %%
uf


# %%
def alf_to_percent(alf):
    return float(alf.replace(",", ".").replace("%", "")) / 100


uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(alf_to_percent)
# %%
uf


# %%
def mi_to_perhund(mi):
    return float(mi.replace(",", ".").replace("‰", ""))


uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(
    mi_to_perhund
)
# %%
uf


# %%
def uf_abreviacao_to_regiao(abrev):
    if abrev in ["AC", "AM", "AP", "PA", "RO", "RR", "TO"]:
        return "Norte"
    elif abrev in ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]:
        return "Nordeste"
    elif abrev in ["DF", "GO", "MS", "MT"]:
        return "Centro Oeste"
    elif abrev in ["ES", "MG", "RJ", "SP"]:
        return "Sudeste"
    elif abrev in ["PR", "RS", "SC"]:
        return "Sul"


uf["Região"] = uf["Abreviação"].apply(uf_abreviacao_to_regiao)

# %%
uf.head().info()

# %%

# Se PIB / Capita > 30.000
# +
# Mort Infantil < 15 / 1000
# +
# IDH (2010) > 700
# -> "Parece bom"

# Não parece bom

uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)


def looks_good(row):
    pib = row["PIB per capita (R$) (2015)"]
    mort_infantil = row["Mortalidade infantil (2016)"]
    idh = row["IDH (2010)"]

    if pib > 30000 and mort_infantil < 15 and idh > 700:
        return "Parece bom"
    return "Não parece bom"


uf["Cenário"] = uf.apply(looks_good, axis=1)
# %%
uf.loc[11]
# %%
