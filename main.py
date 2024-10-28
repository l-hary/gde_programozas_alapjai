import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

import chart_generator as cgen


def main() -> None:
    # TODO: change hardcoded file path to a command line argument
    # xls file is used, as KSH csv files have encoding issues
    df = pd.read_excel("data/stadat-lak0001.xlsx", skiprows=1)

    # drop headers and rows with no data. df.replace() is intentionally not used
    df = df.drop(df.index[0:7])
    df = df.drop(df.index[-1])

    # assign x (feature) and y (target)
    x = df[["Lakáspiaci tranzakció"]]  # double brackets to get a dataframe
    y = df["Folyósított lakáshitel, db"]  # single brackets to get a series

    # create the model and fit it to the data
    model = linear_model.LinearRegression()
    model.fit(x, y)
    predicted_new_loans = model.predict(x)
    chart = cgen.linear_regression(x, y, predicted_new_loans, model)


if __name__ == "__main__":
    main()
