import pandas as pd
from pathlib import Path

SINASC_COLS = ["DTNASC", "QTDFILVIVO", "SEXO", "IDADEMAE", "PESO", "GRAVIDEZ", "CONSULTAS", "RACACOR", "CODMUNNASC", "ESTCIVMAE", "ESCMAE", "PARTO", "IDANOMAL"]

def process_raw_sinasc(csv_folder, save_path=None, cols=None):
    csv_folder = Path(csv_folder)
    cols = SINASC_COLS if cols is None else cols
    dfs = []
    for csv_filepath in csv_folder.glob("*.csv"):
        print("Loading", csv_filepath.name)
        df = pd.read_csv(csv_filepath, usecols=cols)[cols]
        dfs += [df]

    union_df = pd.concat(dfs, axis=0)
    if save_path is not None:
        union_df.to_csv(save_path)
    
    return union_df
