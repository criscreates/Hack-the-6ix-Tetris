from enum import Enum, IntEnum
from collections import namedtuple

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
    'T': ((0,1) , (1,0) , (-1,0)),
    'I': ((0,1) , (0,-1), (0,-2)),
    'O': ((1,0) , (1,-1), (0,-1)),
    'S': ((-1,0), (0,1) , (1,1)),
    'Z': ((1,0) , (0,1) , (-1,1)),
    'J': ((0,-1), (0,1) , (-1,-1)),
    'L': ((0,-1), (0,1) , (1,-1)),
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

RotationLookUpTable = {
    PieceType.T: (((0,1),(1,0),(-1,0))),
    PieceType.I: (((1,0), (1,-1), (0,-1))),
    PieceType.O: (((1,0), (1,-1), (0,-1))),
    PieceType.S: (((-1,0), (0,1), (1,1))),
    PieceType.Z: (((1,0), (0,1), (-1,1))),
    PieceType.J: (((0,-1), (0,1), (-1,-1))),
    PieceType.L: (((0,-1), (0,1), (1,-1)))
}
