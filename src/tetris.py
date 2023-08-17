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

class Tetris():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        window = Window(288, 512)
        screen = pygame.display.set_mode((window.width, window.height))

        self.config = GameConfig(
            screen = screen,
            clock = pygame.time.Clock(),
            fps = 60,
            window = window,
            images = Images(),
        )

    def test(self):
        self.background = Background(self.config)
        self.board = Board(self.config)
        self.score = Score(self.config)
        Bag(self.config)
        Hold(self.config)
        Piece(self.config)
