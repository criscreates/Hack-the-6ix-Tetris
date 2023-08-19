from ..utils import GameConfig
from ..utils.constants import *

class Piece():
    def __init__(self, config: GameConfig, piece_type: PieceType) -> None:
        self.type = piece_type
        self.pos4 = POS4(
            (5,20),
            PIECE_STARTS[piece_type]
        )
