import pygame
import os
from UI.fr import Draw
from src.Game import Game
""""""""""""""""""""""""""
def main():
    pygame.init()
    pygame.display.set_caption("TIC-TAC-TOE")

    info = pygame.display.Info()
    screen_height = info.current_h
    # screen_width = info.current_w

    size = (screen_height // 2, screen_height // 2)
    screen = pygame.display.set_mode(size)

    os.environ['SDL_VIDEO_CENTERED'] = '1'

    draw = Draw(screen)
    game = Game(screen, draw)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
                elif event.key == pygame.K_q:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and game.game_over == False:
                x, y = pygame.mouse.get_pos()
                row, col = y // draw.cell_size, x // draw.cell_size
                if game.board[row][col] == '':
                    game.draw_symbol(row, col)
                    game.switch_player()
                    if game.player == game.ai_player:
                        game.ai_move()

        draw.draw_board()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()