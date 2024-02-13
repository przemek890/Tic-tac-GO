from src.AI import AI
""""""""""""""""""""""""
class Game:
    def __init__(self, screen, draw):
        self.screen = screen
        self.draw = draw
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.ai_player = 'O'
        self.ai = AI(self.screen, self.board)
        self.game_over = False

    def draw_symbol(self, row, col):
        if self.player == 'X':
            self.draw.draw_X(row, col)
        else:
            self.draw.draw_O(row, col)
        self.board[row][col] = self.player

        winner, winning_line = self.ai.check_win(self.board)
        if winner is not None:
            self.game_over = True
            if winning_line is not None:
                self.draw.draw_line(*winning_line[0], *winning_line[2])

    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def ai_move(self):
        score = self.ai.minimax(self.board, 9, True, self.ai_player, 'O' if self.ai_player == 'X' else 'X')
        if score[1] is not None:
            _ , (ai_row, ai_col) = score
            self.draw_symbol(ai_row, ai_col)
            self.switch_player()

    def reset(self):
        self.screen.fill((0, 0, 0))
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.ai.board = self.board
        self.game_over = False
        self.player = 'X'
        self.ai_player = 'O' if self.ai_player == 'X' else 'X'
        if self.ai_player == 'X':
            self.ai_move()

