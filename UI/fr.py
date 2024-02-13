import pygame
""""""""""""""
class Draw:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.cell_size = min(self.width, self.height) // 3

    def draw_board(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, (255, 255, 255), (i * self.cell_size, 0), (i * self.cell_size, self.height), 15)
            pygame.draw.line(self.screen, (255, 255, 255), (0, i * self.cell_size), (self.width, i * self.cell_size), 15)

    def draw_X(self, row, col):
        margin = self.cell_size // 4
        pygame.draw.line(self.screen, (255, 0, 0), (col * self.cell_size + margin, row * self.cell_size + margin), ((col + 1) * self.cell_size - margin, (row + 1) * self.cell_size - margin), 15)
        pygame.draw.line(self.screen, (255, 0, 0), ((col + 1) * self.cell_size - margin, row * self.cell_size + margin), (col * self.cell_size + margin, (row + 1) * self.cell_size - margin), 15)

    def draw_O(self, row, col):
        margin = self.cell_size // 4
        pygame.draw.circle(self.screen, (0, 0, 255), (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2), self.cell_size // 2 - margin, 15)

    def draw_line(self, start_row, start_col, end_row, end_col):
        start_x = start_col * self.cell_size + self.cell_size // 2
        start_y = start_row * self.cell_size + self.cell_size // 2
        end_x = end_col * self.cell_size + self.cell_size // 2
        end_y = end_row * self.cell_size + self.cell_size // 2
        pygame.draw.line(self.screen, (0, 255, 0), (start_x, start_y), (end_x, end_y), 5)