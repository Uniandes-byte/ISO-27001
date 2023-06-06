from enum import Enum

class Score(Enum):
    OPTION_1 = "0%"
    OPTION_2 = "25%"
    OPTION_3 = "50%"
    OPTION_4 = "75%"
    OPTION_5 = "100%"
    OPTION_6 = "N/A"

class Parameter:
    def __init__(self, index:int, score:Score):
        self._index = index
        self._score = score

    @property
    def get_index(self) -> int:
        return self._index

    @property
    def get_score(self) -> Score:
        return self._score  
        
    @property
    def set_index(self, index:int) -> None:
        self._index = index

    @property
    def set_score(self, score:Score) -> None:
        self._score = score