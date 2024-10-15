import pygame
from tile import Tile
from grid import Grid

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

tiles = []
alive_color = 'White'
bg_color = 'Black'
hover_color = 'Grey'

def draw_grid(tiles):
    for tile in tiles:
        if (tile.alive):
            pygame.draw.rect(screen, alive_color, (tile.x, tile.y, tile.size, tile.size))
        if (tile.hover):
            pygame.draw.rect(screen, hover_color, (tile.x, tile.y, tile.size, tile.size))

pygame.init()

grid = Grid(100, 100, 8)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(bg_color)

    mousex, mousey = pygame.mouse.get_pos()
    for n in tiles:
        if tiles[n].x == mousex:
            if tiles[n].y == mousey:
                tiles[n].hover = True
                break
            break
    # RENDER YOUR GAME HERE
    draw_grid(grid.tiles)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()