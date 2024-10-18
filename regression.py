import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

# TODO: change hardcoded file path to a command line argument


def main() -> None:

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

    generate_chart(x, y, predicted_new_loans, model)


def generate_chart(
    x: pd.DataFrame,
    y: pd.Series,
    prediction: np.ndarray,
    model: linear_model.LinearRegression,
) -> None:
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print(f"R-squared: {model.score(x, y):.2f}")
    plt.scatter(x, y, color="blue", label="Actual Data")
    plt.plot(x, prediction, color="red", label="Regression Line")
    plt.xlabel("transactions")
    plt.ylabel("loans")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
