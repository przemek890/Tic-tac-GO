import pygame

class Frontend:
    def __init__(self,screen):
        self.background = pygame.image.load('./data/tlo.png')
        self.board = pygame.image.load('./data/board.png')
        self.assets = pygame.image.load('./data/assets.png')
        self.o = pygame.image.load('./data/o.png')
        self.x = pygame.image.load('./data/x.png')
        self.draw = pygame.image.load("./data/draw.png")
        self.cross = pygame.image.load('./data/cross.png')
        self.circle = pygame.image.load('./data/circle.png')
        self.screen_height = screen.get_height()
        self.background = pygame.transform.scale(self.background, (self.screen_height,self.screen_height))
        screen.blit(self.background, (0, 0))
        screen.blit(self.board, (0,0))
        screen.blit(self.assets, (0, 0))