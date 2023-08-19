from ..utils import GameConfig
from ..utils.constants import PieceType
from ..entities.bag import Bag
import random

class Hold():
    def __init__(self, config: GameConfig) -> None:
        self.piece = None

    def hold_piece(self, current_piece):
        if self.piece:
            if self.piece.id > current_piece.id:
                return current_piece
            else:
                temp_piece = self.piece
                self.piece = current_piece
                current_piece = temp_piece
                return current_piece
        else:
            self.piece = current_piece
            return None



#held_piece = Hold()
# put current piece into hold box
# if the hold box is full you need to swap
# put a condition inside the swap function
# 