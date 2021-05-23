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
  all_cond = conds[0].values
  for cond in conds[1:]:
    all_cond = np.bitwise_and(all_cond, cond)
  return df[all_cond]

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
    df.loc[:, "MUNNAME"] = df.CODMUNNASC.apply(lambda x: city_code_dict[x])

    # Filtering for the rows that are from the selected cities
    df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]

    # Parsing date column
    df.loc[:, "DTNASC"] = df["DTNASC"].apply(str_to_datetime).astype("datetime64")
        
    #Filtering inconsistent data
    if nullify:
      df = to_null(
        df,
        conditions = [
          df['QTDFILVIVO'] <= 30,
          df['QTDFILMORT'] <= 30,
          df['QTDFILMORT'] <= 65,
          df['ESTCIVMAE'] <= 5,
          df['PARTO'] <= 2.0,
          df['IDANOMAL'] <= 2.0,
          df['GESTACAO'] <= 6.0,
          df['RACACOR'] <= 5.0,
          df['RACACORMAE'] <= 5.0
        ]
      )

    return df
