from ..utils.game_config import GameConfig
from ..utils.constants import PieceType
import random

class Bag():
    contents = PieceType
    def __init__(self, config: GameConfig) -> None:
        self.b = []
    def refill_bag():
        contents = random.shuffle(['T', 'I', 'O', 'S', 'Z', 'J', 'L'])
        return contents
    def pull_piece(bag_contents):
        pulled_piece = bag_contents[0]
        del bag_contents[0]
        return pulled_piece, bag_contents
        

# b = Bag()
# b.refill_bag()