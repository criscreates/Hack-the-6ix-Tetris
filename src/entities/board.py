from .piece import Piece
from ..utils import GameConfig
from ..utils import Cell

class Board():
    def __init__(self, config: GameConfig, prefill: list[list[Cell]] = None) -> None:
        self.board = prefill or self.init_board()

    def init_board(self):
        return [[None for _ in range(10)] for _ in range(20)]


    def place_piece(self, piece: Piece) -> bool:
        for v in piece.get_positions():
            if self.board[v.y][v.x]:
                return False
        
        for v in piece.get_positions():
            self.board[v.y][v.x] = Cell.Placed

        return True

