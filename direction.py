from enum import Enum


class Direction(str, Enum):
    UP = 'U',
    DOWN = 'D',
    FRONT = 'F',
    BACK = 'B',
    LEFT = 'L',
    RIGHT = 'R'
