from enum import Enum


class AllureFeature(str, Enum):
    USERS = "Users"
    FILES = "Files"
    GAMES = "Games"
    AUTHENTICATION = "Authentication"
