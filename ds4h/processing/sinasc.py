from ds4h.data.city_ranking import CITY_CODE_DICT
from datetime import datetime as dt
import numpy as np
from functools import partial

SINASC_TRANSLATE_DICT = {
    "MONTH": {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "Septembet",
        10: "October",
        11: "November",
        12: "December"
    },
    "ESTCIVMAE": {
        1: "Single",
        2: "Married",
        3: "Widowed",
        4: "Divorced",
        5: "Stable union",
        9: "Unknown"
    },
    "RACACOR": {
        1: "White",
        2: "Black",
        3: "Asian",
        4: "Brown (Parda)",
        5: "Indigenous"
    },
    "RACACORMAE": {
        1: "White",
        2: "Black",
        3: "Asian",
        4: "Brown (Parda)",
        5: "Indigenous"
    },
    "IDANOMAL": {
        1: "Yes",
        2: "No",
        9: "Unknown"
    },
    "ESCMAE2010": {
        0: "None",
        1: "Fundamental I",
        2: "Fundamental II",
        3: "Ensino Médio",
        4: "Ensino superior incompleto",
        5: "Ensino superior completo",
        9: "Unknown"
    },
    "ESCMAE": {
        1: "None",
        2: "1 to 3 years",
        3: "4 to 7 years",
        4: "8 to 11 years",
        5: "12 or more years",
        9: "Unknown"
    },
    "PARTO": {
        1: "Vaginal",
        2: "Cesarean",
        9: "Unknown"
    }
}

def str_to_datetime(date):
  string = str(date)
  # 3022017 gives error (it reads the day as 30, but the month 22 does not exist), so we add a 0 to the start of the string
  if (string[0] != "0") and len(string) < 8:
    string = "0" + string
  return dt.strptime(string, "%d%m%Y")

def to_null(df, conditions):
  for col, condition in conditions:
    df.loc[condition, col] = np.nan
  return df

def age_to_group(x):
  if x < 20:
    return "A1"
  elif x < 35:
    return "A2"
  else:
    return "A3"

def process_sinasc(df, city_code_dict=None, nullify=True):
  if city_code_dict is None:
      city_code_dict = CITY_CODE_DICT

  df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]
  df.loc[:, "MUNNAME"] = df.CODMUNNASC.apply(city_code_dict.get)

  # Filtering for the rows that are from the selected cities
  df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]

  # Parsing date column
  df.loc[:, "DTNASC"] = df["DTNASC"].apply(str_to_datetime).astype("datetime64")

  # Categorization of age
  df["AGEGROUP"] = df["IDADEMAE"].apply(age_to_group)

  df["YEAR"] = df.DTNASC.dt.year
  df["MONTH"] = df.DTNASC.dt.month
  df["DAY"] = df.DTNASC.dt.day

  #Filtering inconsistent data
  if nullify:
    df = to_null(
      df,
      conditions = [
        ("QTDFILVIVO", df['QTDFILVIVO'] > 30.),
        ("QTDFILMORT", df['QTDFILMORT'] > 30.),
        ("IDADEMAE", df['IDADEMAE'] > 65),
        ("ESTCIVMAE", df['ESTCIVMAE'] > 5.),
        ("PARTO", df['PARTO'] > 2.),
        ("IDANOMAL", df['IDANOMAL'] > 2.),
        ("GESTACAO", df['GESTACAO'] > 6.),
        ("RACACOR", df['RACACOR'] > 5.),
        ("RACACORMAE", df['RACACORMAE'] > 5.),
        ("ESCMAE", df['ESCMAE'] > 5.)
      ]
    )

  return df

def code_to_str(df):

  dict_cols = SINASC_TRANSLATE_DICT.keys()
  df_cols = df.columns
  common_columns = set(dict_cols).intersection(df_cols)

  sub_fn = lambda key: SINASC_TRANSLATE_DICT[col].get(key, np.nan)

  for col in common_columns:
    df.loc[:, col] = df[col].apply(sub_fn)

  return df
