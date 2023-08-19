from enum import Enum, IntEnum
from collections import namedtuple

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def xy(self):
        return (self.x,self.y)
    
    def add(self, v: tuple[int,int]) -> tuple[int,int]:
        return Point(v.x + self.x, v.y + self.y) 


POS4 = namedtuple('POS4', [
    'ORIGIN',
    'BODY',
])

PieceType = {
    'T': 'T',
    'I': 'I',
    'O': 'O',
    'S': 'S',
    'Z': 'Z',
    'J': 'J',
    'L': 'L',
}

PIECE_STARTS = {
    'T': (Point(0,1) , Point(1,0) , Point(-1,0)),
    'I': (Point(0,1) , Point(0,-1), Point(0,-2)),
    'O': (Point(1,0) , Point(1,-1), Point(0,-1)),
    'S': (Point(-1,0), Point(0,1) , Point(1,1)),
    'Z': (Point(1,0) , Point(0,1) , Point(-1,1)),
    'J': (Point(0,-1), Point(0,1) , Point(-1,-1)),
    'L': (Point(0,-1), Point(0,1) , Point(1,-1)),
}


MoveDirection = Enum('MoveDirection', [
    'UP',
    'DOWN',
    'LEFT',
    'RIGHT',
])


RotationDirection = Enum('RotationDirection', [
    'CW',
    'CCW',
])


Cell = Enum('Cell', [
    'Placed',
    'None',
])
