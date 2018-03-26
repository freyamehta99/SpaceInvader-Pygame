import time
import pygame
display = pygame.display.set_mode((700, 700))

class meraantrikshyaan:
    def __init__(self, x, y, w, h):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
    

    def draw(self):
        pygame.draw.rect(display, (241,196,15), (self.x + self.w/2 - 8, self.y - 10, 16, 10))
        pygame.draw.rect(display,  (244,246,247), (self.x, self.y, self.w, self.h))
    