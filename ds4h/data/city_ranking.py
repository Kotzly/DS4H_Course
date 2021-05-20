import pandas as pd
from pathlib import Path

_C = {
  3502101: 'Andradina',
  3502804: 'Araçatuba',
  3505708: 'Barueri',
  3514403: 'Dracena',
  3517406: 'Guaira',
  3524808: 'Jales',
  3546801: 'Santa Isabel',
  3548500: 'Santos',
  3548807: 'São Caetano do Sul',
  3549805: 'São José do Rio Preto',
  3550308: 'São Paulo'
}
CITY_CODE_DICT = {(cod // 10): name for cod, name in _C.items()}

def get_cities_dataframe():
    filepath = Path("../data/processed/indexes/municipios.csv")
    df = pd.read_csv(filepath, sep=";")
    df["taxa_de_incidencia"] = df["total_casos"] / df["populacao"]
    return df

def get_ranking_dataframe(min_population=30000):
    
    def compara(ai, aj):
        res = 0
        if (ai > aj):
            res = 1
        if (ai < aj):
            res = -1

        return res

    def compare(df, col):
        
        mc1 = []
        for i in df.index:
            ai = df.loc[i, col]
            aux = []
            for j in df.index:
                aj = df.loc[j, col]
                aux.append(compara(ai,aj))
            mc1.append(aux)

        dc1 = pd.DataFrame(data=mc1)
        return dc1

    full_df = get_cities_dataframe()
    df = full_df.copy()

    results = {}
    summed = None

    # for col in ("taxa_de_letalidade", "taxa_de_mortalidade", "taxa_de_incidencia", "populacao"):
    for col in ("taxa_de_letalidade", "taxa_de_mortalidade", "taxa_de_incidencia"):
        results[col] = compare(full_df, col)
        if summed is None:
            summed = results[col]
        else:
            summed = summed + results[col]
    
    df["total"] = summed.values.sum(axis=1)
    df = df[df["populacao"] > min_population].sort_values("total", ascending=False).head(10)
    if not "São Paulo" in df.municipio:
        sp_df = full_df[full_df.municipio == "São Paulo"]
        df = pd.concat([df, sp_df], axis=0)
    
    return df

def get_top_cities_from_df(df, code_col="Cod_IBGE", city_col="municipio"):
    city_dict = {(code // 10): name for _, (code, name) in df[[code_col, city_col]].iterrows()}
    return city_dict
