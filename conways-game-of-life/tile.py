class Tile:
    neighbors = []
    raw_x = 0
    raw_y = 0
    isHovered = False #bool
    isAlive = False #bool

    def __init__(self, x, y, size):
        # Dont like these vars :/ -V
        self.raw_x = x
        self.raw_y = y

        # These are good -V
        self.x = x * size #int
        self.y = y * size #int
        self.size = size #int

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors