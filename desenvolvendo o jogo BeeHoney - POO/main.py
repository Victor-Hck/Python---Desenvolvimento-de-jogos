import pygame
from objeto import Obj

class Main:
    
    def __init__(self, sizex, sizey, title):
        
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        
        self.loop = True
        
        self.start_screen = Obj("desenvolvendo o jogo BeeHoney - POO/assets/start.png", 0, 0)
    
    def draw(self):
        self.drawing(self.window)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
    
    def update(self):
        while self.loop:
            self.events()
            self.draw()
            pygame.display.update()

pygame.init()
game = Main(360, 640, "BeeHoney")
game.update()
pygame.quit()
