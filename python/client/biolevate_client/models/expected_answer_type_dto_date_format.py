from enum import Enum


class ExpectedAnswerTypeDtoDateFormat(str, Enum):
    EUR = "EUR"
    ISO = "ISO"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
