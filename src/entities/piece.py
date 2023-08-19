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
from math import sin, cos, pi

class Piece():
    def __init__(self, config: GameConfig, piece_type: PieceType, start_pos: Point = None) -> None:
        self.config = config
        self.type = piece_type
        self.origin = start_pos or self.init_origin(self.type)
        self.body = PIECE_STARTS[piece_type]
        self.rotation = RotationState()
    
    def init_origin(self, piece_type: PieceType) -> Point:
        return Point(BOARD_WIDTH//2-1, BOARD_HEIGHT-1)

    def get_positions_as_tuples(self):
        return (self.origin, *map(lambda v : v.add(self.origin), self.body))
    
    def get_body_as_tuples(self):
        return tuple(map(lambda x: x.xy, self.body))

    def get_positions_vector(self) -> tuple[Point, Point, Point, Point]:
        return tuple(map(lambda x: x.xy, self.get_positions_as_tuples()))
    
    def get_rotated(self, rotation_direction: RotationDirection):
        
        return (
            self.rotate_math(self.body[0],rotation_direction),
            self.rotate_math(self.body[1],rotation_direction),
            self.rotate_math(self.body[2],rotation_direction)
        )


    def rotate_math(self, p: Point,rotation_direction: RotationDirection) -> Point:
        bad_sin = lambda x: 1 if x==rotation_direction.CW else -1
        
        new_x = - p.y * bad_sin(rotation_direction)
        new_y =   p.x * bad_sin(rotation_direction)
        return Point(new_x,new_y)
    
    def move_origin_to(self, new_pos):
        return Piece(self.config, self.type, new_pos)

    def move(self, board, vector: Point) -> bool:
        tempPos = self.origin.add(vector)
        print('Move: ', self.move_origin_to(tempPos).get_positions_vector())

        if board.valid_place(self.move_origin_to(tempPos)):
            self.origin = tempPos
            return True
        else:
            return False
    
    def fall(self, board, speed: int = 1) -> bool:
        return self.move(board, Point(0, -speed))

    def strafe(self, board, horizontal: int) -> bool:
        return self.move(board, Point(horizontal, 0))