import pygame
from .constants import Point

class Images:
    def __init__(self) -> None:
        self.piece_sides = Point(30,30)
        self.piece_rect = pygame.Rect((0,0), self.piece_sides.xy)

        self.piece_red = pygame.Surface(self.piece_sides.xy)
        self.piece_red.fill((255,0,0))

        self.piece_grey = pygame.Surface(self.piece_sides.xy)
        self.piece_grey.fill((50,50,50, 50))

        self.piece_green = pygame.Surface(self.piece_sides.xy)
        self.piece_green.fill((0,255,0, 50))

        self.piece_blue = pygame.Surface(self.piece_sides.xy)
        self.piece_blue.fill((0,0,255, 50))
