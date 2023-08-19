from ..utils import GameConfig
from ..utils import RotationState
from ..utils import PieceType, Point, PIECE_STARTS, POS4

class Piece():
    def __init__(self, config: GameConfig, piece_type) -> None:
        self.type = piece_type
        self.pos4 = POS4(
            Point(5-1, 20-1),
            PIECE_STARTS[piece_type]
        )
        self.rotation = RotationState()

    def get_positions(self):
        origin = self.pos4.ORIGIN
        return (origin, *map(lambda v : v.add(origin), self.pos4.BODY))
    
    def get_positions_vector(self):
        return tuple(map(lambda x: x.xy(), self.get_positions()))

    def move(self, vector: Point):
        self.pos4 = POS4(self.pos4.ORIGIN.add(vector), self.pos4.BODY)
        return self
    
    def fall(self, speed: int = 1) -> None:
        return self.move(Point(0, -speed))