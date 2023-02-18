import pygame
from pygame.locals import *
import sys 


pygame.init()
FPS = pygame.time.Clock()
FPS.tick(60)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = SCREEN_WIDTH, SCREEN_HEIGHT 
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
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

        
        object1 = pygame.Rect((20, 50), (50, 100))
        object2 = pygame.Rect((10, 10), (100, 100))
        
        print(object1.colliderect(object2))
        while( self._running ):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame/quit()
                    sys.exit()
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

