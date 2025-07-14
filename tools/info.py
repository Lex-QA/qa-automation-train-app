from enum import Enum


class Info(str, Enum):
    SUCCESS = "success"
    SUCCESSFULLY_CHANGED = "User password successfully changed"

    def __str__(self):
        return self.value
