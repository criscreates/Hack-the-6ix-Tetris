from .piece import Piece
from ..utils import GameConfig
from ..utils.constants import *

class Board():
    def __init__(self, config: GameConfig, prefill: list[list[Cell]] = None) -> None:
        self.board = prefill or self.init_board()

    def init_board(self):
        return [[None for _ in range(10)] for _ in range(20)]


#    def place_piece(self, piece: Piece) -> bool:
#        piece_positions

