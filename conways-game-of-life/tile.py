class Tile:
    def __init__(self, x, y, size, color):
        self.x = x * size #int
        self.y = y * size #int
        self.size = size #int
        self.color = color #str