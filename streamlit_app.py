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
    

    # Load data and models
    ksh_data = data.data_model.StatisticalData("data/stadat-lak0001.xlsx")
    lr_model = analysis.linear_regression.FittedModel(ksh_data.lr_x, ksh_data.lr_y)

    # Generate charts
    fig, axes = plt.subplots(3, figsize=(8, 8))
    lr_chart = visualization.chart_generator.generate_lr_chart(
        ksh_data.lr_x, ksh_data.lr_y, lr_model.prediction, axes[0]
    )
    line_chart = visualization.chart_generator.generate_line_chart(
        ksh_data.line_x, ksh_data.line_y, axes[1]
    )
    visualization.chart_generator.set_chart_style()
    
    st.write(f"R squared is {lr_model.r_squared: .2f}")
    st.pyplot(fig)

