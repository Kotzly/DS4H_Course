from ds4h.data.city_ranking import CITY_CODE_DICT
from datetime import datetime as dt

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

def process_sinasc(df, city_code_dict=None):
    if city_code_dict is None:
        city_code_dict = CITY_CODE_DICT

    df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]
    df.loc[:, "MUNNAME"] = df.CODMUNNASC.apply(lambda x: city_code_dict[x])

    # Filtering for the rows that are from the selected cities
    df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]
    
    #remove missing data
    df = df.dropna()

    # Parsing date column
    df.loc[:, "DTNASC"] = df["DTNASC"].apply(str_to_datetime).astype("datetime64")
    
    #Filtering inconsistent data
    df = df[df['QTDFILVIVO']<=30]
    df = df[df['QTDFILMORT']<=30]
    df = df[df['QTDFILMORT']<=65]
    df = df[df['ESTCIVMAE']<=5]
    df = df[df['PARTO'] <= 2.0]
    df = df[df['IDANOMAL'] <= 2.0]
    df = df[df['GESTACAO'] <= 6.0]
    df = df[df['ESCMAE2010'] <= 5.0]

    df = df[df['RACACOR'] <= 5.0]
    df = df[df['RACACORMAE'] <= 5.0]

    return df
