import pygame
#-----------------------------
class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("TICTACTOE")
        self.image = pygame.image.load('./data/board.png')
        self.background = pygame.image.load('./data/tlo.png')
        self.info = pygame.display.Info()
        self.screen_width = self.info.current_w
        self.screen_height = self.info.current_h
        self.screen = pygame.display.set_mode((self.screen_height - self.screen_height/5  , self.screen_height - self.screen_height/5 ))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.image, (( self.screen_height - self.screen_height/5 -self.image.get_height())/2,( self.screen_height - self.screen_height/5 -self.image.get_height())/2 - self.screen_height/50))
        print(f'Create new game!')
    def loop(self):
        # Odśwież ekran
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()


