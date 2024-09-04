import pygame
from constants import *
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # Create 2d array of game board with only 0's in it
        self.cells = [[Cell(0, i, j, screen) for j in range(9)] for i in range(9)]
        # Current is the currently selected cell
        self.current = None

    def draw(self):  # Draws game board thin lines and thick lines to make 3x3 boxes
        for i in range(1, 4):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (0, i * SQUARE_SIZE_BOLD),
                             (self.width, i * SQUARE_SIZE_BOLD), LINE_WIDTH_BOLD)
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (i * SQUARE_SIZE_BOLD, 0),
                             (i * SQUARE_SIZE_BOLD, self.height), LINE_WIDTH_BOLD)
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (0, i * SQUARE_SIZE_MINI),
                             (self.width, i * SQUARE_SIZE_MINI), LINE_WIDTH_MINI)
        for i in range(4, 6):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (0, i * SQUARE_SIZE_MINI),
                             (self.width, i * SQUARE_SIZE_MINI), LINE_WIDTH_MINI)
        for i in range(7, 9):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (0, i * SQUARE_SIZE_MINI),
                             (self.width, i * SQUARE_SIZE_MINI), LINE_WIDTH_MINI)
        for i in range(1, 3):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (i * SQUARE_SIZE_MINI, 0),
                             (i * SQUARE_SIZE_MINI, self.height), LINE_WIDTH_MINI)
        for i in range(4, 6):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (i * SQUARE_SIZE_MINI, 0),
                             (i * SQUARE_SIZE_MINI, self.height), LINE_WIDTH_MINI)
        for i in range(7, 9):
            pygame.draw.line(self.screen, LINE_COLOR_BOARD, (i * SQUARE_SIZE_MINI, 0),
                             (i * SQUARE_SIZE_MINI, self.height), LINE_WIDTH_MINI)

        # Prints board onto screen by calling draw on each cell
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()  # Draw is in the cell class

    def select(self, row, col):  # Selects a cell and indicates using a red square
        self.cells[row][col].selected = True  # Sets cell to be selected as being selected in cell class
        self.draw()  # Draws cell with red square
        self.current = self.cells[row][col]  # Saves cell to current so it can be sketched or placed

    # Each cell is 70 px by 70 px so dividing by 70 and converting to int gives col and row
    def click(self, x, y):  # Returns a tuple of the clicked row and col
        if x <= self.width and y <= self.height:
            clicked_row = int(y / 70)
            clicked_col = int(x / 70)
            return clicked_row, clicked_col

        return None

    def sketch(self, value):  # Sketches the entered number into the cell
        # Checks if cell is editable if it then a value can be sketched on it
        if self.current.editable:
            self.current.set_sketched_value(value)

    def place_number(self):  # Places the number in the cell
        # Checks if editable so that user does not edit original board then places number onto board
        if self.current.editable:
            self.current.set_cell_value()

    def reset_to_original(self):  # Resets the board to the original
        for i in range(9):  # For loop to go through all cells.
            for j in range(9):
                if self.cells[i][j].editable:  # If the cell is editable then set both value and sketched value to 0
                    self.cells[i][j].value = 0
                    self.cells[i][j].sketched_val = 0

        self.draw()  # Re-draw board

    def is_full(self):
        # If there is still empty cells
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:  # Iterates through all cells and checks if there is 0 (empty cell)
                    return False

        # If board is full
        return True

    def check_board(self, board_correct):  # Checks the board to see if it matches the correct arrangement
        # Creates a 2d array using a list comprehension of the value in cells
        board = [[self.cells[i][j].value for j in range(9)] for i in range(9)]

        # If the board is incorrect
        for i in range(9):  # A for loop is then used to compare each num in board and board_correct
            for j in range(9):
                if board[i][j] != board_correct[i][j]:
                    return False

        # If the board is correct
        return True
