class Tile:
    neighbors = []
    raw_x = 0
    raw_y = 0
    is_hovered = False #bool
    is_alive = False #bool

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
        self.is_alive = not self.is_alive

    def determine_status(self):
        alive_neighbors = self.count_alive_neighbors()

        if (self.is_alive and alive_neighbors < 2):
            return False
        
        if (self.is_alive and (alive_neighbors == 2 or alive_neighbors == 3)):
            return True
        
        if (self.is_alive and alive_neighbors > 3):
            return False
        
        if (not self.is_alive and alive_neighbors == 3):
            return True
        
        return False

        # if (alive_neighbors < 2 or alive_neighbors > 3):
        #     return False

        # elif alive_neighbors == 3:
        #     return True
        
        # return self.is_alive

    def count_alive_neighbors(self):
        alive_neighbors = 0

        for neighbor in self.neighbors:
            if neighbor.is_alive:
                alive_neighbors += 1
        
        return alive_neighbors