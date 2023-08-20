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
        self.clear_count = 0
    
    def update(self):
        for _ in range(23):
            self.piece.fall(self)
        for _ in range(7):
            self.piece.strafe(self, 1)

    def init_board(self) -> list[list[Cell]]:
        self.clear_count = 0
        return [[None for _ in range(10)] for _ in range(20)]

    def clear_check(self, y):
        return not None in self.board[y]
    
    def clear_board(self):
        for y in self.board:
            if self.clear_check(y) == True:
                self.clear_count += 1
                # you could add to the score here! assuming we have time to implement that...
                self.board[y] = [None for _ in range(10)]
            
    def reset_board(self):
        self.clear_count = 0
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
                if self.board[v.y][v.x] != None:
                    return False
        except IndexError:
            return False

        return True


