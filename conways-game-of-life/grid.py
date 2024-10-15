from tile import Tile

class Grid:
    tiles = []  

    def __init__(self, tiles_x, tiles_y, tile_size):
        self.tiles_x = tiles_x
        self.tiles_y = tiles_y
        self.tile_size = tile_size   

        self.tiles = [[Tile(x, y, tile_size, False, False) for x in range(tiles_x) for y in range(tiles_y)]]

    def get_neighbors(self, tile):
        #              (-1,-1), (0,-1), (1,-1)
        #              (-1, 0), (0, 0), (1, 0)
        #              (-1, 1), (0, 1), (1, 1)
        x_offsets = { -1, 0, 1, 1, 1, 0, -1, -1 }
        y_offsets = { -1, -1, -1, 0, 1, 1, 1, 0 }
        max_x = self.tiles_x
        max_y = self.tiles_y
        neighbors = []

        for pos in range(8):
            if not (tile.raw_x + x_offsets[pos] < 0) or not (tile.raw_x + x_offsets[pos] > max_x) and not (tile.raw_y + y_offsets[pos] < 0) or not (tile.raw_y + y_offsets[pos] > max_y):
                neighbors.append(self.tiles[tile.raw_x + x_offsets[pos]][tile.raw_y + y_offsets[pos]])

        return [neighbors]

    def set_neighbors(self):
        for y in range(self.pixels_y):
            for x in range(self.pixels_x):
                self.tiles[x][y].neighbors = self.get_neighbors(self.tiles[x][y])
