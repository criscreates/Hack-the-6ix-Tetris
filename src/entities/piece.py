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
    def __init__(self, 
                 config: GameConfig, 
                 piece_type: PieceType, 
                 id: int, 
                 body: tuple[Point, Point, Point] = None,
                 rotation: RotationState = None, 
                 start_pos: Point = None,
                 ) -> None:
        self.config = config
        self.type = piece_type
        self.origin = start_pos or self.init_origin(self.type)
        self.body = body or PIECE_STARTS[piece_type]
        self.rotation = rotation or RotationState()
        self.id = id
    
    def init_origin(self, piece_type: PieceType) -> Point:
        return Point(BOARD_WIDTH//2-1, BOARD_HEIGHT-1)

    def get_positions_as_tuples(self):
        return (self.origin, *map(lambda v : v.add(self.origin), self.body))
    
    def get_body_as_tuples(self):
        return tuple(map(lambda x: x.xy, self.body))

    def get_positions_vector(self) -> tuple[Point, Point, Point, Point]:
        return tuple(map(lambda x: x.xy, self.get_positions_as_tuples()))
    
    def rotate(self, board, rotation_direction: RotationDirection):
        rotated = (
            self.rotate_math(self.body[0],rotation_direction),
            self.rotate_math(self.body[1],rotation_direction),
            self.rotate_math(self.body[2],rotation_direction)
        ) 

        if self.type == PieceType.O:
            return
        if not board.valid_place(
            self.move_to(
                self.origin,
                rotated,
                self.rotation)):
            return

        self.body = rotated

        if rotation_direction == RotationDirection.CCW:
            self.rotation.go_ccw()
        elif rotation_direction == RotationDirection.CW:
            self.rotation.go_cw()



    def rotate_math(self, p: Point,rotation_direction: RotationDirection) -> Point:
        bad_sin = lambda x: 1 if x==rotation_direction.CW else -1
        
        new_x = - p.y * bad_sin(rotation_direction)
        new_y =   p.x * bad_sin(rotation_direction)
        return Point(new_x,new_y)

        
    def move_to(self, new_origin, new_body, new_rotation):
        return Piece(self.config, self.type, self.id, body=new_body, rotation=new_rotation, start_pos=new_origin)


    def move(self, board, vector: Point) -> bool:
        tempPos = self.origin.add(vector)

        if board.valid_place(self.move_to(tempPos, self.body, self.rotation)):
            self.origin = tempPos
            return True
        else:
            return False
    
    def fall(self, board, speed: int = 1) -> bool:
        return self.move(board, Point(0, -speed))

    def strafe(self, board, horizontal: int) -> bool:
        return self.move(board, Point(horizontal, 0))