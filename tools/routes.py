from enum import Enum


class APIRoutes(str, Enum):
    USERS = "/api/user"
    FILES = "/api/files"
    GAMES = "/api/user/games"
    REGISTRATION = "/api/signup"
    AUTHENTICATION = "/api/login"

    def __str__(self):
        return self.value
