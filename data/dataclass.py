from dataclasses import InitVar, dataclass, field

import pandas as pd


@dataclass
class DataAnalyzer:
    file_path: InitVar[str]
    data: pd.DataFrame = field(default=None)


def __post_init__(self, file_path) -> None:
    self.data = pd.read_excel(file_path)
