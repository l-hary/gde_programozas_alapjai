import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


def linear_regression(
    x: pd.DataFrame,
    y: pd.Series,
    prediction: np.ndarray,
    model: linear_model.LinearRegression,
) -> dict[plt.Figure, float]:

    fig, ax = plt.subplots()
    ax.scatter(x, y, color="blue", label="Actual Data")
    ax.plot(x, prediction, color="red", label="Regression Line")
    ax.set_xlabel("transactions")
    ax.set_ylabel("loans")
    ax.legend()

    return {
        "chart": fig,
        "coeffs": float(model.coef_),
        "intercept": float(model.intercept_),
        "r_squared": float(model.score(x, y)),
    }
