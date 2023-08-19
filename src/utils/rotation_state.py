class RotationState():
    def __init__(self, rotation: int = 0) -> None:
        self.rotation = rotation
    
    def get_right(self):
        return RotationState((self.rotation + 1) % 4)

    def get_left(self):
        return RotationState((self.rotation - 1) % 4)