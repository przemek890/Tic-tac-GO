import src.Game as gm
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("TICTACTOE")
    info = pygame.display.Info()
    screen_height = info.current_h
    screen = pygame.display.set_mode((screen_height - screen_height / 5, screen_height - screen_height / 5))
    #--------------------------------------------------
    game = gm.Game(screen)
    game.loop(screen)

main()
