from dataclasses import InitVar, dataclass, field

import numpy as np
import pandas as pd
from sklearn import linear_model


@dataclass
class FittedModel:
    x: InitVar[pd.DataFrame]
    y: InitVar[pd.Series]
    model: linear_model.LinearRegression = field(init=False)
    coefficient: np.ndarray = field(init=False)
    intercept: float | np.ndarray = field(init=False)
    r_squared: float = field(init=False)
    prediction: np.ndarray = field(init=False)

    def __post_init__(self, x, y) -> None:
        self._fit_model(x, y)
        self._set_model_parameters(x, y)

    def _fit_model(self, x, y) -> None:
        self.model = linear_model.LinearRegression()
        self.model.fit(x, y)
        self.prediction = self.model.predict(x)

    def _set_model_parameters(self, x, y):
        self.coefficient = self.model.coef_
        self.intercept = self.model.intercept_
        self.r_squared = self.model.score(x, y)
