import pygame
from tile import Tile
from grid import Grid

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

tiles = []

def parse_color(tile):
    if tile.isHovered:
        return 'gray'
    elif tile.isAlive:
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
    tile.isHovered = True
    return(hovered_tile)

def dehover(hovered_tile):
    hovered_tile.isHovered = False

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