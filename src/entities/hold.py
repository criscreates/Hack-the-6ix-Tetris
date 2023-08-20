from ..utils import GameConfig
from ..utils.constants import PieceType
from ..entities.bag import Bag
import random

class Hold():
    def __init__(self, config: GameConfig) -> None:
        self.held_piece = None
        self.held_piece_spot = None
    def hold_piece(self, current_piece, current_piece_spot):
        if self.held_piece != None:
            if self.held_piece_spot > current_piece_spot:
                return current_piece, current_piece_spot
            else:
                temp_piece = self.held_piece
                temp_piece_spot = self.held_piece_spot
                self.held_piece = current_piece
                self.held_piece_spot = current_piece_spot
                current_piece = temp_piece
                current_piece_spot = temp_piece_spot
                return current_piece, current_piece_spot
        else:
            self.held_piece = current_piece
            self.held_piece_spot = current_piece_spot
            return None



#held_piece = Hold()
# put current piece into hold box
# if the hold box is full you need to swap
# put a condition inside the swap function
# 