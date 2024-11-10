import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def generate_lr_chart(
    x: pd.DataFrame,
    y: pd.Series,
    prediction: np.ndarray,
    ax: plt.Axes = None,
) -> plt.Axes:
    """
    Generate a chart for linear regression results.

    Parameters:
    x (pd.DataFrame): Feature data.
    y (pd.Series): Target data.
    prediction (np.ndarray): Predicted values from the model.

    Returns:
    plt.Figure: Matplotlib figure object containing the chart.
    """
    if ax is None:  # creates a new ax if not provided
        ax = plt.gca()
    ax.scatter(x, y, color="blue", label="Actual Data")
    ax.plot(x, prediction, color="red", label="Regression Line")
    ax.set_xlabel("Transactions")
    ax.set_ylabel("Loans")
    ax.legend()
    # TODO add labels and title
    return ax


def generate_line_chart(x: pd.Series, y: pd.Series, ax: plt.Axes = None) -> plt.Axes:
    if ax is None:
        ax = plt.gca()  # creates a new ax if not provided
    x = x.astype(str)
    sns.lineplot(x=x, y=y, ax=ax)
    ax.set_xticklabels(
        ax.get_xticklabels(), rotation=45
    )  # Rotate for better readability
    # TODO add labels and title
    # TODO format y axis numbers

    return ax


def generate_scatterplot() -> plt.Figure:
    pass
