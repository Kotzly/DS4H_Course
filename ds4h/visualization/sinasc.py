from ds4h.processing.sinasc import SINASC_TRANSLATE_DICT
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def pct_lineplot(df, x_col, group_col, percentage=True, y_logscale=False, figsize=None):
  
  if figsize is None:
      figsize = (14, 5)
  plt.figure(figsize=figsize)
  ax = plt.gca()
  ax.grid()
  hue_order = list(SINASC_TRANSLATE_DICT[group_col].values()) if group_col in SINASC_TRANSLATE_DICT else None
  if percentage:
    pct2 = (100 * df.groupby([x_col, group_col]).size() / df.groupby([x_col]).size()).reset_index().rename({0:'Percentage'}, axis=1)
    plot = sns.lineplot(x=x_col, hue=group_col, y='Percentage', data=pct2, ax=ax, hue_order=hue_order)
    ticks = ax.get_yticks()
    ax.set_yticklabels([f"{x}%" for x in ticks])
  else:
    df = df.groupby([x_col, group_col]).count().reset_index()
    plot = sns.lineplot(data=df, x=x_col, y="DTNASC", hue=group_col, ax=ax, hue_order=hue_order)

  if y_logscale:
    ax.set_yscale("log")

  ax.set_ylabel("Count" if percentage else "Percentage [%]")
  ax.set_xlabel(x_col)

  ax.set_title(f"Count per {x_col} stratified by {group_col}")
  ax.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
  plt.xticks(rotation = 45)

  plt.show()
  plt.close()

def pct_plot(df, x_col, group_col, percentage=True, y_logscale=False, figsize=(14, 5)):
  if figsize is None:
      figsize = (14, 5)

  plt.figure(figsize=figsize)
  ax = plt.gca()
  ax.grid()

  def intersect_with(list1, list2):
    return [x for x in list1 if x in list2]

  order = intersect_with(list(SINASC_TRANSLATE_DICT[x_col].values()), df[x_col].unique()) if x_col in SINASC_TRANSLATE_DICT else None
  hue_order = intersect_with(list(SINASC_TRANSLATE_DICT[group_col].values()), df[group_col].unique()) if group_col in SINASC_TRANSLATE_DICT else None

  if percentage:
    group_df = (100 * df.groupby([x_col, group_col]).size() / df.groupby([x_col]).size()).reset_index().rename({0:'Percentage'}, axis=1)
    sns.barplot(data=group_df, x=x_col, hue=group_col, y='Percentage', ax=ax, order=order, hue_order=hue_order)
    ticks = ax.get_yticks()
    ax.set_yticklabels([f"{x}%" for x in ticks])
  else:
    group_df = df.groupby([x_col, group_col]).count().rename(columns={"DTNASC": "Count"})["Count"]
    sns.countplot(data=df, x=x_col, hue=group_col, ax=ax, order=order, hue_order=hue_order)

  if y_logscale:
    ax.set_yscale("log")

  ax.set_ylabel("Count" if percentage else "Percentage [%]")
  ax.set_xlabel(x_col)

  ax.set_title(f"Count per {x_col} stratified by {group_col}")
  ax.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
  ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)

  plt.show()
  plt.close()

  return group_df