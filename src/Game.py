import front.Front as front
import src.Click as click
import src.AI as ai
import pygame
#--------
class Game:
    def __init__(self, screen,start):
        self.map = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.screen = screen
        self.interface = front.Frontend(self.screen)
        self.PC = ai.AI(screen,self.map)
        self.turn = False
        self.start = start

    def loop(self,screen):
        running = True
        pom = 0
        while running:
            pygame.display.update()
            if (self.turn == self.start):
                for event in pygame.event.get():
                    poz = click.Click()
                    poz.get_position()
                    if event.type == pygame.QUIT: running = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        pom += 1
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        poz = click.Click()
                        poz.get_position()
                        self.circle_cross(poz.pozycja,self.map)
            else:
                if(self.start == False):
                    score = self.PC.minimax(self.map, 9, True,'O','X')
                else:
                    score = self.PC.minimax(self.map, 9, True, 'X', 'O')
                if(score[1] != None):
                    pozycja = str(chr(score[1][0] + 65)) + str(score[1][1] + 1)
                    self.circle_cross(pozycja,self.map)
                    result = self.PC.check_win(self.map)
                    if result is not None:
                        if self.turn == self.start:
                            self.turn = not self.start
                        else:
                            self.turn = self.start

            result = self.PC.check_win(self.map)
            if result == "X":
                self.screen.blit(self.interface.x, (420, 649))
            elif result == "O":
                self.screen.blit(self.interface.o, (420, 649))
            else:
                pp = 0
                for i in self.map:
                    for j in i:
                        if j == ' ':
                            pp = pp + 1
                if(pp == 0):
                    self.screen.blit(self.interface.draw, (420, 665))

            # ---------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    pom += 1
                    running = False

        if(pom == 1):
            game = Game(screen,not self.start)
            game.loop(screen)
        else:
            pygame.quit()
    # ------
    def circle_cross(self,pozycja,map):
        if (pozycja == "A1" and map[0][0] == ' '):
            x = 84 + 84 - 172 / 2
            y = 46 + 84 - 172 / 2
            if(self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[0][0] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[0][0] = "O"
                self.turn = False
        elif (pozycja == "A2" and map[0][1] == ' '):
            x = 84 + 84 - 172 / 2
            y = 46 + 84 * 3 - 172 / 2 + 25
            if (self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[0][1] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[0][1] = "O"
                self.turn= False
        elif (pozycja== "A3" and map[0][2] == ' '):
            x = 84 + 84 - 172 / 2
            y = 46 + 84 * 5 - 172 / 2 + 25 * 2
            if (self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[0][2] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[0][2] = "O"
                self.turn = False
        elif (pozycja== "B1" and map[1][0] == ' '):
            x = 84 + 84 * 3 - 172 / 2 + 25
            y = 46 + 84 - 172 / 2
            if (self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[1][0] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[1][0] = "O"
                self.turn = False
        elif (pozycja == "B2" and map[1][1] == ' '):
            x = 84 + 84 * 3 - 172 / 2 + 25
            y = 46 + 84 * 3 - 172 / 2 + 25
            if (self.turn== False):
                self.screen.blit(self.interface.cross, (x, y))
                map[1][1] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[1][1] = "O"
                self.turn = False
        elif (pozycja == "B3" and map[1][2] == ' '):
            x = 84 + 84 * 3 - 172 / 2 + 25
            y = 46 + 84 * 5 - 172 / 2 + 25 * 2
            if (self.turn== False):
                self.screen.blit(self.interface.cross, (x, y))
                map[1][2] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[1][2] = "O"
                self.turn = False
        elif (pozycja == "C1" and map[2][0] == ' '):
            x = 84 + 84 * 5 - 172 / 2 + 25 * 2
            y = 46 + 84 - 172 / 2
            if(self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[2][0] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[2][0] = "O"
                self.turn = False
        elif (pozycja == "C2" and map[2][1] == ' '):
            x = 84 + 84 * 5 - 172 / 2 + 25 * 2
            y = 46 + 84 * 3 - 172 / 2 + 25
            if (self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[2][1] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[2][1] = "O"
                self.turn = False
        elif (pozycja == "C3" and map[2][2] == ' '):
            x = 84 + 84 * 5 - 172 / 2 + 25 * 2
            y = 46 + 84 * 5 - 172 / 2 + 25 * 2
            if (self.turn == False):
                self.screen.blit(self.interface.cross, (x, y))
                map[2][2] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[2][2] = "O"
                self.turn = False
        else:
            print("Blad pobierania pozycji - sprobuj ponownie!")
            return -1

        return 1













