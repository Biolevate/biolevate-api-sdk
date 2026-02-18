from enum import Enum


class ItemReferenceType(str, Enum):
    FILE = "FILE"
    FOLDER = "FOLDER"

    def __str__(self) -> str:
        return str(self.value)
