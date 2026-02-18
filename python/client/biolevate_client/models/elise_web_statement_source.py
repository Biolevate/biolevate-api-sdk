from enum import Enum


class EliseWebStatementSource(str, Enum):
    BRAVE = "BRAVE"
    UNRECOGNIZED = "UNRECOGNIZED"
    WEB = "WEB"
    WIKIPEDIA = "WIKIPEDIA"

    def __str__(self) -> str:
        return str(self.value)
