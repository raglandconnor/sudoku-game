import pygame
import sys

from board import Board
from constants import *
from sudoku_generator import *


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 80)
    game_mode_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font("button_font.ttf", 20)

    # Color background
    screen.fill((255, 255, 255))
    image = pygame.image.load('sudoku_background.jpg')
    img_resize = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(img_resize, (0, 0))

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", True, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw game mode message
    game_mode_surface = game_mode_font.render("Select Game Mode", True, (0, 0, 0))
    game_mode_rectangle = game_mode_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 25))
    screen.blit(game_mode_surface, game_mode_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("EASY", True, (255, 255, 255))
    medium_text = button_font.render("MEDIUM", True, (255, 255, 255))
    hard_text = button_font.render("HARD", True, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((medium_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (27, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((medium_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (27, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 4, HEIGHT // 2 + 120))
    medium_rectangle = medium_surface.get_rect(
        center=(2 * (WIDTH // 4), HEIGHT // 2 + 120))
    hard_rectangle = hard_surface.get_rect(
        center=(3 * (WIDTH // 4), HEIGHT // 2 + 120))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # get user's desired difficulty choice which is returned
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                elif medium_rectangle.collidepoint(event.pos):
                    return "medium"
                elif hard_rectangle.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()


def draw_game_win(screen):
    # initialize fonts
    win_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font("button_font.ttf", 20)

    # put image of sudoku in background
    screen.fill((255, 255, 255))
    image = pygame.image.load('sudoku_background.jpg')
    img_resize = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(img_resize, (0, 0))

    # display game won
    win_surface = win_font.render("Game Won!", True, (0, 0, 0))
    win_rectangle = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(win_surface, win_rectangle)

    # make and display button
    # Initialize text first
    win_text = button_font.render("EXIT", True, (255, 255, 255))

    # Initialize button background color and text
    win_surface = pygame.Surface((win_text.get_size()[0] + 20, win_text.get_size()[1] + 20))
    win_surface.fill(LINE_COLOR)
    win_surface.blit(win_text, (10, 10))

    # Initialize button rectangle
    win_rectangle = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 120))

    # Draw buttons
    screen.blit(win_surface, win_rectangle)

    # get user input to exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if win_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def draw_game_lose(screen):
    # initialize fonts
    lose_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font("button_font.ttf", 20)

    # put image of sudoku in background
    screen.fill((255, 255, 255))
    image = pygame.image.load('sudoku_background.jpg')
    img_resize = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(img_resize, (0, 0))

    # display game won
    lose_surface = lose_font.render("Game Over :(", True, (0, 0, 0))
    lose_rectangle = lose_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(lose_surface, lose_rectangle)

    # make and display button

    # Initialize text first
    lose_text = button_font.render("RESTART", True, (255, 255, 255))

    # Initialize button background color and text
    lose_surface = pygame.Surface((lose_text.get_size()[0] + 20, lose_text.get_size()[1] + 20))
    lose_surface.fill(LINE_COLOR)
    lose_surface.blit(lose_text, (10, 10))

    # Initialize button rectangle
    lose_rectangle = lose_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 120))

    # Draw buttons
    screen.blit(lose_surface, lose_rectangle)

    # get user input to restart game which then calls main()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lose_rectangle.collidepoint(event.pos):
                    main()
        pygame.display.update()


# Prints board for testing purposes
def test_board(correct_board):
    print("Correct board: ")
    for idx in range(9):
        for col in correct_board:
            print(col[idx], end=" ")
        print()


def main():
    pygame.init()
    button_font = pygame.font.Font("button_font.ttf", 20)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")  # says Sudoku in top of project window
    difficulty = draw_game_start(screen)
    # now switches to game screen
    screen.fill(BG_GAME_COLOR)
    # now lines will be drawn
    removed = 0
    if difficulty == "easy":
        removed = 30
    elif difficulty == "medium":
        removed = 40
    elif difficulty == "hard":
        removed = 50
    sudoku = SudokuGenerator(9, removed)
    sudoku.fill_values()
    board_complete = sudoku.get_board() # what user's board is eventually compared to
    sudoku.remove_cells()
    board_blank = sudoku.get_board()
    display_board = Board(630, 630, screen, removed)

    # Used to test end functionality in video (COMMENT OUT WHEN NOT TESTING)
    # test_board(board_complete)

    # give cells values from generated sudoku board
    for i in range(9):
        for j in range(9):
            display_board.cells[i][j].value = board_blank[i][j]
            if display_board.cells[i][j].value != 0:
                display_board.cells[i][j].editable = False

    # displays board on the screen
    display_board.draw()

    # Initialize buttons
    # Initialize text first
    reset_text = button_font.render("RESET", True, (255, 255, 255))
    restart_text = button_font.render("RESTART", True, (255, 255, 255))
    exit_text = button_font.render("EXIT", True, (255, 255, 255))

    # Initialize button background color and text
    reset_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (27, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (27, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 4, HEIGHT // 2 + 316))
    restart_rectangle = restart_surface.get_rect(
        center=(2 * (WIDTH // 4), HEIGHT // 2 + 316))
    exit_rectangle = exit_surface.get_rect(
        center=(3 * (WIDTH // 4), HEIGHT // 2 + 316))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)
    clicked_row = 0
    clicked_col = 0
    while True:
        # Checks if board is full. If it is full then see if it is correct
        if display_board.is_full():
            print("board full")

            if display_board.check_board(board_complete):
                draw_game_win(screen)
                # You win screen
            else:
                draw_game_lose(screen)
                # You lose screen

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] <= 630:  # If  user clicks inside board
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    clicked_row, clicked_col = display_board.click(event.pos[1], event.pos[0])
                    # Gets row and col where user clicks on screen if inside game board

                    # Highlight place where user clicks by calling select in Board which calls draw in Cell
                    display_board.select(clicked_row, clicked_col)
                # If user clicks reset then the background color fills the screen and reset_to_original() is called
                elif reset_rectangle.collidepoint(event.pos):
                    screen.fill(BG_GAME_COLOR)
                    display_board.reset_to_original()
                # If user clicks restart then main() is called
                elif restart_rectangle.collidepoint(event.pos):
                    main()
                # If user clicks exit then sys.exit()
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
            # Keyboard input
            if event.type == pygame.KEYDOWN:
                input_val = None
                if event.key == pygame.K_RETURN:  # enter key
                    input_val = 0
                elif event.key == pygame.K_1:  # "1"
                    input_val = 1
                elif event.key == pygame.K_2:  # "2"
                    input_val = 2
                elif event.key == pygame.K_3:  # "3"
                    input_val = 3
                elif event.key == pygame.K_4:  # "4"
                    input_val = 4
                elif event.key == pygame.K_5:  # "5"
                    input_val = 5
                elif event.key == pygame.K_6:  # "6"
                    input_val = 6
                elif event.key == pygame.K_7:  # "7"
                    input_val = 7
                elif event.key == pygame.K_8:  # "8"
                    input_val = 8
                elif event.key == pygame.K_9:  # "9"
                    input_val = 9
                # Move selected red square with arrow keys
                elif event.key == pygame.K_UP:  # Up arrow
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_val = 11
                    if clicked_col - 1 >= 0:
                        clicked_col -= 1
                        display_board.select(clicked_row, clicked_col)
                elif event.key == pygame.K_DOWN:  # Down arrow
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_val = 11
                    if clicked_col + 1 <= 8:
                        clicked_col += 1
                        display_board.select(clicked_row, clicked_col)
                elif event.key == pygame.K_LEFT:  # Left arrow
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_val = 11
                    if clicked_row - 1 >= 0:
                        clicked_row -= 1
                        display_board.select(clicked_row, clicked_col)
                elif event.key == pygame.K_RIGHT:  # Right arrow
                    screen.fill(BG_GAME_COLOR)
                    display_board.draw()
                    input_val = 11
                    if clicked_row + 1 <= 8:
                        clicked_row += 1
                        display_board.select(clicked_row, clicked_col)

                try:
                    # Sketch input val onto screen
                    if 1 <= input_val <= 9:
                        display_board.sketch(input_val)
                        # Place sketch and reset background/lines/buttons
                        screen.fill(BG_GAME_COLOR)
                        display_board.sketch(input_val)  # Adds new sketch
                        display_board.draw()
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                        pygame.display.update()  # Updates board

                    # Turn sketch value into actual val
                    elif input_val == 0:
                        if display_board.current.editable and display_board.current.value:
                            display_board.current.value = 0
                        else:
                            display_board.place_number()
                        screen.fill(BG_GAME_COLOR)
                        display_board.draw()

                except:
                    pass  # If a user enters a number not 1-9 it will do nothing

        # replace buttons
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        pygame.display.update()


if __name__ == "__main__":
    main()
