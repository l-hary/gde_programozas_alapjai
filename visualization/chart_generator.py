import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Apply a consistent, slightly darker theme
sns.set_theme(style="darkgrid", rc={
    "axes.facecolor": "#e0e0e0",  # Slightly darker grey background
    "grid.color": "#808080",      # Medium-dark gridlines
    "axes.edgecolor": "#4d4d4d",  # Subtle axis edges
    "axes.labelcolor": "#202020", # Darker axis labels
    "xtick.color": "#202020",
    "ytick.color": "#202020",
})
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica"]

# Create a color palette
palette = sns.color_palette("coolwarm", as_cmap=False)

def generate_lr_chart(
    x: pd.Series,
    y: pd.Series,
    prediction: np.ndarray,
    ax: plt.Axes = None,
) -> plt.Axes:
    """
    Generate a chart for linear regression results.

    Parameters:
    x (pd.Series or pd.DataFrame): Feature data (Lakáspiaci tranzakciók száma).
    y (pd.Series): Target data (Folyósított lakáshitelek száma).
    prediction (np.ndarray): Predicted values from the model.
    ax (plt.Axes): Optional matplotlib axes object.

    Returns:
    plt.Axes: Matplotlib axes object with the chart.
    """
    if ax is None:  # creates a new ax if not provided
        ax = plt.gca()

    # Ensure x is a single-dimensional array (use the first column if it's multi-dimensional)
    if isinstance(x, pd.DataFrame):
        x = x.iloc[:, 0]  # Select the first column for plotting

    # Plot data points and regression line
    ax.scatter(x, y, color=palette[2], alpha=0.9, label="Adatpontok")  # Slightly darker
    ax.plot(x, prediction, color=palette[5], alpha=0.8, label="Regressziós egyenes")

    # Format axes
    ax.set_xlabel("Lakáspiaci tranzakciók száma")
    ax.set_ylabel("Folyósított lakáshitelek száma")
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.legend()

    # Add a title
    ax.set_title("Lineáris regresszió eredményei", fontsize=14, color="#202020")

    # Set dynamic axis limits
    ax.set_xlim(float(x.min()) * 0.95, float(x.max()) * 1.05)
    ax.set_ylim(float(y.min()) * 0.95, float(y.max()) * 1.05)

    return ax


def generate_line_chart(x: pd.Series, y: pd.Series, ax: plt.Axes = None) -> plt.Axes:
    if ax is None:
        ax = plt.gca()  # creates a new ax if not provided
    x = x.astype(str)

    sns.lineplot(x=x, y=y, ax=ax, linestyle="--", marker="o", color=palette[3], alpha=0.9)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    # Set fixed stepping for y-axis
    ax.yaxis.set_major_locator(plt.MultipleLocator(100000))
    ax.set_ylim(float(y.min()) * 0.95, float(y.max()) * 1.05)

    # Add labels and title
    ax.set_xlabel("Évek", fontsize=12, color="#202020")
    ax.set_ylabel("Lakásállomány (db)", fontsize=12, color="#202020")
    ax.set_title("Lakásállomány alakulása évek szerint", fontsize=14, color="#202020")

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
