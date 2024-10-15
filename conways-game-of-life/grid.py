from tile import Tile

class Grid:
    tiles = []  

    def __init__(self, tiles_x, tiles_y, pixel_size):
        self.pixels_x = tiles_x
        self.pixels_y = tiles_y
        self.tile_size = pixel_size   

        self.tiles = [[Tile(x, y, pixel_size, False, False) for x in range(tiles_x) for y in range(tiles_y)]]

    def set_neighbors(self, tile):
        for y in range(self.pixels_y):
            for x in range(self.pixels_x):
                neighbors = []
                