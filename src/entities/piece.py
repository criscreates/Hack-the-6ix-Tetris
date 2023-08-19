from ..utils import GameConfig
from ..utils import RotationState
from ..utils import PieceType, Point, PIECE_STARTS, POS4, RotationLookUpTable, RotationDirection 
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
    def __init__(self, config: GameConfig, piece_type: PieceType, pos4: POS4 = None) -> None:
        self.config = config
        self.type = piece_type
        self.pos4 = pos4 or self.init_pos4(self.type)
        self.rotation = RotationState()
    
    def init_pos4(self, piece_type: PieceType) -> POS4:
        return POS4(
            Point(BOARD_WIDTH//2-1, BOARD_HEIGHT-1),
            PIECE_STARTS[piece_type]
        )

    def get_positions(self):
        origin = self.pos4.ORIGIN
        return (origin, *map(lambda v : v.add(origin), self.pos4.BODY))
    
    def get_Rotated(self, rotation_direction: RotationDirection):
        
        return (
            self.rotate_math(self.BODY[0],rotation_direction),
            self.rotate_math(self.BODY[1],rotation_direction),
            self.rotate_math(self.BODY[2],rotation_direction)
        )


    def rotate_math(o_point: Point,rotation_direction: RotationDirection) -> Point:
        x = o_point.x
        y = o_point.y
        new_x = 0
        new_y = 0
        
        new_x = x*cos(int(rotation_direction)) - y*sin(int(rotation_direction))
        new_y = x*sin(int(rotation_direction)) - y*cos(int(rotation_direction))
        return Point(new_x,new_y)

    def get_positions_vector(self) -> tuple[Point, Point, Point, Point]:
        return tuple(map(lambda x: x.xy, self.get_positions()))
    
    def move_to(self, pos4: POS4):
        return Piece(self.config, self.type, pos4)

    def move(self, board, vector: Point) -> bool:
        tempPos = POS4(self.pos4.ORIGIN.add(vector), self.pos4.BODY)
        print('Move: ', self.move_to(tempPos).get_positions_vector())

        if board.valid_place(self.move_to(tempPos)):
            self.pos4 = tempPos
            return True
        else:
            return False
    
    def fall(self, board, speed: int = 1) -> bool:
        return self.move(board, Point(0, -speed))

    def strafe(self, board, horizontal: int) -> bool:
        return self.move(board, Point(horizontal, 0))