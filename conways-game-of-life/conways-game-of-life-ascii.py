from tile import Tile
from grid import Grid

grid = Grid(10, 10, 0)

def raw_print(string):
    print(string, end='')

def display_grid(grid):
    print('  0 1 2 3 4 5 6 7 8 9')
    for row in grid.tiles:
        raw_print(grid.tiles.index(row))
        for cell in row:
            match cell.isAlive:
                case True:
                    raw_print('# ')
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

display_grid(grid)