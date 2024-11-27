"""
This module provides functions to generate various types of charts for housing market analysis.

Functions:
----------
- set_chart_style: Set the style for the charts using seaborn and matplotlib settings.
- generate_lr_chart: Generate a chart for linear regression results.
- generate_line_chart: Generate a line chart for the given data.
- generate_bar_chart: Generate a bar chart for the given data.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Declaring global palette variable
PALETTE = sns.color_palette("crest") #kékeszöld szín 
TITLE_COLOR = "#202020"


def set_chart_style() -> None:
    """
    Set the style for the charts using seaborn and matplotlib settings.
    """

    sns.set_theme(style="darkgrid")
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica"]
    plt.tight_layout()


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
    plt.Axes: Matplotlib axes object with the chart.
    """
    if ax is None:  # creates a new ax if not provided
        ax = plt.gca()

    # Plot data points and regression line
    ax.scatter(x, y, color=PALETTE[1], label="Adatpontok")
    ax.plot(x, prediction, color=PALETTE[5], label="Regressziós egyenes")

    # Format axes

    ax.set_xlabel("Lakáspiaci tranzakciók")
    ax.set_ylabel("Folyósított lakáshitelek ")

    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.legend()

    # extra rácsozás
    ax.grid(which="major", color="gray", linestyle="--", linewidth=0.7)  # fő rácsvonal
    ax.minorticks_on()  # kis tick 
    ax.grid(which="minor", color="lightgray", linestyle=":", linewidth=0.5)  # kis rácsvonal

    # cím
    ax.set_title("Lineáris regresszió eredményei", fontsize=14, color=TITLE_COLOR)

    return ax


def generate_line_chart(x: pd.Series, y: pd.Series, ax: plt.Axes = None) -> plt.Axes:
    """
    Generate a line chart for the given data.

    Parameters:
    x (pd.Series): Series containing the x-axis data.
    y (pd.Series): Series containing the y-axis data.
    ax (plt.Axes, optional): Matplotlib Axes object to plot on. Defaults to None.

    Returns:
    plt.Axes: Matplotlib Axes object containing the chart.
    """
    if ax is None:
        ax = plt.gca()  # creates a new ax if not provided

    # drops trailing zeroes caused by years treated as floats, forces displaying all
    # element of years. Dirty solution, should use int conversion and ax.set_xticks
    x = x.astype(str)

    sns.lineplot(x=x, y=y, ax=ax, linestyle="--", marker="o", color=PALETTE[4])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    # Set fixed stepping for y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(100000))

    ax.set_ylim(float(y.min()) * 0.95, float(y.max()) * 1.05)
    # Add title

    ax.set_title("Lakásállomány alakulása évek szerint", fontsize=14, color=TITLE_COLOR)
    # Format y-axis numbers
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    #grid rács 
    ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
    
    # Add callouts (annotations)
    for i in range(len(x)):
        ax.annotate(
            text=f"{y.iloc[i]/1000000:,.2f}M",
            xy=(x.iloc[i], y.iloc[i]),
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
            fontsize=10,
            rotation=50,
        )
    return ax


def generate_bar_chart(x: pd.Series, y: pd.Series, ax: plt.Axes = None) -> plt.Axes:
    """
    Generate a bar chart for the given data.

    Parameters:
    x (pd.Series): Series containing the x-axis data.
    y (pd.Series): Series containing the y-axis data.
    ax (plt.Axes, optional): Matplotlib Axes object to plot on. Defaults to None.

    Returns:
    plt.Axes: Matplotlib Axes object containing the chart.
    """
    # drops trailing zeroes caused by years treated as floats, forces displaying all
    # element of years. Dirty solution, should use int conversion and ax.set_xticks
    x = x.astype(str)
    sns.barplot(x=x, y=y, ax=ax, color=PALETTE[0])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_ylim(-15000, 15000)
    ax.yaxis.set_major_locator(plt.MultipleLocator(5000))
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.set_title(
        "Megépült lakások számának változása az előző évhez képest viszonyítva",
        fontsize=14,
        color=TITLE_COLOR,
    )

    for p in ax.patches:
        ax.annotate(
            text=f"{p.get_height():,.0f}",
            xy=(p.get_x() + p.get_width() / 2.0, p.get_height()),
            va="center",
            ha="center",
            fontsize=10,
            rotation=50,
        )

    return ax