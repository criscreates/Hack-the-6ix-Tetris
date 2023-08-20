from ..utils import GameConfig
import pygame

class Score():
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.score = 0
        self.previous_rect = None
        self.current_rect = None

    def add(self, clear_count: int):
        self.score += clear_count*100

    def draw(self, x = 0, y = 0):

        font = pygame.font.SysFont("Arial",50)
        self.previous_rect = self.current_rect
        current_surface = font.render('Score: ' + str(self.score), True, (0,0,0))
        self.current_rect = self.config.screen.blit(current_surface,(x,y))
        return [self.previous_rect, self.current_rect]
