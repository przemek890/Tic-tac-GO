import src.Game as gm
#--------
class AI:
    def __init__(self,screen,board):
        self.screen = screen
        self.board = board
    def get_empty_cells(self, board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    def check_win(self, board):
        # Sprawdź, czy któryś z graczy wygrał.
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return board[0][2]

        # Sprawdź, czy plansza jest już pełna.
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return None
        return 'tie'
    def minimax(self,board, depth, is_maximizing,znak_1,znak_2):
        # Sprawdź, czy gra została zakończona lub osiągnięto maksymalną głębokość rekursji.
        pom = 0
        for i in board:
            for j in i:
                if j == ' ':
                    pom += 1
        if(pom == 9): return float('inf') ,(1,1)

        result = self.check_win(self.board)
        if result is not None:
            score = 10 - depth if result == znak_1 else depth - 10 if result == znak_2 else 0
            return score, None
        if depth == 0:
            return 0, None

        # Przeglądaj wszystkie możliwe ruchy dla gracza.
        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None
        for i, j in self.get_empty_cells(board):
            board[i][j] = znak_1 if is_maximizing else znak_2
            score, _ = self.minimax(board, depth - 1, not is_maximizing,znak_1,znak_2)
            board[i][j] = ' '
            if is_maximizing and score > best_score:
                best_score, best_move = score, (i, j)
            elif not is_maximizing and score < best_score:
                best_score, best_move = score, (i, j)
        return best_score, best_move