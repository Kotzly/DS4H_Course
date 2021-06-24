import pandas as pd
from pathlib import Path
import numpy as np

SINASC_COLS = ["DTNASC", "QTDFILVIVO", "QTDFILMORT", "IDADEMAE", "RACACOR", "RACACORMAE", "CODMUNNASC", "ESTCIVMAE", "ESCMAE", "PARTO", "IDANOMAL", "GESTACAO"]

def join_sinasc_files(csv_folder, save_path=None, cols=None):
    csv_folder = Path(csv_folder)
    cols = SINASC_COLS if cols is None else cols

    union_df = None
    for csv_filepath in csv_folder.glob("*.csv"):

        print("Loading", csv_filepath.name)
        df = pd.read_csv(csv_filepath)
        for column in cols:
            if not column in df.columns:
                df[column] = np.nan
                print(f"\tFile did not have column {column}, filling with NaN's.")
        df = df[cols]

        union_df = df if union_df is None else pd.concat([union_df, df], axis=0)

    if save_path is not None:
        union_df.to_csv(save_path)
    
    return union_df

