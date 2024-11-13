from dataclasses import InitVar, dataclass, field

import pandas as pd  # only used for type hinting

from data.data_handler import load_and_preprocess_data


@dataclass
class StatisticalData:
    file_path: InitVar[str]
    data: pd.DataFrame = field(init=False)
    lr_x: pd.DataFrame = field(init=False)
    lr_y: pd.Series = field(init=False)
    line_x: pd.Series = field(init=False)
    line_y: pd.Series = field(init=False)

    def __post_init__(self, file_path: str) -> None:
        self.data = load_and_preprocess_data(file_path)
        self.lr_x = self.data[["Lakáspiaci tranzakció"]]
        self.lr_y = self.data["Folyósított lakáshitel, db"]
        self.line_x = self.data["Év"]
        self.line_y = self.data["Lakásállomány"]

    def set_line_y(self, column: str) -> None:
        self.line_y = self.data[column]

    def set_line_x(self, column: str) -> None:
        self.line_x = self.data[column]
