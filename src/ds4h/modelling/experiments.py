
from ds4h.processing.dataset import FOLDS, create_folds_seq_with_year
from ds4h.modelling.evaluation import evaluate, create_results_table
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from pathlib import Path
import json

N_YEARS = 2
N_MONTHS = 4
USE_YEAR = True
FILTERS_KWARGS_LIST = [
    {"ISWHITE": True},
    {"ISWHITE": False},
    {"ESCMAE": ["None", "1 to 3 years", "4 to 7 years"]},
    {"ESCMAE": ["8 to 11 years", "12 or more years"]},
    {"ESTCIVMAE": ["Married", "Stable Union"]},
    {"ESTCIVMAE": "Single"},
    {"AGEGROUP": "A1"},
    {"AGEGROUP": "A2"},
    {"AGEGROUP": "A3"},
    
]

def run_experiment_no_estratification(df, n_years=N_YEARS, n_months=N_MONTHS, use_year=USE_YEAR, save_path=None):
    results = []
    cities = list(df.MUNNAME.unique()) + [None]
    for _, fold in enumerate(FOLDS):
        result_dict = dict()
        for city in cities:
            train_intervals, test_intervals = fold["train"], fold["test"]
            x_train, y_train, _ = create_folds_seq_with_year(df, train_intervals, n_months=n_months, n_years=n_years, city=city, use_year=use_year, other_filters=None)
            x_test, y_test, _ = create_folds_seq_with_year(df, test_intervals, n_months=n_months, n_years=n_years, city=city, use_year=use_year, other_filters=None)

            model = LinearRegression()
            model.fit(x_train, y_train)
            r_test = evaluate(y_test, model.predict(x_test))
            r_train = evaluate(y_train, model.predict(x_train))

            result_dict[city] = {
                "model": model,
                "train": r_train,
                "test": r_test,
            }
        
        results.append(result_dict)

    result_df, formatted_df = create_results_table(results)
    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(exist_ok=True, parents=True)
        result_df.to_csv(save_path)

    best_idx = result_df.loc[:, ("Fold 1", "Test", "MAPE")].values.argmin()
    worst_idx = result_df.loc[:, ("Fold 1", "Test", "MAPE")].values.argmax()

    best_city = result_df.loc[:, ("", "", "Cidade")].values[best_idx]
    worst_city = result_df.loc[:, ("", "", "Cidade")].values[worst_idx]

    plt.clf()
    fig, axes= plt.subplots(1, 2, figsize=(16, 5))
    x_test, y_test, _ = create_folds_seq_with_year(df, test_intervals, n_months=n_months, n_years=n_years, city=city, use_year=use_year)
    for ax, city in zip(axes, [best_city, worst_city]):
        model = results[1][city]["model"]
        title = "{}: R2={:.3f}, MAPE={:.3f}".format(
            city,
            results[1][city]["test"]["R2"],
            results[1][city]["test"]["MAPE"],
        )
        ax.set_title(title)
        ax.plot(model.predict(x_test), label="Predição")
        ax.plot(y_test, label="Valor real")
        ax.grid(True)
        ax.legend()
    fig.suptitle("Test results for best (left) and worst (right) cities")
    plt.show()

    display(formatted_df)
    print(result_df.to_markdown())

    return result_df


def run_experiment_with_estratification(df, n_years=N_YEARS, n_months=N_MONTHS, use_year=USE_YEAR, filters_kwargs_list=FILTERS_KWARGS_LIST, save_folder=None):

    processed_df = df.copy()
    processed_df["ISWHITE"] = processed_df.RACACOR == "White"

    cities = list(df.MUNNAME.unique()) + [None]
        
    for filter_i, filters in enumerate(filters_kwargs_list):
        results = []
        for i, fold in enumerate(FOLDS):
            result_dict = dict()
            for city in cities:
                train_intervals, test_intervals = fold["train"], fold["test"]
                x_train, y_train, _ = create_folds_seq_with_year(processed_df, train_intervals, n_months=n_months, n_years=n_years, city=city, use_year=use_year, other_filters=filters)
                x_test, y_test, _ = create_folds_seq_with_year(processed_df, test_intervals, n_months=n_months, n_years=n_years, city=city, use_year=use_year, other_filters=filters)

                model = LinearRegression()
                model.fit(x_train, y_train)
                r_test = evaluate(y_test, model.predict(x_test))
                r_train = evaluate(y_train, model.predict(x_train))

                result_dict[city] = {
                    "model": model,
                    "train": r_train,
                    "test": r_test,
                }


            results.append(result_dict)

        print(filters)
        result_df, formatted_df = create_results_table(results)

        if save_folder:
            save_folder = Path(save_folder)
            save_folder.mkdir(exist_ok=True, parents=True)
            result_df.to_csv(save_folder / f"{fold}_{i}_filters_{filter_i}.csv")
            json.dump(filters, save_folder / f"filters_{filter_i}.json")

        display(formatted_df)
        print("\n\n")
