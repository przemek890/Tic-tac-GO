import pygame
import os

class UI:
    def __init__(self, screen):
        path = os.getcwd() + '/../data/'
        image_files = ['tlo.png', 'board.png', 'assets.png', 'o.png', 'x.png', 'draw.png', 'cross.png', 'circle.png']

        self.background = pygame.image.load(path + 'tlo.png')
        self.screen_height = screen.get_height()
        self.background = pygame.transform.scale(self.background, (self.screen_height, self.screen_height))

        for image_file in image_files[1:]:
            setattr(self, image_file.split('.')[0], pygame.image.load(path + image_file))

        for image in [self.background, self.board, self.assets]:
            screen.blit(image, (0, 0))