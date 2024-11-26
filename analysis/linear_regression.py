"""
Module for performing linear regression analysis.
This module contains classes and functions to fit a linear regression model
and make predictions based on the model.
"""

from dataclasses import InitVar, dataclass, field

import numpy as np
import pandas as pd
from sklearn import linear_model


@dataclass
class FittedModel:
    """
    A class used to represent a fitted linear regression model.

    Attributes
    ----------
    x : pd.DataFrame
        The independent variable data.
    y : pd.Series
        The dependent variable data.
    model : linear_model.LinearRegression
        The linear regression model.
    coefficient : np.ndarray
        The coefficients of the linear regression model.
    intercept : float | np.ndarray
        The intercept of the linear regression model.
    r_squared : float
        The R-squared value of the model.
    prediction : np.ndarray
        The predicted values from the linear regression model.
    """

    x: InitVar[pd.DataFrame]
    y: InitVar[pd.Series]
    model: linear_model.LinearRegression = field(init=False)
    coefficient: np.ndarray = field(init=False)
    intercept: float | np.ndarray = field(init=False)
    r_squared: float = field(init=False)
    prediction: np.ndarray = field(init=False)

    def __post_init__(self, x, y) -> None:
        """
        Initializes the FittedModel with independent and dependent variables,
        fits the model, and sets the model parameters.

        Parameters
        ----------
        x : pd.DataFrame
            The independent variable data.
        y : pd.Series
            The dependent variable data.
        """
        self._fit_model(x, y)
        self._set_model_parameters(x, y)

    def _fit_model(self, x, y) -> None:
        """
        Fits a linear regression model to the data.

        Parameters
        ----------
        x : pd.DataFrame
            The independent variable data.
        y : pd.Series
            The dependent variable data.
        """
        self.model = linear_model.LinearRegression()
        self.model.fit(x, y)
        self.prediction = self.model.predict(x)

    def _set_model_parameters(self, x, y):
        """
        Sets the parameters of the linear regression model.

        Parameters
        ----------
        x : pd.DataFrame
            The independent variable data.
        y : pd.Series
            The dependent variable data.
        """
        self.coefficient = self.model.coef_
        self.intercept = self.model.intercept_
        self.r_squared = self.model.score(x, y)
