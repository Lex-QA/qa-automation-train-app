from enum import Enum


class AllureEpic(str, Enum):
    FILES = "Files service"
    GAMES = "Games service"
    ADMINISTRATION = "Administrator service"
