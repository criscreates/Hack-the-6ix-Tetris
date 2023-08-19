from ..utils.game_config import GameConfig
from ..utils.constants import PieceType
from .piece import Piece
import random

class Bag():
    def __init__(self,config: GameConfig) -> None:
        self.config = config
        self.contents = []
        self.spot = 0

    def init_bag(self):
        return ['T', 'I', 'O', 'S', 'Z', 'J', 'L']


    def refill_bag(self):
        self.contents = self.init_bag()
        random.shuffle(self.contents)
    
    
    def pull_piece(self):
        if self.contents == []:
            self.refill_bag()
        current = self.contents[0]
        del self.contents[0]
        self.spot += 1
        return Piece(self.config, current, self.spot)    