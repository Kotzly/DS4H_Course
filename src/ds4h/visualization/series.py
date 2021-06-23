import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt
import numpy as np

DEFAULT_CITIES = ["Santos", "São Paulo", "Guaãra", "Dracena"] 

def plot_cities_series(df, cities=DEFAULT_CITIES, years=None, title=""):
    for city in cities:
        mlocator = mdates.MonthLocator()  # every month
        ylocator = mdates.YearLocator()  # every month
        yfmt = mdates.DateFormatter('%y')

        if years is None:
            years = df.YEAR.unique()

        plt.figure(figsize=(16, 5))
        for year in years:
            data_df = df[np.bitwise_and(df.MUNNAME == city, df.YEAR == year)].groupby(["YEAR", "MONTH"]).count().reset_index()
            data_df["MONTH"] = data_df.MONTH.apply(lambda d: dt.strptime(d, "%B").month)
            data_df["DATE"] = data_df[["YEAR", "MONTH"]].apply(lambda x: dt(x[0], x[1], 1), axis=1)
            data_df = data_df.sort_values(by="DATE")
            x, y = data_df["DATE"].values, data_df["DTNASC"].values

            plt.plot(x, y, label=str(year))
            plt.scatter(x, y)

        xaxis = plt.gca().xaxis
        xaxis.set_major_locator(ylocator)
        xaxis.set_major_formatter(yfmt)
        xaxis.set_minor_locator(mlocator)
        plt.xticks(rotation=90)
        plt.title(city + f": {title}")
        plt.legend(loc=6)
        plt.ylabel("Número de Nascidos Vivos")
        plt.xlabel("Ano")
        plt.grid()
        plt.show()


