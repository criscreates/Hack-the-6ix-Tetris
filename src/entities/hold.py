from ..utils import GameConfig
from ..utils import PieceType, DrawPlacement
from ..entities import Bag
import random

class Hold():
    def __init__(self, config: GameConfig) -> None:
        self.piece = None

    def hold_piece(self, current_piece):
        if self.piece != None:
            if self.piece.id > current_piece.id - 1:
                return current_piece
            else:
                temp_piece = self.piece
                self.piece = current_piece
                return temp_piece
        else:
            self.piece = current_piece
            return None

    def draw(self):
        if self.piece != None:
            return self.piece.draw(DrawPlacement.HOLD)
        else:
            return []



#held_piece = Hold()
# put current piece into hold box
# if the hold box is full you need to swap
# put a condition inside the swap function
# 
