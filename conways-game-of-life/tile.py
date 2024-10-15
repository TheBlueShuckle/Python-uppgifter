class Tile:
    neighbors = []
    raw_x = 0
    raw_y = 0

    def __init__(self, x, y, size, alive, hover):
        self.raw_x = x
        self.raw_y = y
        self.x = x * size #int
        self.y = y * size #int
        self.size = size #int
        self.alive = alive #bool
        self.hover = hover #bool

    def find_neighbors(self, neighbors):
        self.neighbors = neighbors