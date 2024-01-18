import src.Game as gm
import pygame

# Constants
SCREEN_RATIO = 1 / 3
GAME_START = False

def main():
    pygame.init()
    pygame.display.set_caption("TICTACTOE")
    info = pygame.display.Info()
    screen_height = info.current_h
    screen_size = (screen_height - screen_height * SCREEN_RATIO, screen_height - screen_height * SCREEN_RATIO)
    screen = pygame.display.set_mode(screen_size)

    game = gm.Game(screen, GAME_START)
    game.loop(screen)

main()
