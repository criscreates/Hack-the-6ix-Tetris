from ..utils import GameConfig
from ..utils import RotationState
<<<<<<< HEAD
from ..utils import PieceType, Point, PIECE_STARTS, POS4, RotationLookUpTable, RotationDirection 
from math import sin, cos
=======
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
>>>>>>> 85bcc9a30fe84d6983369efc78c7619d1482340f

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
    
#    def get_positions_vector(self) -> None:
#        return self.get_positions()
<<<<<<< HEAD
    def get_Rotated(self, rotation_direction: RotationDirection):
        self.pos4.BODY[1].x

    def rotate_math(o_point: Point,rotation_direction: RotationDirection):


    # def rotate_block(self, rotation_direction: RotationDirection):
    #     print(tuple(map(lambda x: x.xy(),self.pos4.BODY)))
    #     orientation = 0
    #     if (rotation_direction==RotationDirection.CCW):
    #         self.rotation.go_ccw()
    #         orientation = self.rotation.get_ccw().rotation
        
    #     elif (rotation_direction==RotationDirection.CW):
    #         self.rotation.go_cw()
    #         orientation = self.rotation.get_cw().rotation
        
    #     print(RotationLookUpTable[self.type][orientation])
        
    #     return(RotationLookUpTable[self.type][orientation])
=======
    
    def rotate_block(self, rotation_direction: RotationDirection):
        # mutate here
        rotation = self.rotation
        if (rotation_direction==RotationDirection.CCW):
            #goleft
            pass
        elif (rotation_direction==RotationDirection.CW):
            #goright
            pass
        print(RotationLookUpTable[self.type][rotation_direction])
        return(RotationLookUpTable[self.type][rotation_direction])
>>>>>>> 85bcc9a30fe84d6983369efc78c7619d1482340f

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