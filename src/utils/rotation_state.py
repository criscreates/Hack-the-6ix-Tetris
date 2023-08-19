class RotationState():
    def __init__(self, rotation: int = 0) -> None:
        self.rotation = rotation
    
    def circle(self, dir: int) -> int:
        new_rot = (self.rotation + dir) % 4
        return new_rot if new_rot != -1 else 3
    
    def get_cw(self):
        return RotationState(self.circle(1))

    def get_ccw(self):
        return RotationState(self.circle(-1))
    
    def go_cw(self):
        self.rotation = self.circle(1)

    def go_ccw(self):
        self.rotation = self.circle(-1)