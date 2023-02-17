import pygame
import os

class Frontend:
    def __init__(self,screen):
        if os.name == "posix":
            path = "./"
        elif os.name == "nt":
            path = "../"
        self.background = pygame.image.load('{}data/tlo.png'.format(path))
        self.board = pygame.image.load('{}data/board.png'.format(path))
        self.assets = pygame.image.load('{}data/assets.png'.format(path))
        self.o = pygame.image.load('{}data/o.png'.format(path))
        self.x = pygame.image.load('{}data/x.png'.format(path))
        self.draw = pygame.image.load('{}data/draw.png'.format(path))
        self.cross = pygame.image.load('{}data/cross.png'.format(path))
        self.circle = pygame.image.load('{}data/circle.png'.format(path))
        self.screen_height = screen.get_height()
        self.background = pygame.transform.scale(self.background, (self.screen_height,self.screen_height))
        screen.blit(self.background, (0, 0))
        screen.blit(self.board, (0,0))
        screen.blit(self.assets, (0, 0))