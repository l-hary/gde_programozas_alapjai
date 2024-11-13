import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import analysis.linear_regression
import data.data_model
import visualization.chart_generator


# ? remove unused main
def main() -> None:
    pass


def run_streamlit_app() -> None:
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(3, figsize=(8, 8))
    ksh_data = data.data_model.StatisticalData("data/stadat-lak0001.xlsx")
    lr_model = analysis.linear_regression.FittedModel(ksh_data.lr_x, ksh_data.lr_y)
    lr_chart = visualization.chart_generator.generate_lr_chart(
        ksh_data.lr_x, ksh_data.lr_y, lr_model.prediction, axes[0]
    )
    line_chart = visualization.chart_generator.generate_line_chart(
        ksh_data.line_x, ksh_data.line_y, axes[1]
    )
    plt.tight_layout()  # Fixes clipping on lower charts
    fig.canvas.draw()
    plt.show()
    st.write(f"R squared is {lr_model.r_squared: .2f}")
    st.write(fig)


if __name__ == "__main__":
    main()
