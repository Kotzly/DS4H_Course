from ds4h.data.city_ranking import CITY_CODE_DICT
from datetime import datetime as dt
import numpy as np

def parse_day(d):
  d = str(d)
  day, month, year = int(d[-8:-6]), int(d[-6:-4]), int(d[:-4])
  return day
def parse_month(d):
  d = str(d)
  day, month, year = int(d[-8:-6]), int(d[-6:-4]), int(d[:-4])
  return month
def parse_year(d):
  d = str(d)
  day, month, year = int(d[-8:-6]), int(d[-6:-4]), int(d[-4:])
  if year < 2000:
    year += 2000
  return year

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
    
    #Filtering inconsistent data
    if nullify:
      df = to_null(
        df,
        conditions = [
          ("QTDFILVIVO", df['QTDFILVIVO'] > 30),
          ("QTDFILMORT", df['QTDFILMORT'] > 30),
          ("QTDFILMORT", df['QTDFILMORT'] > 65),
          ("ESTCIVMAE", df['ESTCIVMAE'] > 5),
          ("PARTO", df['PARTO'] > 2.0),
          ("IDANOMAL", df['IDANOMAL'] > 2.0),
          ("GESTACAO", df['GESTACAO'] > 6.0),
          ("RACACOR", df['RACACOR'] > 5.0),
          ("RACACORMAE", df['RACACORMAE'] > 5.0)
        ]
      )

    return df
