from .constants import RED, BROWN, SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win, y_offset=0):
        radius = SQUARE_SIZE // 2 - self.PADDING
        adjusted_y = self.y + y_offset
        pygame.draw.circle(win, GREY, (self.x, adjusted_y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, adjusted_y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, adjusted_y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)