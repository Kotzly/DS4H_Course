from ds4h.data.city_ranking import CITY_CODE_DICT

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

def process_sinasc(df, city_code_dict=None):
    if city_code_dict is None:
        city_code_dict = CITY_CODE_DICT
    

    df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]
    df["MUNNAME"] = df.CODMUNNASC.apply(lambda x: city_code_dict[x])

    df = df[df.CODMUNNASC.apply(lambda x: x in city_code_dict.keys())]
    df["YEAR"], df["MONTH"], df["DAY"] = 0, 0, 0
    df["DAY"] = df.DTNASC.apply(parse_day)
    df["MONTH"] = df.DTNASC.apply(parse_month)
    df["YEAR"] = df.DTNASC.apply(parse_year)
    df["CITYNAME"] = df.CODMUNNASC.apply(lambda x: city_code_dict[x])

    return df