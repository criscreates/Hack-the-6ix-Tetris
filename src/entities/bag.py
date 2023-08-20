from ..utils import GameConfig
from ..utils import PieceType, DrawPlacement
from .piece import Piece
import random

class Bag():
    def __init__(self,config: GameConfig) -> None:
        self.config = config
        self.contents = []
        self.spot = 0

    def init_bag(self):
        return [
            PieceType.T,
            PieceType.I,
            PieceType.O,
            PieceType.S,
            PieceType.Z,
            PieceType.J,
            PieceType.L,
        ]


    def refill_bag(self):
        self.contents = self.init_bag()
        random.shuffle(self.contents)
    
    def refill_if_needed(self):
        if self.contents == []:
            self.refill_bag()
    
    def pull_piece(self):
        self.refill_if_needed()
        current = self.contents[0]
        del self.contents[0]
        self.spot += 1
        return Piece(self.config, current, self.spot)    

    def preview_piece(self):
        self.refill_if_needed()
        return Piece(self.config, self.contents[0], self.spot+1)

    def draw_preview(self):
        self.refill_if_needed()
        return self.preview_piece().draw(DrawPlacement.PREVIEW)
