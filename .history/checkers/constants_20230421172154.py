import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = ("#ff0000")
WHITE = ("#964b00")
BLACK = ("#ffffff")
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (44, 25))         
# source for the image, if changed location will show up with error
