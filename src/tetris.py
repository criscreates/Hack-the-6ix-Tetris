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
        piece = Piece(self.config, PieceType['T'])

        #print(piece.get_positions())

    def testPiece(self):
        piece.rotate_block(RotationDirection.CCW)