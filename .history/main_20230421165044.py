import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Checkers Game')


def get_row_col_from_mouse(pos):        # position determination
    x, y = pos
    row = y // SQUARE_SIZE              # row number
    col = x // SQUARE_SIZE              # col number
    return row, col


def main():                             # main function
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:          # AI's turn
            value, new_board = minimax(
                game.get_board(), 4, WHITE, game, float("-inf"), float("inf"))
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():  # quit the game
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:    # mouse click
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
