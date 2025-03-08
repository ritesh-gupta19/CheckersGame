import pygame

# Window dimensions
WIDTH, HEIGHT = 720, 720
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Define header height
HEADER_HEIGHT = 80
TOTAL_HEIGHT = HEIGHT + HEADER_HEIGHT

# Colors (RGB or hex)
RED = ("#ff0000")
BROWN = ("#964b00")  
BLACK = ("#000000")
GREEN = ("#3f9719")
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Crown image for kings
CROWN = pygame.transform.scale(pygame.image.load('checkers/crown.png'), (44, 25))