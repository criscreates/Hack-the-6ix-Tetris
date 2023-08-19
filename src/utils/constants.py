from enum import Enum, IntEnum
from collections import namedtuple
from math import pi

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.xy = (x,y)
    
    def add(self, v: tuple[int,int]) -> tuple[int,int]:
        return Point(v.x + self.x, v.y + self.y) 


POS4 = namedtuple('POS4', [
    'ORIGIN',
    'BODY',
])

BOARD_WIDTH = 10
BOARD_HEIGHT = 20

class PieceType (IntEnum):
    T = 1
    I = 2
    O = 3
    S = 4
    Z = 5
    J = 6
    L = 7

PIECE_STARTS = {
    int(PieceType.T): (Point(0,1) , Point(1,0) , Point(-1,0)),
    int(PieceType.I): (Point(0,1) , Point(0,-1), Point(0,-2)),
    int(PieceType.O): (Point(1,0) , Point(1,-1), Point(0,-1)),
    int(PieceType.S): (Point(-1,0), Point(0,1) , Point(1,1)),
    int(PieceType.Z): (Point(1,0) , Point(0,1) , Point(-1,1)),
    int(PieceType.J): (Point(0,-1), Point(0,1) , Point(-1,-1)),
    int(PieceType.L): (Point(0,-1), Point(0,1) , Point(1,-1)),
}


MoveDirection = Enum('MoveDirection', [
    'UP',
    'DOWN',
    'LEFT',
    'RIGHT',
])


RotationDirection = Enum('RotationDirection', [
    'CW',
    'CCW'
])

Cell = Enum('Cell', [
    'Placed',
    'Empty',
])

RotationLookUpTable = {
    int(PieceType.T): (
        ((0,1),(1,0),(-1,0)),
        ((0,1),(1,0),(0,-1)),
        ((0,-1),(1,0),(-1,0)),
        ((0,1),(1,0),(0,-1))),
    int(PieceType.I): (
        ((0,1) , (0,-1), (0,-2)),
        ((-2,0),(-1,0),(1,0)),
        ((0,2),(0,1),(0,-1)),
        ((2,0),(1,0),(-1,0))),
    int(PieceType.O): (
        ((1,0), (1,-1), (0,-1)),
        ((1,0), (1,-1), (0,-1)),
        ((1,0), (1,-1), (0,-1)),
        ((1,0), (1,-1), (0,-1))),
    int(PieceType.S): (
        ((-1,0), (0,1), (1,1)),
        ((0,1), (1,0), (1,-1)),
        ((0,-1),(-1,-1),(1,0)),
        ((-1,0), (-1,1), (0,-1))),
    int(PieceType.Z): (
        ((1,0), (0,1), (-1,1)),
        ((0,-1), (1,0), (1,1)),
        ((-1,0), (0,-1), (1,-1)),
        ((0,1), (-1,0), (-1,-1))),
    int(PieceType.J): (
        ((0,-1), (0,1), (-1,-1)),
        ((-1,1), (1,0), (-1,0)),
        ((0,-1), (0,1), (1,1)),
        ((-1,0), (1,0), (1,-1))),
    int(PieceType.L): (
        ((0,-1), (0,1), (1,-1)),
        ((-1,-1), (0,-1), (0,1)),
        ((-1,1), (0,1), (0,-1)),
        ((1,1), (-1,0), (1,0)))
}
