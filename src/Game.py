import pygame
import src.Voice as voice
#-----------------------------
class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("TICTACTOE")
        self.background = pygame.image.load('./data/tlo.png')
        self.board = pygame.image.load('./data/board.png')
        self.assets = pygame.image.load('./data/assets.png')
        self.circle = pygame.image.load('./data/circle.png')
        self.cross = pygame.image.load('./data/cross.png')
        self.turn = False;
        #-----
        self.info = pygame.display.Info()
        self.screen_height = self.info.current_h
        self.screen = pygame.display.set_mode((self.screen_height - self.screen_height / 5, self.screen_height - self.screen_height / 5))
        self.background = pygame.transform.scale(self.background, (self.screen_height,self.screen_height))
        print(f'Create new game!')
    def loop(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.board, ((self.screen_height - self.screen_height / 5 - self.board.get_height()) / 2, (self.screen_height - self.screen_height / 5 - self.board.get_height()) / 2 - self.screen_height / 20))
        self.screen.blit(self.assets, (0, 0))
        running = True
        while running:
            pygame.display.update()
            self.circle_cross()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    def circle_cross(self):

        pozycja = voice.Voice()
        pozycja.audio_text()

        if(pozycja.text == "A1"):
            x = 91
            y = 85
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "A2"):
            x = 91
            y = 85 + 142
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text== "A3"):
            x = 91
            y = 85 + 142 * 2
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "B1"):
            x = 91 + 185
            y = 85
            if(pozycja.text == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True;
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "B2"):
            x = 91 + 185
            y = 85 + 142
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "B3"):
            x = 91 + 185
            y = 85 + 142 * 2
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "C1"):
            x = 91 + 185 * 2
            y = 85
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "C2"):
            x = 91 + 185 * 2
            y = 85 + 142
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        elif(pozycja.text == "C3"):
            x = 91 + 185 * 2
            y = 85 + 142 * 2
            if(self.turn == False):
                self.screen.blit(self.cross, (x, y))
                self.turn = True
            else:
                self.screen.blit(self.circle, (x, y))
                self.turn = False
        else:
            print("Blad pobierania pozycji - sprobuj ponownie!")
            return -1

        return 1


