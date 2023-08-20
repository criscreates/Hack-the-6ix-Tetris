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

        self.bag = Bag(self.config)

    def play(self):
        board = Board(self.config, self.bag.pull_piece())

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            #board.update(pygame.key.get_pressed())
        
            self.config.screen.fill((255, 255, 255))

            board.piece.draw()

            pygame.display.flip()
        

    def test(self):
        self.background = Background(self.config)
        piece = Piece(self.config, PieceType.T, 0)
        bag = Bag(self.config)
        hold = Hold(self.config)
        self.board = Board(self.config, piece)
        self.score = Score(self.config)

        self.board.piece.fall(self.board)
        print('After Updates: ', self.board.piece.get_positions_vector())
        self.board.place_piece()
        self.test_print_board()
    
    def test_print_board(self) -> list[list[int]]:
        for row in reversed(self.board.board):
            print(row)
    
    def test_rotation(self):
        piece = Piece(self.config,PieceType.T, 0)
        board = Board(self.config, piece)

        piece.fall(board)
        piece.fall(board)
        piece.rotate(board, RotationDirection.CW)
        print(piece.get_body_as_tuples())

        piece.rotate(board, RotationDirection.CCW)
        print(piece.get_body_as_tuples())
        
    def test_hold(self):
        h = Hold(self.config)

        h.hold_piece(Piece(self.config, PieceType.I, 0))
        print('Piece: ', h.piece.type)
        print('Id: ', h.piece.id)

        h.hold_piece(Piece(self.config, PieceType.S, 1))
        print('Piece: ', h.piece.type)
        print('Id: ', h.piece.id)

        h.hold_piece(Piece(self.config, PieceType.T, 1))
        print('Piece: ', h.piece.type)
        print('Id: ', h.piece.id)
