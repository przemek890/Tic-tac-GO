import Front.Front as front
import src.Click as click
import src.AI as ai
import pygame
#--------
class Game:
    def __init__(self, screen):
        self.map = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.screen = screen
        self.interface = front.Frontend(self.screen)
        self.PC = ai.AI(screen,self.map)
        self.turn = False

    def loop(self,screen):
        running = True
        pom = 0
        while running:
            pygame.display.update()
            if (self.turn == False):
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
                        result = self.PC.check_win(self.map)
                        if result is not None:
                            self.screen.blit(self.interface.x, (300, 655))
            else:
                score = self.PC.minimax(self.map, 9, True)
                if(score[1] != None):
                    pozycja = str(chr(score[1][0] + 65)) + str(score[1][1] + 1)
                    self.circle_cross(pozycja,self.map)
                    result = self.PC.check_win(self.map)
                    if result is not None:
                        self.screen.blit(self.interface.o, (300, 652))
                        self.turn = True


            # ---------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    pom += 1
                    running = False

        if(pom == 1):
            game = Game(screen)
            game.loop(screen)
        else:
            print(pom)
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













