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

        window = Window(1280, 720)

        screen = pygame.display.set_mode((window.width, window.height))
        images = Images()

        self.config = GameConfig(
            screen = screen,
            clock = pygame.time.Clock(),
            fps = 60,
            window = window,
            images = images,
            font_type = 'consolas',
            font_size = 45,
        )


    def play(self):
        bag = Bag(self.config)
        board = Board(self.config, bag.pull_piece(), bag)
        score = Score(self.config)
        
        self.config.screen.fill((255, 255, 255))
        

        while True:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            # Inputs
            keys = pygame.key.get_pressed()
            ticks = pygame.time.get_ticks()            

            # Input Handles
            if (keys[pygame.K_q]):
                exit()
            
            board_update_results = board.update(keys, ticks)

            if board_update_results == None:
                self.lose(score.score)
                break
            else:
                score.add(board_update_results)
        
            # Draws
            self.config.screen.fill((255, 255, 255))
            board_rects = board.draw()
            if board_rects == None:
                self.lose()
            score_rects = score.draw()
            caption_rects = self.draw_captions()

            # Displays
            pygame.display.update(score_rects + board_rects + caption_rects)
            self.config.tick()

    def draw_captions(self):
        block_size = self.config.images.piece_sides.x
        board_offset = Point((BOARD_WIDTH * block_size)//2, 0)
        board_top_right = Point(BOARD_WIDTH, BOARD_HEIGHT)
        board_top_left = Point(0, BOARD_HEIGHT)
        hold_top_left = board_top_left.add(Point(3, 0)).add(Point(-9, 2.5))
        preview_top_right = board_top_right.add(Point(3, 0)).add(Point(2, 2.5))

        p2r = lambda x: x.point_to_real(block_size, board_offset, self.config.window)

        font = pygame.font.SysFont(self.config.font_type, self.config.font_size)
        hold_rect = self.config.screen.blit(font.render('Hold', True, (0,0,0)), p2r(hold_top_left).xy)
        next_rect = self.config.screen.blit(font.render('Next', True, (0,0,0)), p2r(preview_top_right).xy)
        
        return [hold_rect, next_rect]


    def lose(self, score):
        print(f'Game Over: You got a score of : {score} points')

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
