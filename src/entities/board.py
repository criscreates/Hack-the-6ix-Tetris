from .piece import Piece
from ..utils import GameConfig
from ..utils import Cell

class Board():
    def __init__(self, 
                 config: GameConfig, 
                 piece,
                 prefill: list[list[Cell]] = None,
                 ) -> None:
        self.board = prefill or self.init_board()
        self.piece = piece
    
    def update(self):
        for _ in range(23):
            self.piece.fall(self)
        for _ in range(7):
            self.piece.strafe(self, 1)

    def init_board(self) -> list[list[Cell]]:
        return [[None for _ in range(10)] for _ in range(20)]

    def clear_board(self):
        self.board = self.init_board()
        return self

    def place_piece(self) -> bool:
        if not self.valid_place(self.piece):
            return False

        for v in self.piece.get_positions_as_tuples():
            self.board[v.y][v.x] = Cell.Placed

        return True

    def valid_place(self, piece: Piece) -> bool:
        try:        
            for v in piece.get_positions_as_tuples():
                if v.x < 0 or v.y < 0:
                    return False
                if not self.board[v.y][v.x] == None:
                    return False
        except IndexError:
            return False

        return True


