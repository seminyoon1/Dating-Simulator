from enum import Enum

class GameStates(Enum):
    START = 1
    TITLE = 0
    QUIT = -1
    GAME = 2
    ENEMY = 3
    RECORD = 4
    SETTINGS = 5
    MUSIC = 6