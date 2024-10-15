class Tile:
    def __init__(self, x, y, size, alive, hover):
        self.x = x * size #int
        self.y = y * size #int
        self.size = size #int
        self.alive = alive #bool
        self.hover = hover #bool