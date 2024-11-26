import matplotlib.pyplot as plt
import streamlit as st

import analysis.linear_regression
import data.data_model
import visualization.chart_generator


def run_streamlit_app() -> None:
    st.set_page_config(
        page_title="Programozási Alapok",
        page_icon=":computer:",
    )
    st.title(":blue[Gábor Dénes Egyetem 2024]")
    st.write(":green[Programozási Alapok Projektfeladatot készítették:]")
    st.write(
        ":green[Balom Soma - T3JIXF, Háry László - GA790T, Ashwood Morrigan- GMQUVO, Bukur Norbert - NZIE3G]"
    )


    fig, axes = plt.subplots(3, figsize=(8, 8))
    # Load data and models
    ksh_data = data.data_model.StatisticalData("data/stadat-lak0001.xlsx")
    lr_model = analysis.linear_regression.FittedModel(
        ksh_data.lr_independent_x, ksh_data.lr_dependent_y
    )
    ksh_data.add_year_on_year_change_to_data(["Lakásállomány", "Épített lakás"])

    # Generate charts
    linear_regression_chart = visualization.chart_generator.generate_lr_chart(
        ksh_data.lr_independent_x, ksh_data.lr_dependent_y, lr_model.prediction, axes[0]

    )
    available_housing = visualization.chart_generator.generate_line_chart(
        ksh_data.x_axis, ksh_data.y_axis, axes[1]
    )

    ksh_data.set_y_axis("Épített lakás változása")
    new_builds_yoy_change = visualization.chart_generator.generate_bar_chart(
        x=ksh_data.x_axis[1:], y=ksh_data.y_axis, ax=axes[2]
    )

    st.write(f"R squared is {lr_model.r_squared: .2f}")
    visualization.chart_generator.set_chart_style()
    st.pyplot(fig)

