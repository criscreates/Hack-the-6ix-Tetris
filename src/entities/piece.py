from ..utils import GameConfig
from ..utils import RotationState
from ..utils import (
    PieceType, 
    Point, 
    PIECE_STARTS, 
    POS4, 
    RotationLookUpTable, 
    RotationDirection,
    BOARD_HEIGHT,
    BOARD_WIDTH,
) 
from math import sin, cos

class Piece():
    def __init__(self, config: GameConfig, piece_type: PieceType, start_pos: Point = None) -> None:
        self.config = config
        self.type = piece_type
        self.origin = start_pos or self.init_origin(self.type)
        self.body = PIECE_STARTS[piece_type]
        self.rotation = RotationState()
    
    def init_origin(self, piece_type: PieceType) -> Point:
        return Point(BOARD_WIDTH//2-1, BOARD_HEIGHT-1)

    def get_positions(self):
        return (self.origin, *map(lambda v : v.add(self.origin), self.body))
    
    def get_rotated(self, rotation_direction: RotationDirection):
        self.body[1].x

    def rotate_math(o_point: Point,rotation_direction: RotationDirection):
        pass

    def get_positions_vector(self) -> tuple[Point, Point, Point, Point]:
        return tuple(map(lambda x: x.xy, self.get_positions()))
    
    def move_to(self, new_pos):
        return Piece(self.config, self.type, new_pos)

    def move(self, board, vector: Point) -> bool:
        tempPos = self.origin.add(vector)
        print('Move: ', self.move_to(tempPos).get_positions_vector())

        if board.valid_place(self.move_to(tempPos)):
            self.origin = tempPos
            return True
        else:
            return False
    
    def fall(self, board, speed: int = 1) -> bool:
        return self.move(board, Point(0, -speed))

    def strafe(self, board, horizontal: int) -> bool:
        return self.move(board, Point(horizontal, 0))