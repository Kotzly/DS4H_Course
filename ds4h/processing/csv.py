import pandas as pd
from pathlib import Path

SINASC_COLS = ["DTNASC", "QTDFILVIVO", "SEXO", "IDADEMAE", "PESO", "GRAVIDEZ", "CONSULTAS", "RACACOR", "CODMUNNASC", "ESTCIVMAE", "ESCMAE", "PARTO", "IDANOMAL"]

def process_raw_sinasc(csv_folder, save_path=None, cols=None):
    csv_save_folder = Path(csv_folder)
    save_path = csv_folder / "union.csv" if save_path is None else Path(save_path)
    cols = SINASC_COLS if cols is None else cols
    dfs = []
    for csv_filepath in csv_save_folder.glob("*.csv"):
        if csv_filepath.name == union_csv_filename:
            continue
        print("Loading", csv_filepath.name)
        df = pd.read_csv(csv_filepath, usecols=cols)
        sorted_cols = list(sorted(df.columns))
        dfs += [df]

    union_df = pd.concat([union_df, df])
    union_df.to_csv(save_path)
