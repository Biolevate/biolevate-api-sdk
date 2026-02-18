from enum import Enum


class CreateItemRequestType(str, Enum):
    FOLDER = "FOLDER"

    def __str__(self) -> str:
        return str(self.value)
