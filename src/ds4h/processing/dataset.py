from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

FOLDS = [
  {
    "train": [
      ("2005-01-01", "2015-12-31"),
      ("2018-01-01", "2020-06-30"),
    ],
    "test": [
      ("2020-06-01", "2020-12-31"),             
    ]
  },
  {
    "train": [
      ("2005-01-01", "2020-05-31"),
    ],
    "test": [
      ("2020-06-01", "2020-12-31"),             
    ]
  },
]

def create_folds_seq_with_year(df, intervals, n_months=3, n_years=2, city=None, use_year=False, month_poly_degree=None, other_filters=None):
  df = df.copy()
  
  if city:
    df = df[df.MUNNAME == city]
  
  if other_filters:
    for col, value in other_filters.items():
      if isinstance(value, list):
        df = df[df[col].apply(lambda x: x in value)]
      else:
        df = df[df[col] == value]

  df = df.groupby(["YEAR", "MONTH"]).count().sort_values(by=["YEAR", "MONTH"]).reset_index()
  df.MONTH = df.MONTH.apply(lambda d: dt.strptime(d, "%B").month)
  df["DATE"] = df[["YEAR", "MONTH"]].apply(lambda x: dt(x[0], x[1], 1), axis=1)
  df = df[["YEAR", "MONTH", "DATE", "DTNASC"]]
  X, Y, years = list(), list(), list()
  
  for start, end in intervals:
    start_date = dt.strptime(start, "%Y-%m-%d")
    end_date = dt.strptime(end, "%Y-%m-%d")

    for _, (year, month, date, cnt) in df.iterrows():
      date = dt(year, month, 1)
      if not (date >= start_date) and (date <= end_date):
        continue
      features = list()
      if use_year:
        features.append(year - 2000)
      missing_date = False
      for i in range(n_months):
        query_date = date - relativedelta(months=i+1)
        query_df = df[df.DATE == query_date]
        if len(query_df) == 0:
          missing_date = True
          break
        else:
          features.append(query_df["DTNASC"].item())
      for i in range(n_years):
        query_date = date - relativedelta(years=i+1)
        query_df = df[df.DATE == query_date]
        if len(query_df) == 0:
          missing_date = True
          break
        else:
          features.append(query_df["DTNASC"].item())
      if missing_date:
        continue
      
      if month_poly_degree:
        month_features = [month ** i for i in range(1, month_poly_degree)]
      else:
        month_features = [0] * 12
        month_features[month - 1] = 1
      
      features.extend(month_features)
      X.append(features)
      Y.append(cnt)
      years.append(year)
  X, Y, years = np.stack(X), np.array(Y).reshape(-1, 1), np.array(years)
  return X, Y, years
