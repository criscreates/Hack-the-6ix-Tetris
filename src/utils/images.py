import pygame
from .constants import Point

class Images:
    def __init__(self) -> None:
        self.piece_size = Point(20,20)
        self.piece_rect = pygame.Rect((0,0), self.piece_size.xy)
        self.piece_red = pygame.Surface(self.piece_size.xy)
        self.piece_red.fill((255,0,0))
