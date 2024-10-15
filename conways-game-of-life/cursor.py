import pygame
from grid import *
from tile import *

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