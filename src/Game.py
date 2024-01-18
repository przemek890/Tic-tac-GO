from UI.fr import UI as Ui
from src.Click import Click as click
from src.AI import AI as ai
import pygame
#--------
class Game:
    def __init__(self, screen,start):
        self.map = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.screen = screen
        self.interface = Ui(self.screen)
        self.PC = ai(screen,self.map)
        self.turn = False
        self.start = start
        self.poz = click()

    def loop(self,screen):
        running = True
        pom = 0
        while running:
            pygame.display.update()
            if (self.turn == self.start):
                for event in pygame.event.get():
                    self.poz = click()
                    self.poz.get_position()
                    if event.type == pygame.QUIT: running = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        pom += 1
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.poz = click()
                        self.poz.get_position()
                        self.circle_cross(self.poz.pozycja,self.map)
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
    def draw(self, position, map, x, y):
        if map[position[0]][position[1]] == ' ':
            if self.turn == False:
                self.screen.blit(self.interface.cross, (x, y))
                map[position[0]][position[1]] = "X"
                self.turn = True
            else:
                self.screen.blit(self.interface.circle, (x, y))
                map[position[0]][position[1]] = "O"
                self.turn = False
        else:
            print("Blad pobierania pozycji - sprobuj ponownie!")

    def circle_cross(self, pozycja, map):
        positions = {
            "A1": ([0, 0], 84 + 84 - 172 / 2, 46 + 84 - 172 / 2),
            "A2": ([0, 1], 84 + 84 - 172 / 2, 46 + 84 * 3 - 172 / 2 + 25),
            "A3": ([0, 2], 84 + 84 - 172 / 2, 46 + 84 * 5 - 172 / 2 + 25 * 2),
            "B1": ([1, 0], 84 + 84 * 3 - 172 / 2 + 25, 46 + 84 - 172 / 2),
            "B2": ([1, 1], 84 + 84 * 3 - 172 / 2 + 25, 46 + 84 * 3 - 172 / 2 + 25),
            "B3": ([1, 2], 84 + 84 * 3 - 172 / 2 + 25, 46 + 84 * 5 - 172 / 2 + 25 * 2),
            "C1": ([2, 0], 84 + 84 * 5 - 172 / 2 + 25 * 2, 46 + 84 - 172 / 2),
            "C2": ([2, 1], 84 + 84 * 5 - 172 / 2 + 25 * 2, 46 + 84 * 3 - 172 / 2 + 25),
            "C3": ([2, 2], 84 + 84 * 5 - 172 / 2 + 25 * 2, 46 + 84 * 5 - 172 / 2 + 25 * 2)
        }

        if pozycja in positions:
            self.draw(positions[pozycja][0], map, positions[pozycja][1], positions[pozycja][2])