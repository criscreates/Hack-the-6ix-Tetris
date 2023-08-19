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
        self.board = Board(self.config)
        self.score = Score(self.config)
        bag = Bag(self.config)
        hold = Hold(self.config)
        piece = Piece(self.config, PieceType.T)

<<<<<<< HEAD
        #print(piece.get_positions())

    def testPiece(self):
        piece.rotate_block(RotationDirection.CCW)
=======
#        for i in range(10):
#            print(bag.pull_piece())

        piece.fall(self.board)
        piece.fall(self.board)
        print(piece.get_positions_vector())
        self.board.place_piece(piece)
        self.test_print_board()
    
    def test_print_board(self) -> list[list[int]]:
<<<<<<< HEAD
        for row in self.board.board:
            print(row)
>>>>>>> 64bd3c5b1c7b1fcd3d1e218f0d862b2e6a011a3f
=======
        for row in reversed(self.board.board):
            print(row)
>>>>>>> bc57f4eb948115c60bee6a1896993887489856a4
