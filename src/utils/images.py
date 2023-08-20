import pygame
from .constants import Point

class Images:
    def __init__(self) -> None:
        self.piece_sides = Point(30,30)
        self.piece_rect = pygame.Rect((0,0), self.piece_sides.xy)
        self.piece_red = pygame.Surface(self.piece_sides.xy)
        self.piece_red.fill((255,0,0))
