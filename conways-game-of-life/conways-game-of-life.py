import pygame
from tile import Tile
from grid import Grid

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

tiles = []
alive_color = 'white'
dead_color  = 'black'
hover_color = 'gray'

def draw_grid(tiles):
    for tile in tiles:
        pygame.draw.rect(screen, tile.color, (tile.x, tile.y, tile.size, tile.size))

def get_cursor_pos():
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    return (mouse_x, mouse_y)

def hover(mouse_x, mouse_y):
    for tile in grid.tiles:
        if tile.x <= mouse_x and tile.x + tile.size >= mouse_x:
            if tile.y <= mouse_y and tile.y + tile.size >= mouse_y:
                prev_color = tile.color
                hovered_tile = tile
                tile.color = hover_color
                return(hovered_tile, prev_color)

def dehover(hovered_tile, prev_color):
    hovered_tile.color = prev_color

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
    hovered_tile, prev_color = hover(mouse_x, mouse_y)
    draw_grid(grid.tiles)

    pygame.display.flip()
    dehover(hovered_tile, prev_color)

    clock.tick(30)  # limits FPS to 30

pygame.quit()