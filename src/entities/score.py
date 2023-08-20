from ..utils import GameConfig
from ..utils import ScoreAmount
import pygame

class Score():
    def __init__(self, config: GameConfig) -> None:
        self.score = 0
        self.previous_rect = None
        self.current_rect = None

    def addScore(self, clear_count: int):
        self.score += clear_count*100

    def getDispScore(self, x = 0 ,y = 0):
        font = pygame.font.SysFont("Arial",10)
        self.previous_rect = current_rect
        self.current_rect = font.render(self.score, True, (0,0,0))
        return [self.previous_rect, self.current_rect]


