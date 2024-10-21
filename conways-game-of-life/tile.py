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

    def flip(self):
        self.isAlive = not self.isAlive

    def determine_status(self):
        alive_neighbors = self.count_alive_neighbors(self.neighbors)

        if (alive_neighbors < 2 or alive_neighbors > 3):
            self.isAlive = False

        if (not self.isAlive and alive_neighbors == 3):
            self.isAlive = True

    def count_alive_neighbors(neighbors):
        alive_neighbors = 0

        for neighbor in neighbors:
            if neighbor.isAlive:
                alive_neighbors += 1
        
        return alive_neighbors