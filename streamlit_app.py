import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import analysis.linear_regression
import data.data_model
import visualization.chart_generator


def run_streamlit_app() -> None:
    sns.set_style("whitegrid")  # Ensures a consistent style for all plots
    fig, axes = plt.subplots(3, figsize=(8, 8))
    
    # Load data and models
    ksh_data = data.data_model.StatisticalData("data/stadat-lak0001.xlsx")
    lr_model = analysis.linear_regression.FittedModel(ksh_data.lr_x, ksh_data.lr_y)
    
    # Generate charts using updated functions
    visualization.chart_generator.generate_lr_chart(
        ksh_data.lr_x, ksh_data.lr_y, lr_model.prediction, axes[0]
    )
    visualization.chart_generator.generate_line_chart(
        ksh_data.line_x, ksh_data.line_y, axes[1]
    )
    
    # Adjust layout to prevent clipping
    plt.tight_layout()
    
    # Streamlit rendering
    st.write(f"R squared is {lr_model.r_squared: .2f}")
    st.pyplot(fig)  # Use Streamlit's method to render the matplotlib figure


if __name__ == "__main__":
    run_streamlit_app()