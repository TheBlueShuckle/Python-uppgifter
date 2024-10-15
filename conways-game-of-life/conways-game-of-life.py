import pygame
from tile import Tile
from grid import Grid

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

tiles = []

def parse_color(tile):
    if tile.hover:
        return 'gray'
    elif tile.alive:
        return 'white'
    else:
        return 'black'

def draw_grid(tiles):
    for row in grid.tiles:
        for tile in row:
            pygame.draw.rect(screen, parse_color(tile), (tile.x, tile.y, tile.size, tile.size))

def get_cursor_pos():
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    return (mouse_x, mouse_y)
            
def hover(mouse_x, mouse_y):
    tile = grid.tiles[min(round(mouse_y / 8), 99)][min(round(mouse_x / 8), 99)]
    hovered_tile = tile
    tile.hover = True
    return(hovered_tile)

def dehover(hovered_tile):
    hovered_tile.hover = False

# // PYGAME START //

pygame.init()

grid = Grid(100, 100, 8)

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
    draw_grid(grid.tiles)

    pygame.display.flip()
    dehover(hovered_tile)

    clock.tick(30)  # limits FPS to 30

pygame.quit()