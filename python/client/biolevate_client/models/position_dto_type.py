from enum import Enum


class PositionDtoType(str, Enum):
    BBOX = "BBOX"
    CELL = "CELL"
    LINE = "LINE"
    UNRECOGNIZED = "UNRECOGNIZED"

    def __str__(self) -> str:
        return str(self.value)
