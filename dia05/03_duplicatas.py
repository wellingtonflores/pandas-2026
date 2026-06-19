# %%
import pandas as pd

# %%
df = pd.DataFrame(
    {
        "nome": ["wel", "rafa", "isabel", "wel"],
        "sobrenome": ["flores", "schneider", "cardoso", "flores"],
        "salario": [800, 1000, 10000, 801],
    }
)

df
# %%
df = df.sort_values("salario", ascending=False).drop_duplicates(
    keep="last", subset=["nome", "sobrenome"]
)


# %%
