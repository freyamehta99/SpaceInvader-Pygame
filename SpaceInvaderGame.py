import pygame
import sys
import time
import random

from alien import Alien
from missiles import missile
from missiles import missile2
from spaceship import meraantrikshyaan

pygame.init()
display = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
global inittime
inittime=0

def check():
    currtime = time.time()
    global inittime
    diff = currtime - inittime    
    if diff >= 10:
        inittime = currtime;
        return True
    else:
        return False


global hit 
hit = 0

Chotafont = pygame.font.SysFont("Arial", 40)
Badafont = pygame.font.SysFont("Arial", 50)

def GameOver():
    text1 = Badafont.render("Game Over!", True, (253,254,254))
    text2 = Chotafont.render("Your Score is :  ", True, (253,254,254))
    text3 = Chotafont.render(str(hit), True, (253,254,254))
    display.blit(text1, (180, 300))
    display.blit(text2, (105, 450))
    display.blit(text3, (400, 450))

def game():
    hallabol = False
    merinaav = meraantrikshyaan(310, 660, 80, 30)

    bullets = []
    bullets2 = []
    num_bullet = 0
    num_bullet2 =0

    for i in range(num_bullet2):
        i = missile2(345,650)
        bullets2.append(i)

    for i in range(num_bullet):
        i = missile(345, 650)
        bullets.append(i)

    x_move = 0

    aliens = []
    kitnealienthe = random.randint(1,9)

    global outputaliens
    outputaliens = kitnealienthe
    
    for i in range(1):
        tmp = random.randint(0,5)
        ali = Alien((tmp+1)*50 + tmp*20,70, 50)
        aliens.append(ali)

    while not hallabol:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    GameOver()
                    pygame.display.update()
                    time.sleep(5)
                    hallabol = True
                   

                if event.key == pygame.K_d:
                    x_move = 8

                if event.key == pygame.K_a:
                    x_move = -8

                if event.key == pygame.K_SPACE:
                    num_bullet += 1
                    i = missile(merinaav.x + 35, merinaav.y)
                    bullets.append(i)

                if event.key == pygame.K_s:
                	num_bullet2 +=1
                	i = missile2(merinaav.x + 35, merinaav.y)
                	bullets2.append(i)

            if event.type == pygame.KEYUP:
                x_move = 0

        display.fill((8,8,8))

        for i in range(num_bullet):
            bullets[i].draw()
            bullets[i].move()


        for i in range(num_bullet2):
        	bullets2[i].draw()
        	bullets2[i].move()

        for alien in aliens:
            if alien.willdie == 0:
                alien.draw()
            else:
                alien.draw2()

            for item in bullets:
                if item.hit(alien.x, alien.y, alien.d):
                    bullets.remove(item)
                    num_bullet -= 1
                    global hit
                    hit +=1
                    # print 'hitting'
                    aliens.remove(alien)
                    kitnealienthe -= 1
            for item in bullets2:
                if item.hit(alien.x, alien.y, alien.d):
                    bullets2.remove(item)
                    num_bullet2 -= 1
                    alien.dieinfive()
                    alien.draw2()
                    # print 'hitting'
                    isincrement=alien.visitonlyonce()
                    if isincrement:
                        hit += 1
                    
                    # kitnealienthe -= 1 #added at last toh check pehle                    

        

        for alien in aliens:
            canikill = alien.iskillalien()
            if canikill:
                kitnealienthe -= 1
                aliens.remove(alien)
                # print 'hitting'
                # hit+=1
                

        checkche = check()
        if checkche:
            tmp = random.randint(0,5)
            ali = Alien((tmp+1)*50 + tmp*20,70, 50)
            aliens.append(ali)
            kitnealienthe  += 1            

        merinaav.x += x_move

        if merinaav.x < 0:
            merinaav.x -= x_move
        if merinaav.x + 80 > 700:
            merinaav.x -= x_move

        merinaav.draw()

        pygame.display.update()
        clock.tick(60)

game()
pygame.quit()
sys.exit()