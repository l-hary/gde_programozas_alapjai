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
    ax.scatter(x, y, color="blue", label="Adatpontok")
    ax.plot(x, prediction, color="red", label="Regressziós egyenes")

    # Format axes
    ax.set_xlabel("Lakáspiaci tranzakciók száma")
    ax.set_ylabel("Folyósított lakáshitelek száma")
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.legend()
    # TODO add title
    return ax


def generate_line_chart(x: pd.Series, y: pd.Series, ax: plt.Axes = None) -> plt.Axes:
    if ax is None:
        ax = plt.gca()  # creates a new ax if not provided
    x = x.astype(str)

    sns.lineplot(x=x, y=y, ax=ax, linestyle="--", marker="o", color="salmon")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    # Set fixed stepping for y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(100000))
    ax.set_ylim(bottom=4200000, top=4700000)
    # TODO add labels and title

    # Format y-axis numbers
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    # Add callouts (annotations)
    for i in range(len(x)):
        ax.annotate(
            text=f"{y.iloc[i]/1000000:,.2f}M",
            xy=(x.iloc[i], y.iloc[i]),
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
            rotation=50,
        )
    return ax


def generate_scatterplot() -> plt.Figure:
    pass
