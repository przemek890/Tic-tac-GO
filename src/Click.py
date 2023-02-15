import pygame
#--------
class Click:
    def __init__(self):
        self.pozycja = None
    def get_position(self):
        cursor = pygame.mouse.get_pos()
        if(cursor[0] > 84 and cursor[0] < 84 + 172  and cursor[1] > 46 and cursor[1] < 46 + 172 ):
            self.pozycja = "A1"
        elif(cursor[0] > 84 and cursor[0] < 84 + 172 and cursor[1] > 46 + 172 + 25 and cursor[1] < 46 + 172 * 2 + 25 ):
            self.pozycja = "A2"
        elif(cursor[0] > 84 and cursor[0] < 84 + 172 and cursor[1] > 46 + 172 * 2 + 25 * 2 and cursor[1] < 46 + 172 * 3 + 25 * 2 ):
            self.pozycja = "A3"
        elif(cursor[0] > 84 + 172 + 25 and cursor[0] < 84 + 172 * 2 + 25  and cursor[1] > 46 and cursor[1] < 46 + 172 ):
            self.pozycja = "B1"
        elif(cursor[0] > 84 + 172 + 25 and cursor[0] < 84 + 172 * 2 + 25 and cursor[1] > 46 + 172 + 25 and cursor[1] < 46 + 172 * 2 + 25   ):
            self.pozycja = "B2"
        elif(cursor[0] > 84 + 172 + 25 and cursor[0] < 84 + 172 * 2 + 25  and cursor[1] > 46 + 172 * 2 + 25 * 2 and cursor[1] < 46 + 172 * 3 + 25 * 2 ):
            self.pozycja = "B3"
        elif(cursor[0] > 84 + 172 * 2 + 25 * 2 and cursor[0] < 84 + 172 * 3 + 25 * 2  and cursor[1] > 46 and cursor[1] < 46 + 172 ):
            self.pozycja = "C1"
        elif(cursor[0] > 84 + 172 * 2 + 25 * 2 and cursor[0] < 84 + 172 * 3 + 25 * 2  and cursor[1] > 46 + 172 + 25 and cursor[1] < 46 + 172 * 2 + 25 ):
            self.pozycja = "C2"
        elif(cursor[0] > 84 + 172 * 2 + 25 * 2 and cursor[0] < 84 + 172 * 3 + 25 * 2  and cursor[1] > 46 + 172 * 2 + 25 * 2 and cursor[1] < 46 + 172 * 3 + 25 * 2 ):
            self.pozycja = "C3"
        elif (cursor[0] > 338 and cursor[0] < 457 and cursor[1] > 700 and cursor[1] < 730):
            self.pozycja = "RESET"
