
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import pandas as pd
import numpy as np

def mean_absolute_percentage_error(y_true, y_pred):
  return np.mean(abs(y_pred - y_true) / y_true)

def evaluate(y_true, y_pred):
  metrics = {
      "R2": r2_score(y_true, y_pred),
      "MAE": mean_absolute_error(y_true, y_pred),
      "MSE": mean_squared_error(y_true, y_pred),
      "MAPE": mean_absolute_percentage_error(y_true, y_pred)
  }
  return metrics

def create_results_table(results):
  line = list()
  table = list()
  cities = results[0].keys()
  for city in cities:
    header = list()
    line = [city,]
    for _, result_dict in enumerate(results):
      train_r, test_r = result_dict[city]["train"], result_dict[city]["test"]
      metrics_train, metrics_test = [train_r[metric] for metric in ["R2", "MAPE"]], [test_r[metric] for metric in ["R2", "MAPE"]], 
      metrics = metrics_train + metrics_test
      line.extend(metrics)
    table.append(line)
  header = [
    [""] + ["Fold 0"] * 4 + ["Fold 1"] * 4,
    [""] + ["Train", "Train", "Test", "Test"] * 2,
    ["Cidade"] + ["R2", "MAPE"] * 4,    
  ]
  cols = pd.MultiIndex.from_tuples(tuple(zip(*header)))
  results_df = pd.DataFrame(table, columns=cols).round(3)

  results_df.loc[:, ("", "", "Analysis")] = None
  good_train = np.bitwise_and(results_df.loc[:, ("Fold 1", "Train", "MAPE")] <= .2, results_df.loc[:, ("Fold 1", "Train", "R2")] >= .5)
  good_test = results_df.loc[:, ("Fold 1", "Test", "MAPE")] <= .1
  results_df.loc[:, ("", "", "Analysis")][~good_train] = "N"
  results_df.loc[:, ("", "", "Analysis")][np.bitwise_and(good_train, ~good_test)] = "V"
  results_df.loc[:, ("", "", "Analysis")][np.bitwise_and(good_train, good_test)] = "X"

  def highlight_r2(x):
    return ['font-weight: bold' if v > 0.5 else '' for v in x]

  def highlight_mape(x):
    return ['font-weight: bold' if v < 0.05 else '' for v in x]

  return results_df, results_df.style\
    .apply(highlight_r2, subset=pd.IndexSlice[:, [(f"Fold {fold_index}", f"{fold}", "R2") for fold_index in range(2) for fold in ("Train", "Test")]])\
    .apply(highlight_mape, subset=pd.IndexSlice[:, [(f"Fold {fold_index}", f"{fold}", "MAPE") for fold_index in range(2) for fold in ("Train", "Test")]])

