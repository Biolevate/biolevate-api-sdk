from enum import Enum


class EliseAnnotationStatus(str, Enum):
    NOTVALID = "NOTVALID"
    VALID = "VALID"

    def __str__(self) -> str:
        return str(self.value)
