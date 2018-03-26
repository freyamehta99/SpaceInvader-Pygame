import time
import pygame

display = pygame.display.set_mode((700, 700))

class Missiles:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        if (x < self.x < x + d) and (y + d > self.y > y):
            return True

class missile(Missiles):
    def __init__(self, x, y):
        self.speed = -5
        self.d = 10
        Missiles.__init__(self,x,y)

    def draw(self):
        pygame.draw.ellipse(display, (186,74,0), (self.x, self.y, self.d, self.d))

    # def move(self):
    #     pass

    # def hit(self, x, y, d):
    #     pass
# both the bullets hit the enemy now properly

class missile2(Missiles):
    def __init__(self, x, y):
        self.speed = -10
        self.d = 20
        Missiles.__init__(self,x,y)

    def draw(self):
        pygame.draw.ellipse(display, (128,0,0) , (self.x, self.y, self.d, self.d))

    # def move(self):
    #     pass

    # def hit(self, x, y, d):
    #     pass
