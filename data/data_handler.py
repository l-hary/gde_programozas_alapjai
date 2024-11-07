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
        df = df.drop(df.index[0:7])
        df = df.drop(df.index[-1])
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except Exception as e:
        raise ValueError(f"An error occurred while loading the data: {e}")
    return df
