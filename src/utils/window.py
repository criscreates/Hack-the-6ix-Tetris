class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ratio = width / height
        self.viewport_width = width
        self.viewport_height = height * 0.79
        self.viewport_ratio = self.vw / self.vh