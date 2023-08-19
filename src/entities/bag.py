from ..utils.game_config import GameConfig
from ..utils.constants import PieceType
import random

class Bag():
    def __init__(self, config: GameConfig) -> None:
        self.contents = []
        self.spot = 0
    def refill_bag(self):
        self.contents = random.shuffle(['T', 'I', 'O', 'S', 'Z', 'J', 'L'])
    def pull_piece(self):
        if self.contents == []:
            self.contents = self.refill_bag(self)
        current = self.contents[0]
        del self.contents[0]
        self.spot += 1
        return current      