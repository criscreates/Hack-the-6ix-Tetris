from ..entities.piece import Piece
from .constants import *

class RotationType():
    def __init__(self, rotation: int = 0) -> None:
        self.rotation = rotation
    
    def get_right(self):
        return RotationType((self.rotation + 1) % 4)

    def get_left(self):
        return RotationType((self.rotation - 1) % 4)