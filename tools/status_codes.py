from enum import Enum


class StatusCodes(str, Enum):
    BAD_REQUEST = "Bad Request"
    CREATED = "created"
    Forbidden = "Forbidden"
    NOT_FOUND = "Not Found"
    MOVED_PERMANENTLY = "Moved Permanently"
    UNAUTHORIZED = "Unauthorized"

    def __str__(self):
        return self.value
