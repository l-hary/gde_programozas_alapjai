from dataclasses import InitVar, dataclass, field

import pandas as pd  # only used for type hinting

from data.data_handler import load_and_preprocess_data


@dataclass
class StatisticalData:
    file_path: InitVar[str]
    data: pd.DataFrame = field(init=False)
    x: pd.DataFrame = field(init=False)
    y: pd.Series = field(init=False)

    def __post_init__(self, file_path) -> None:
        self.data = load_and_preprocess_data(file_path)
        self.x = self.data[["Lakáspiaci tranzakció"]]
        self.y = self.data["Folyósított lakáshitel, db"]
