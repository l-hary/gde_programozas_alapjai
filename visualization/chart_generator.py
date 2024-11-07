import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


def generate_fitted_lr_model(
    x: pd.DataFrame, y: pd.Series
) -> linear_model.LinearRegression:
    """
    Generate and fit a linear regression model.

    Parameters:
    x (pd.DataFrame): Feature data.
    y (pd.Series): Target data.

    Returns:
    linear_model.LinearRegression: Fitted linear regression model.
    """
    model = linear_model.LinearRegression()
    model.fit(x, y)

    return model


def get_lr_model_data(
    model: linear_model.LinearRegression,
    x: pd.DataFrame,
    y: pd.Series,
) -> dict[str, float | np.ndarray]:
    """
    Get data and metrics from a linear regression model.

    Parameters:
    model (linear_model.LinearRegression): Fitted linear regression model.
    x (pd.DataFrame): Feature data.
    y (pd.Series): Target data.

    Returns:
    Dict[str, Union[float, np.ndarray]]: Dictionary containing model metrics and predictions.
    """
    metrics = {
        "coefficient": float(model.coef_),
        "intercept": float(model.intercept_),
        "r_squared": float(model.score(x, y)),
        "prediction": model.predict(x),
    }
    return metrics


def generate_lr_chart(
    x: pd.DataFrame,
    y: pd.Series,
    prediction: np.ndarray,
) -> plt.Figure:
    """
    Generate a chart for linear regression results.

    Parameters:
    x (pd.DataFrame): Feature data.
    y (pd.Series): Target data.
    prediction (np.ndarray): Predicted values from the model.

    Returns:
    plt.Figure: Matplotlib figure object containing the chart.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y, color="blue", label="Actual Data")
    ax.plot(x, prediction, color="red", label="Regression Line")
    ax.set_xlabel("transactions")
    ax.set_ylabel("loans")
    ax.legend()
    return fig
