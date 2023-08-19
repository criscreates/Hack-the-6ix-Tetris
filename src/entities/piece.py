from ..utils import GameConfig
from ..utils import RotationState
from ..utils import PieceType, Point, PIECE_STARTS, POS4

class Piece():
    def __init__(self, config: GameConfig, piece_type) -> None:
        self.type = piece_type
        self.pos4 = POS4(
            Point(5,20),
            PIECE_STARTS[piece_type]
        )
        self.rotation = RotationState

    def get_positions(self) -> None:
        origin = self.pos4.ORIGIN
        return (origin, *map(lambda v : v.add(origin), self.pos4.BODY))
    
#    def get_positions_vector(self) -> None:
#        return self.get_positions()
    