import streamlit as st

import analysis.linear_regression
import data.data_model
import visualization.chart_generator


# ? remove unused main
def main() -> None:
    pass


def run_streamlit_app() -> None:

    ksh_data = data.data_model.StatisticalData("data/stadat-lak0001.xlsx")
    lr = analysis.linear_regression.FittedModel(ksh_data.x, ksh_data.y)
    lr_chart = visualization.chart_generator.generate_lr_chart(
        ksh_data.x, ksh_data.y, lr.prediction
    )

    st.write(f"R squared is {lr.r_squared: .2f}")
    st.write(lr_chart)


if __name__ == "__main__":
    main()
