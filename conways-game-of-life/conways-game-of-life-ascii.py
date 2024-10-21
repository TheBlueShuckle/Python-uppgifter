from tile import Tile
from grid import Grid

grid = Grid(10, 10, 0)

def input_alive_tiles():
    is_done = False
    
    while not is_done:
        display_grid(grid)
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

def simulation(focus_tiles):
    to_flip = []
    for tile in focus_tiles:
        if tile.is_alive != tile.determine_status:
            to_flip.append(tile)
    the_flippening(to_flip)

def the_flippening(to_flip):
    for tile in to_flip:
        tile.flip

def check_if_valid_coordinate(grid, coordinate):
    if (len(coordinate) == 2):
        if (coordinate[0] >= 0 and coordinate[0] <= grid.tiles_x and coordinate[1] >= 0 and coordinate[1] <= grid.tiles_y):
            return True
        
    return False

def raw_print(string):
    print(string, end='')

def display_grid(grid):
    print('  0 1 2 3 4 5 6 7 8 9')
    for row in grid.tiles:
        raw_print(grid.tiles.index(row))
        for cell in row:
            match cell.isAlive:
                case True:
                    raw_print(' #')
                case False:
                    raw_print('  ')
        raw_print('\n')

def start_sim(grid):
    print('Press ENTER to iterate')
    print('Type "q" to exit the program')

    while True:
        display_grid(grid)
        simulation()
        i = input('> ')
        if i == 'q':
            break

input_alive_tiles()
start_sim()