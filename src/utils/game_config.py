import os

import pygame

from .images import Images
from .window import Window


class GameConfig:
    def __init__(
        self,
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        fps: int,
        window: Window,
        images: Images,
        font_type: str,
        font_size: int,
    ) -> None:
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.window = window
        self.images = images
        self.font_type = font_type
        self.font_size = font_size


    def tick(self) -> None:
        self.clock.tick(self.fps)