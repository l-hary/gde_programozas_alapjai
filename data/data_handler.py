import pandas as pd


def load_and_preprocess_data(file_path: str) -> pd.DataFrame:
    """
    Load and preprocess data from an Excel file.

    Parameters:
    file_path (str): Path to the Excel file.

    Returns:
    pd.DataFrame: Dataframe containing feature data and target data.
    """
    # Using Excel file, as csv from KSH have encoding issues
    try:
        df = pd.read_excel(file_path, skiprows=1)
        df = _drop_unnecessary_columns(file_path, df)
        df = df.rename(columns={"Lakásállomány, január 1.": "Lakásállomány"})
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except Exception as e:
        raise ValueError(f"An error occurred while loading the data: {e}")
    return df


def _drop_unnecessary_columns(file_path: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops rows where some of the data is missing and the last totals row.

    Parameters:
    file_path (str): Path to the data file.
    df (pd.DataFrame): DataFrame to process.

    Returns:
    pd.DataFrame: DataFrame with unnecessary columns dropped.
    """
    df = df.drop(df.index[0:7])
    df = df.drop(df.index[-1])
    return df


# TODO add more robust error handling
# TODO use pd.diff() instead of pd.shift()
def add_year_on_year_change(
    df: pd.DataFrame, target: str | list, result: str | list = None
) -> None:
    """
    Add year-on-year change columns to the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to modify.
    target (str | list): The target column(s) to calculate the year-on-year change for.
    result (str | list, optional): The name(s) of the result column(s). Defaults to None.

    Returns:
    None: The function modifies the DataFrame in place.
    """

    def add_default_suffix(df, target):
        df[f"{target} változása az előző évhez képest"] = df[target] - df[target].shift(
            1
        )

    # checks if a single column name was given
    if isinstance(target, str):
        if isinstance(result, str):  # checks if result column name was provided
            df[result] = df[target] - df[target].shift(1)
        else:  # generates column with default name
            add_default_suffix(df, target)

    if isinstance(target, list):  # checks if multiple column names were given
        # Checks if the length of the target list and result list matches for renaming
        if isinstance(result, list) and len(target) == len(result):
            for index, column in enumerate(target):
                df[result[index]] = df[column] - df[column].shift(1)
        else:  # generates columns with default names
            for column in target:
                add_default_suffix(df, column)
