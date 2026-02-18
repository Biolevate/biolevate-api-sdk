from enum import Enum


class ExpectedAnswerTypeDtoDataType(str, Enum):
    BOOL = "BOOL"
    DATE = "DATE"
    ENUM = "ENUM"
    FLOAT = "FLOAT"
    INT = "INT"
    STRING = "STRING"
    UNRECOGNIZED = "UNRECOGNIZED"

    def __str__(self) -> str:
        return str(self.value)
