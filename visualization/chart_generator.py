import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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
