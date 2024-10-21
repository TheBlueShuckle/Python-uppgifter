import pygame
from tile import Tile
from grid import Grid

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

tiles = []

def find_focus_tiles(grid):
    focus_tiles = []

    for y in range(grid.tiles_y):
        for x in range(grid.tiles_x):
            tile = grid.tiles[x][y]
            
            if (tile.is_alive):
                focus_tiles.append(tile)
                for neighbor in tile.neighbors:
                    if neighbor not in focus_tiles and not neighbor.is_alive:
                        focus_tiles.append(neighbor)

    return focus_tiles

def simulation(grid):
    focus_tiles = find_focus_tiles(grid)

    to_flip = []
    for tile in focus_tiles:
        # print(str(tile.x) + ', ' + str(tile.y))

        # for neighbor in tile.neighbors:
        #     print(str(neighbor.x) + ', ' + str(neighbor.y))

        # print(tile.is_alive)
        # print(tile.determine_status())
        # print('----')
        if tile.is_alive != tile.determine_status():
            to_flip.append(tile)
                
    the_flippening(to_flip)

def the_flippening(to_flip):
    for tile in to_flip:
        tile.flip()

def parse_color(tile):
    if tile.is_hovered:
        return 'gray'
    elif tile.is_alive:
        return 'white'
    else:
        return 'black'

def draw_grid(tiles):
    for row in tiles:
        for tile in row:
            pygame.draw.rect(screen, parse_color(tile), (tile.x, tile.y, tile.size, tile.size))

def get_cursor_pos():
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    return (mouse_x, mouse_y)
            
def hover(mouse_x, mouse_y):
    tile = grid.tiles[min(round(mouse_y / 8), 99)][min(round(mouse_x / 8), 99)]
    hovered_tile = tile
    tile.is_hovered = True
    return(hovered_tile)

def dehover(hovered_tile):
    hovered_tile.is_hovered = False

# // PYGAME START //

pygame.init()

grid = Grid(100, 100, 8)
pygame.mouse.set_visible(False) # No more mouse-centering problems if you can't see the mouse -C

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('black')
    
    mouse_x, mouse_y = get_cursor_pos()
    hovered_tile = hover(mouse_x, mouse_y)
    draw_grid(grid.tiles) # Passing in grid.tiles because its more efficient (dont cite me) -V

    pygame.display.flip()
    dehover(hovered_tile)

    clock.tick(60)  # limits FPS to 60

pygame.quit()