import pygame
from pygame.locals import QUIT

from .entities import (
    Background,
    Bag,
    Board,
    Hold,
    Piece,
    Score,
)

from .utils import GameConfig, Images, Window
from .utils.constants import *

class Tetris():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        window = Window(288, 512)
        screen = pygame.display.set_mode((window.width, window.height))
        images = Images()

        self.config = GameConfig(
            screen = screen,
            clock = pygame.time.Clock(),
            fps = 60,
            window = window,
            images = images,
        )

    def test(self):
        self.background = Background(self.config)
        piece = Piece(self.config, PieceType.T, 0)
        bag = Bag(self.config)
        hold = Hold(self.config)
        self.board = Board(self.config, piece)
        self.score = Score(self.config)

        self.board.update()
        print('After Updates: ', self.board.piece.get_positions_vector())
        self.board.place_piece()
        self.test_print_board()
    
    def test_print_board(self) -> list[list[int]]:
        for row in reversed(self.board.board):
            print(row)
    
    def test_rotation(self):
        piece = Piece(self.config,PieceType.T, 0)
        piece.get_rotated(RotationDirection.CW)
        print(piece.get_body_as_tuples())
        piece.get_rotated(RotationDirection.CW)
        print(piece.get_body_as_tuples())
        

