from ..utils import RotationState
from ..utils import PieceType, Point, PIECE_STARTS, POS4, RotationLookUpTable, RotationDirection 
class Piece():
    def __init__(self, piece_type: PieceType, pos4: POS4 = None) -> None:
        self.type = piece_type
        self.pos4 = pos4 or self.init_pos4(self.type)
        self.rotation = RotationState()
    
    def init_pos4(self, piece_type: PieceType) -> POS4:
        return POS4(
            Point(5-1, 20-1),
            PIECE_STARTS[piece_type]
        )

    def get_positions(self):
        origin = self.pos4.ORIGIN
        return (origin, *map(lambda v : v.add(origin), self.pos4.BODY))
    
<<<<<<< HEAD
#    def get_positions_vector(self) -> None:
#        return self.get_positions()
    
    def rotate_block(self, rotation_direction: RotationDirection):
        # mutate here
        rotation = self.rotation
        if (rotation_direction==RotationDirection.CCW):
             #goleft
        elif (rotation_direction==RotationDirection.CW):
             #goright
        print(RotationLookUpTable[self.type][rotation_direction])
        return(RotationLookUpTable[self.type][rotation_direction])


=======
    def get_positions_vector(self) -> tuple[Point, Point, Point, Point]:
        return tuple(map(lambda x: x.xy(), self.get_positions()))
    
    def move_to(self, pos4: POS4):
        return Piece(self.type, pos4)

    def move(self, board, vector: Point) -> bool:
        tempPos = POS4(self.pos4.ORIGIN.add(vector), self.pos4.BODY)

        if board.valid_place(self.move_to(tempPos)):
            self.pos4 = tempPos
            return True
        else:
            return False
    
    def fall(self, board: list[list[int]], speed: int = 1) -> bool:
        return self.move(board, Point(0, -speed))
>>>>>>> 64bd3c5b1c7b1fcd3d1e218f0d862b2e6a011a3f
