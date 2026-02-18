from enum import Enum


class JobStatus(str, Enum):
    ABORTED = "ABORTED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    UNRECOGNIZED = "UNRECOGNIZED"

    def __str__(self) -> str:
        return str(self.value)
