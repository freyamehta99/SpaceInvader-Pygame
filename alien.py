import time
import pygame

display = pygame.display.set_mode((700, 700))


class Alien:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.x_dir = 1
        self.speed = 0
        # print time.time()
        self.tmp = 0
        self.willdie = 0
        self.lifetime = time.time()

    def draw(self):
        pygame.draw.ellipse(display, (35,155,86), (self.x, self.y, self.d, self.d))
        pygame.draw.rect(display, (23,32,42), (self.x, self.y+self.d-20, 50, 7))

    def draw2(self):
        pygame.draw.ellipse(display, (186,74,0), (self.x, self.y, self.d, self.d))
        pygame.draw.rect(display, (23,32,42), (self.x, self.y+self.d-20, 50, 7))

    def visitonlyonce(self):
        if self.tmp == 0:
            self.tmp = 1
            return True
        else:
            return False

    def move(self):
        self.x += self.x_dir*self.speed

    def iskillalien(self):
        maarde = time.time() - self.lifetime
        if maarde >= 8:
            # print 'entering here'
            return True
        else:
            # print "self time " + str(self.lifetime) 
            # print "current time " + str(time.time())
            return False

    def dieinfive(self):
        self.willdie = 1
        # print 'will kill after five'
        self.lifetime = time.time() - 3  ;

    def shift_down(self):
        self.y += self.d
