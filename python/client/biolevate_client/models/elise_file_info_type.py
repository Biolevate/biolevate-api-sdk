from enum import Enum


class EliseFileInfoType(str, Enum):
    ELISE_FILE = "ELISE_FILE"
    FILE = "FILE"
    FOLDER = "FOLDER"

    def __str__(self) -> str:
        return str(self.value)
