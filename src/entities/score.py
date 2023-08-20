from ..utils import GameConfig

class Score():
    def __init__(self, config: GameConfig) -> None:
        self.score = 0

    def addScore(self, clear_count: int):
        self.score += clear_count*100
