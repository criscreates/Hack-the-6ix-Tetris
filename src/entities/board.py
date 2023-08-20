import pygame
from .bag import Bag
from .piece import Piece
from ..utils import GameConfig
from ..utils import Cell
from ..utils.constants import *

class Board():
    def __init__(self, 
                 config: GameConfig, 
                 piece,
                 bag = None,
                 prefill: list[list[Cell]] = None,
                 ) -> None:
        self.config = config
        self.board = prefill or self.init_board()
        self.set_piece(piece)
        self.bag = bag or Bag(config)

    def set_piece(self, piece):
        self.piece = piece
        piece.fall_until_valid(self)
    
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
        #if keys[pygame.K_DOWN]:
        #    self.piece.quick_drop(self)
        #else:
        #    self.piece.fall(self)
        if keys[pygame.K_DOWN]:
            if not self.piece.fall(self):
                self.place_piece()

        return self.clear_board()

        

    
    def draw(self):
        block_size = self.config.images.piece_sides.x
        board_offset = Point((BOARD_WIDTH * block_size)//2, 0)

        draw_rects = []

        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                draw_rects.append(self.config.screen.blit(
                    self.config.images.piece_blue if self.board[y][x] else self.config.images.piece_grey, 
                    Point(x,y).point_to_real(block_size, board_offset, self.config.window).xy))

        return [*self.piece.draw(), *draw_rects]


    def init_board(self) -> list[list[Cell]]:
        return [self.init_row() for _ in range(20)]
    
    def init_row(self) -> list[Cell]:
        return [None for _ in range(10)]

    def clear_check(self, y: int) -> bool:
        return not None in self.board[y]
    
    def clear_board(self) -> int:
        clear_count = 0
        for y in range(BOARD_HEIGHT):
            if self.clear_check(y) == True:
                clear_count += 1
                # you could add to the score here! assuming we have time to implement that...
                del self.board[y]
                self.board.append(self.init_row())
        return clear_count
            
    def reset_board(self):
        self.board = self.init_board()
        return self

    def place_piece(self) -> bool:
        if not self.valid_place(self.piece):
            return False

        for v in self.piece.get_positions_as_tuples():
            self.board[v.y][v.x] = Cell.Placed

        # made for multi boards simultaneously
        if self.piece.id == self.bag.spot:
            self.set_piece(self.bag.pull_piece())

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


