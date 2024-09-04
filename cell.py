import pygame.font
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_val = None
        self.selected = False
        self.editable = True

    def set_cell_value(self):  # Sets an individual cell with the sketch that the user input
        self.value = self.sketched_val  # Sets value to value currently sketched
        self.sketched_val = None  # Sketched value reset to None

    def set_sketched_value(self, value):  # Sets the sketched value from keyboard input
        self.sketched_val = value

        # Render sketched value with pygame
        font_sketch = pygame.font.Font("button_font.ttf", 40)
        sketch_surface = font_sketch.render(str(value), True, SKETCH_COLOR)
        sketch_rectangle = sketch_surface.get_rect(
            center=((SQUARE_SIZE_MINI * self.row) + SQUARE_SIZE_MINI // 2,
                    (SQUARE_SIZE_MINI * self.col) + SQUARE_SIZE_MINI // 2))
        self.screen.blit(sketch_surface, sketch_rectangle)

    def draw(self):  # Draws the cell
        font_num = pygame.font.Font(None, 80)

        # Only displays cell if the value of cell is not 0
        if self.value != 0:
            num_surface = font_num.render(str(self.value), True, (0, 0, 0))
            num_rectangle = num_surface.get_rect(
                center=((SQUARE_SIZE_MINI * self.row) + SQUARE_SIZE_MINI // 2,
                        (SQUARE_SIZE_MINI * self.col) + SQUARE_SIZE_MINI // 2))
            self.screen.blit(num_surface, num_rectangle)

        # If the cell is currently selected then a red outline is drawn around the cell
        if self.selected:
            red_square = pygame.Rect(SQUARE_SIZE_MINI * self.row, SQUARE_SIZE_MINI * self.col, SQUARE_SIZE_MINI,
                                     SQUARE_SIZE_MINI)
            pygame.draw.rect(self.screen, (255, 0, 0), red_square, 2)
            self.selected = False  # The cell is no longer sketched so the red outline goes away

        # If there is a sketched value then it is rendered with "button_font.ttf"
        if self.sketched_val:
            font_sketch = pygame.font.Font("button_font.ttf", 40)
            sketch_surface = font_sketch.render(str(self.sketched_val), True, SKETCH_COLOR)
            sketch_rectangle = sketch_surface.get_rect(
                center=((SQUARE_SIZE_MINI * self.row) + SQUARE_SIZE_MINI // 2,
                        (SQUARE_SIZE_MINI * self.col) + SQUARE_SIZE_MINI // 2))
            self.screen.blit(sketch_surface, sketch_rectangle)
