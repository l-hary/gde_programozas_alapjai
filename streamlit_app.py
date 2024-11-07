import streamlit as st

import data.data_handler as dacq
import visualization.chart_generator as cgen


# ? remove unused main
def main() -> None:
    pass


def run_streamlit_app() -> None:

    # TODO: change hardcoded file path to a command line argument
    # ? use st.file_uploader
    ksh_data = dacq.load_and_preprocess_data("data/stadat-lak0001.xlsx")

    # assign x (feature) and y (target)
    x = ksh_data[["Lakáspiaci tranzakció"]]  # double brackets to get a dataframe
    y = ksh_data["Folyósított lakáshitel, db"]  # single brackets to get a series

    fitted_model = cgen.generate_fitted_lr_model(x, y)
    lr_data = cgen.get_lr_model_data(fitted_model, x, y)
    prediction = lr_data["prediction"]
    lr_chart = cgen.generate_lr_chart(x, y, prediction)

    st.write(f"R squared is {lr_data["r_squared"]: .2f}")
    st.write(lr_chart)


if __name__ == "__main__":
    main()
