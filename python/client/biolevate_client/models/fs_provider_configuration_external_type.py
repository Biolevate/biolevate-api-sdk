from enum import Enum


class FSProviderConfigurationExternalType(str, Enum):
    AZURE = "AZURE"
    GCS = "GCS"
    LEANEAR = "LEANEAR"
    LOCAL = "LOCAL"
    S3 = "S3"
    SHAREPOINT_ONLINE = "SHAREPOINT_ONLINE"

    def __str__(self) -> str:
        return str(self.value)
