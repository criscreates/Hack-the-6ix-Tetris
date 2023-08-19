from ..utils import GameConfig
from ..utils.constants import *

class Piece():
    def __init__(self, config: GameConfig, piece_type) -> None:
        self.type = piece_type
        self.pos4 = POS4(
            (5,20),
            PIECE_STARTS[piece_type]
        )

    def get_positions(self) -> None:
        origin = self.pos4.ORIGIN
        return (origin, *map(lambda x : self.pairwise_add(x, origin), self.pos4.BODY))
    
    def pairwise_add(self, v1: tuple[int,int], v2: tuple[int,int]) -> tuple[int,int]:
        return tuple(x + y for x,y in zip(v1, v2)) 