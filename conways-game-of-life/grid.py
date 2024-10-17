from tile import Tile

class Grid:
    def __init__(self, tiles_x, tiles_y, tile_size):
        self.tiles_x = tiles_x
        self.tiles_y = tiles_y
        self.tile_size = tile_size   

        self.tiles = [[Tile(x, y, tile_size) for x in range(tiles_x)] for y in range(tiles_y)]
        self.set_neighbors()

    def get_neighbors(self, tile):
        #              (-1,-1), (0,-1), (1,-1)
        #              (-1, 0), (0, 0), (1, 0)
        #              (-1, 1), (0, 1), (1, 1)
        x_offsets = [ -1, 0, 1, 1, 1, 0, -1, -1 ]
        y_offsets = [ -1, -1, -1, 0, 1, 1, 1, 0 ]
        neighbors = []

        for pos in range(8):
            hasValidNeighbor = (not (tile.raw_x + x_offsets[pos] < 0) and not (tile.raw_x + x_offsets[pos] > self.tiles_x - 1)) and (not (tile.raw_y + y_offsets[pos] < 0) and not (tile.raw_y + y_offsets[pos] > self.tiles_y - 1))

            if hasValidNeighbor:
                neighbors.append(self.tiles[tile.raw_x + x_offsets[pos]][tile.raw_y + y_offsets[pos]])

        return neighbors

    def set_neighbors(self):
        for y in range(self.tiles_x):
            for x in range(self.tiles_y):
                self.tiles[x][y].neighbors = self.get_neighbors(self.tiles[x][y])

grid = Grid(100, 100, 8)

# # Test default
# for neighbor in grid.get_neighbors(grid.tiles[10][10]):
#     print(str(neighbor.x) + " " + str(neighbor.y))

# print("---")
# # Test corner
# for neighbor in grid.get_neighbors(grid.tiles[0][0]):
#     print(str(neighbor.x) + " " + str(neighbor.y))

# print("---")
# # Test edge
# for neighbor in grid.get_neighbors(grid.tiles[1][0]):
#     print(str(neighbor.x) + " " + str(neighbor.y))
    
# print("---")

# Test Thingy
# for neighbor in grid.get_neighbors(grid.tiles[99][99]):
#     print(str(neighbor.x) + " " + str(neighbor.y))
    
# print("---")