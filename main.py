import pygame
from pygame.locals import *
import sys 
import random

#define screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

#define minefield parameters
FIELD_WIDTH = 10
FIELD_HEIGHT = 8
MINE_COUNT = 4

#define button size




#Define colours
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class button():
    def __init__(self, width, height, colour, locx, locy, text):
        self.width = width
        self.height = height
        self.colour = colour
        self.locx = locx
        self.locy = locy
        self.text = text
    
    def draw(self, _display_surf):
        pygame.draw.rect(_display_surf, self.colour, pygame.Rect(self.locx, self.locy, self.locx + self.width, self.locy + self.height))
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render(self.text , True , BLACK)
        _display_surf.blit(text, (30, 30))
        pygame.display.flip()

    def isOver(self):
        x, y = pygame.mouse.get_pos()
        if x >= self.locx and x <= self.locx + self.width:
            if y >= self.locy and y <= self.locy + self.height:
                return True

#Board parameters
class board:
    def __init__(self):
        self.width = FIELD_WIDTH
        self.height = FIELD_HEIGHT
        self.totalMines = MINE_COUNT
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, curMines):
        self.curMines = curMines
    


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        FPS = pygame.time.Clock()
        FPS.tick(60)

        self.size = self.weight, self.height = SCREEN_WIDTH, SCREEN_HEIGHT 
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(WHITE)
        pygame.display.set_caption("Game")
        self._running = True
        button1.draw(self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            for event in pygame.event.get():
                b1, b2, b3 = pygame.mouse.get_pressed(num_buttons=3)
                if b1:
                    if button1.isOver():
                        print("Button Pressed")
                # if b3:
                #     print("Right button pressed")

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                self.on_event(event)

            self._display_surf.fill(WHITE)
            # b.draw(self._display_surf)
            

            self.on_loop()
            self.on_render()
        self.on_cleanup()


# b = board()
button1 = button(20, 20, RED, 40, 30, "Button")

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

