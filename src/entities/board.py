import pygame
from .piece import Piece
from ..utils import GameConfig
from ..utils import Cell
from ..utils.constants import *

class Board():
    def __init__(self, 
                 config: GameConfig, 
                 piece,
                 prefill: list[list[Cell]] = None,
                 ) -> None:
        self.board = prefill or self.init_board()
        self.piece = piece
    
    def update(self, keys):
        # Strafes
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.piece.strafe(self, 0)
        elif keys[pygame.K_LEFT]:
            self.piece.strafe(self, -1)
        elif keys[pygame.K_RIGHT]:
            self.piece.strafe(self, 1)
        
        # Rotation
        if keys[pygame.K_x]:
            self.piece.rotate(self, RotationDirection.CW)
        elif keys[pygame.K_z]:
            self.piece.rotate(self, RotationDirection.CCW)
        
        # Falls
        if keys[pygame.K_DOWN]:
            self.piece.quick_drop(self)
        else:
            self.piece.fall(self)

    def init_board(self) -> list[list[Cell]]:
        return [[None for _ in range(10)] for _ in range(20)]

    def clear_check(self, y: int) -> bool:
        return not None in self.board[y]
    
    def clear_board(self) -> int:
        clear_count = 0
        for y in self.board:
            if self.clear_check(y) == True:
                clear_count += 1
                # you could add to the score here! assuming we have time to implement that...
                self.board[y] = [None for _ in range(10)]
        return clear_count
            
    def reset_board(self):
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


