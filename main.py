import pygame
import random
import math

# lets create game 2048 using pygame
# Variables with CAPS LOCK are constants

pygame.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4

REACT_HEIGHT = HEIGHT // ROWS
REACT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVEL_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")