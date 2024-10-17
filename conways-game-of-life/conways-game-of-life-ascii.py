from tile import Tile
from grid import Grid

grid = Grid(10, 10, 0)

def input_alive_tiles():
    is_done = False
    
    while not is_done:
        coordinate = input('Input coordinates (eg. \'1 2\' for the positoin (1, 2)): ')

        if (coordinate != 'done'):
            parsed_coordinate = []

            for i in range(0, 2):
                parsed_coordinate.append(int(coordinate.split(' ')[i]))

            if check_if_valid_coordinate(grid, parsed_coordinate):
                tile = grid.tiles[parsed_coordinate[1]][parsed_coordinate[0]]
                tile.isAlive = not tile.isAlive # Toggles bool -V

            else:
                print('Incorrect input, retry.')

        else:
            is_done = True


def check_if_valid_coordinate(grid, coordinate):
    if (len(coordinate) == 2):
        if (coordinate[0] >= 0 and coordinate[0] <= grid.tiles_x and coordinate[1] >= 0 and coordinate[1] <= grid.tiles_y):
            return True
        
    return False