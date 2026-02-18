from enum import Enum


class FSProviderExternalType(str, Enum):
    AZURE = "AZURE"
    GCS = "GCS"
    LEANEAR = "LEANEAR"
    LOCAL = "LOCAL"
    S3 = "S3"
    SHAREPOINT_ONLINE = "SHAREPOINT_ONLINE"

    def __str__(self) -> str:
        return str(self.value)
