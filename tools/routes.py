from enum import Enum


class APIRoutes(str, Enum):
    USER = "/api/user"
    USERS = "/api/users"
    FILES = "/api/files"
    GAMES = "/api/user/games"
    REGISTRATION = "/api/signup"
    AUTHENTICATION = "/api/login"
    STATUS_CODES = "/api"

    def __str__(self):
        return self.value
