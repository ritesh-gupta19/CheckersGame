import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BROWN, HEADER_HEIGHT, TOTAL_HEIGHT
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, TOTAL_HEIGHT))
pygame.display.set_caption('The Checkers Game')

EASY = 2
MEDIUM = 4
HARD = 6

def get_row_col_from_mouse(pos, header_offset=HEADER_HEIGHT):
    x, y = pos
    y -= header_offset
    if y < 0:
        return -1, -1
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_difficulty_buttons(win):
    font = pygame.font.SysFont('comicsans', 27)
    easy_text = font.render('EASY', 1, (0, 0, 0))
    medium_text = font.render(' MEDIUM', 1, (0, 0, 0))
    hard_text = font.render('HARD', 1, (0, 0, 0))
    pygame.draw.rect(win, (200, 200, 200), (WIDTH//2 - 150, HEIGHT//2 - 50, 100, 50))
    pygame.draw.rect(win, (200, 200, 200), (WIDTH//2 - 50, HEIGHT//2 - 50, 100, 50))
    pygame.draw.rect(win, (200, 200, 200), (WIDTH//2 + 50, HEIGHT//2 - 50, 100, 50))
    win.blit(easy_text, (WIDTH//2 - 142, HEIGHT//2 - 45))
    win.blit(medium_text, (WIDTH//2 - 67, HEIGHT//2 - 45))
    win.blit(hard_text, (WIDTH//2 + 68, HEIGHT//2 - 45))
    pygame.display.update()

def draw_header(win, game, difficulty):
    pygame.draw.rect(win, (50, 50, 50), (0, 0, WIDTH, HEADER_HEIGHT))
    font = pygame.font.SysFont('comicsans', 30)
    title = font.render('CHECKERS GAME', 1, (0, 0, 255))
    win.blit(title, (WIDTH//2 - title.get_width()//2, 10))
    turn_text = font.render(f"TURN: {'RED' if game.turn == RED else 'BROWN'}", 1, (255, 255, 255))
    win.blit(turn_text, (WIDTH//2 - turn_text.get_width()//2, 45))
    diff_level = "EASY" if difficulty == EASY else ("MED" if difficulty == MEDIUM else "HARD")
    diff_text = font.render(f"DIFF: {diff_level}", 1, (255, 255, 255))
    win.blit(diff_text, (WIDTH - diff_text.get_width() - 20, 45))
    button_font = pygame.font.SysFont('comicsans', 24)
    pygame.draw.rect(win, (255, 255, 0), (0, 20, 120, 40))
    restart_text = button_font.render('RESTART', 1, (0, 0, 0))
    win.blit(restart_text, (10 + (100 - restart_text.get_width())//2, 20 + (40 - restart_text.get_height())//2))
    pygame.draw.rect(win, (200, 200, 200), (120, 20, 100, 40))
    menu_text = button_font.render('MENU', 1, (0, 0, 0))
    win.blit(menu_text, (120 + (100 - menu_text.get_width())//2, 20 + (40 - menu_text.get_height())//2))

def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    difficulty = MEDIUM
    game_started = False
    
    while run:
        clock.tick(FPS)
        
        if not game_started:
            WIN.fill((255, 255, 255))
            font = pygame.font.SysFont('comicsans', 50)
            title = font.render('Select Difficulty', 1, (0, 0, 0))
            WIN.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 150))
            draw_difficulty_buttons(WIN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    if WIDTH//2 - 150 <= x <= WIDTH//2 - 50 and HEIGHT//2 - 50 <= y <= HEIGHT//2:
                        difficulty = EASY
                        game_started = True
                    elif WIDTH//2 - 50 <= x <= WIDTH//2 + 50 and HEIGHT//2 - 50 <= y <= HEIGHT//2:
                        difficulty = MEDIUM
                        game_started = True
                    elif WIDTH//2 + 50 <= x <= WIDTH//2 + 150 and HEIGHT//2 - 50 <= y <= HEIGHT//2:
                        difficulty = HARD
                        game_started = True
        else:
            WIN.fill((0, 0, 0))  # Clear the screen
            draw_header(WIN, game, difficulty)  # Draw header
            if game.turn == BROWN:
                value, new_board = minimax(game.get_board(), difficulty, BROWN, game, float("-inf"), float("inf"))
                game.ai_move(new_board)
            if game.winner() != None:
                print(game.winner())
                font = pygame.font.SysFont('comicsans', 80)
                winner_text = font.render(f'{game.winner()} WINS!', 1, (255, 255, 255))
                WIN.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2, HEADER_HEIGHT + (HEIGHT//2 - winner_text.get_height()//2)))
                pygame.display.update()
                pygame.time.delay(3000)
                game = Game(WIN)
                game_started = False
                continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    if 10 <= x <= 110 and 20 <= y <= 60:
                        game = Game(WIN)
                    elif 120 <= x <= 220 and 20 <= y <= 60:
                        game = Game(WIN)
                        game_started = False
                    else:
                        row, col = get_row_col_from_mouse(pos)
                        if row >= 0 and col >= 0:
                            game.select(row, col)
            game.update(HEADER_HEIGHT)  # Update game with offset

    pygame.quit()

if __name__ == "__main__":
    main()