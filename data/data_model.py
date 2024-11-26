"""
This module defines the StatisticalData class for housing market analysis.

The class loads and preprocesses data from a given file path and provides
attributes for linear regression and line plotting.
"""

from dataclasses import InitVar, dataclass, field

import pandas as pd  # only used for type hinting

from data.data_handler import add_year_on_year_change, load_and_preprocess_data


@dataclass
class StatisticalData:
    """
    A class to represent statistical data for housing market analysis.

    Attributes:
    -----------
    file_path : InitVar[str]
        The path to the data file.
    data : pd.DataFrame
        The preprocessed data loaded from the file.
    lr_x : pd.DataFrame
        DataFrame containing the 'Lakáspiaci tranzakció' column for linear regression.
    lr_y : pd.Series
        Series containing the 'Folyósított lakáshitel, db' column for linear regression.
    x_series : pd.Series
        Series containing x column data for plotting. Defaults to Év.
    x_series : pd.Series
        Series containing the y column data for plotting. Defaults to Lakásállomány.
    """

    file_path: InitVar[str]
    data: pd.DataFrame = field(init=False)
    lr_independent_x: pd.DataFrame = field(init=False)
    lr_dependent_y: pd.Series = field(init=False)
    x_axis: pd.Series = field(init=False)
    y_axis: pd.Series = field(init=False)

    def __post_init__(self, file_path: str) -> None:
        """
        Post-initialization method to load and preprocess data from the given file path.

        Parameters:
        -----------
        file_path : str
            The path to the data file.
        """
        self.data = load_and_preprocess_data(file_path)
        self.lr_independent_x = self.data[["Lakáspiaci tranzakció"]]
        self.lr_dependent_y = self.data["Folyósított lakáshitel, db"]
        self.x_axis = self.data["Év"]
        self.y_axis = self.data["Lakásállomány"]

    def set_y_axis(self, column: str) -> None:
        """
        Set the y_axis attribute to a different column from the data.

        Parameters:
        column (str): The column name to set as y_axis.
        """
        self.y_axis = self.data[column]

    def set_x_axis(self, column: str) -> None:
        """
        Set the x_axis attribute to a different column from the data.

        Parameters:
        column (str): The column name to set as x_axis.
        """
        self.x_axis = self.data[column]

    def add_year_on_year_change_to_data(
        self, target: str | list, result: str | list = None
    ) -> None:
        """
        Add year-on-year change columns to the DataFrame (self.data).

        Parameters:
        target (str | list): The column(s) to calculate the year-on-year change for.
        result (str | list, optional): The name(s) of the result column(s). Defaults to None.
        """
        add_year_on_year_change(self.data, target, result)
