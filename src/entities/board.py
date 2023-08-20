import pygame
from .bag import Bag
from .piece import Piece
from .hold import Hold
from ..utils import GameConfig
from ..utils import Cell
from ..utils.constants import *

class Board():
    def __init__(self, 
                 config: GameConfig, 
                 piece = None,
                 bag = None,
                 hold = None,
                 prefill: list[list[Cell]] = None,
                 ) -> None:
        self.config = config
        self.board = prefill or self.init_board()
        self.bag = bag or Bag(config)
        self.hold = hold or Hold(config)
        self.set_piece(piece or bag.pull_piece())
        self.lose = False

        self.fall_s_time = 0
        self.rotate_s_time = 0
        self.strafe_s_time = 0

    def set_piece(self, piece) -> bool:
        self.piece = piece
        return piece.fall_until_valid(self)
    
    def update(self, keys, ticks):
        # Lose
        if self.lose:
            return None

        # Holds
        if keys[pygame.K_c]:
            temp_piece = self.hold.hold_piece(self.piece)
            if temp_piece == None:
                self.set_piece(self.bag.pull_piece())
            elif temp_piece.id != self.piece.id:
                self.set_piece(Piece(self.config, temp_piece.type, temp_piece.id))

        # Strafes
        if ticks - self.strafe_s_time > 100:
            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                self.piece.strafe(self, 0)
                self.strafe_s_time = ticks
            elif keys[pygame.K_LEFT]:
                self.piece.strafe(self, -1)
                self.strafe_s_time = ticks
            elif keys[pygame.K_RIGHT]:
                self.piece.strafe(self, 1)
                self.strafe_s_time = ticks
        
        # Rotation
        if ticks - self.rotate_s_time > 100:
            if keys[pygame.K_x]:
                self.piece.rotate(self, RotationDirection.CW)
                self.rotate_s_time = ticks
            elif keys[pygame.K_z]:
                self.piece.rotate(self, RotationDirection.CCW)
                self.rotate_s_time = ticks
        
        # Falls
        if keys[pygame.K_DOWN] and ticks - self.fall_s_time > 200:
            self.piece.quick_drop(self)
            if not self.piece.fall(self):
                self.place_piece()
            self.fall_s_time = ticks
        elif ticks - self.fall_s_time > 300:
            self.piece.fall(self)
            if not self.piece.fall(self):
                self.place_piece()
            self.fall_s_time = ticks

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

        # Bag
        bag_rect = self.bag.draw_preview()

        # Hold
        hold_rect = self.hold.draw()

        return [*self.piece.draw(), *draw_rects, *hold_rect, *bag_rect]



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

        if not self.set_piece(self.bag.pull_piece()):
            self.lose = True


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


