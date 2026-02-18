from enum import Enum


class ExpectedAnswerTypeDtoDecimalPrecision(str, Enum):
    FIVE_DECIMALS = "FIVE_DECIMALS"
    FOUR_DECIMALS = "FOUR_DECIMALS"
    ONE_DECIMAL = "ONE_DECIMAL"
    THREE_DECIMALS = "THREE_DECIMALS"
    TWO_DECIMALS = "TWO_DECIMALS"
    UNRECOGNIZED = "UNRECOGNIZED"
    ZERO_DECIMALS = "ZERO_DECIMALS"

    def __str__(self) -> str:
        return str(self.value)
