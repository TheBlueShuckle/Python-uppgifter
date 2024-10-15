from tile import Tile

class Grid:
    tiles = []

    def __init__(self, pixels_x, pixels_y, pixel_size):
        for y in range(pixels_x):
            for x in range(pixels_y):
                self.tiles.append(Tile(x, y, pixel_size, 'white'))