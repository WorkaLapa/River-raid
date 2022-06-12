import pygame
import random

pygame.init()
okno=pygame.display.set_mode(size=(900,600))
clock=pygame.time.Clock()
lvl_speed=3
bok = 50*(random.randint(1,8))
lap=1
lvl_length=22*50

def pasmo(kolejnosc, zbior):
    pasl=pygame.Rect(0, -50*(kolejnosc), bok*50, 50)
    pasp=pygame.Rect(900-bok*50, -50*(kolejnosc), bok*50, 50)
    zbior.append(pasl)
    zbior.append(pasp)

def enemy(kolejnosc, szer, zbiorwrog, zbiorpali):
    los = random.randint(1,10)
    if los == 1: #heli
        wrog = pygame.Rect(450, -50*(kolejnosc+1), 30, 30)
        zbiorwrog.append(wrog)
    elif los == 2: #statek
        wrog = pygame.Rect(450, -50*(kolejnosc+1), 70, 25)
        zbiorwrog.append(wrog)
    elif los == 8 or los == 7: #fuel
        szerter = random.randint(szer*50, 900-szer*50)
        #szerokość losowana z szer*50 od lewej (lewy bok ściany) do prawego boku ściany (900-szer*50)
        wrog = pygame.Rect(szerter, -50*(kolejnosc+1), 30, 50)
        zbiorpali.append(wrog)
        print(los)


"""
3 laps - nadpisywanie jednego na drugim or sth - albo jedno stałe lap i nadpisywanie lap na drugim?
"""

if lap==1:
    blocks=[]
    wrog=[]
    fuel=[]
    a=2
    b=20
    c=22
    for i in range(a):
        bok = 8
        pasmo(i, blocks)
        enemy(i, bok, wrog, fuel)
    for i in range(a, b):
        bok = 4
        pasmo(i, blocks)
        enemy(i, bok, wrog, fuel)
    for i in range(b, c):
        bok = 2
        pasmo(i, blocks)
        enemy(i, bok, wrog, fuel)
        pygame.display.flip()



run = True


while run:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                run = False
                exit()
    for block in blocks:
        block.move_ip(0, lvl_speed)
    for enemy in wrog:
        enemy.move_ip(0, lvl_speed)
    for zbiornik in fuel:
        zbiornik.move_ip(0, lvl_speed)

    okno.fill((0, 0, 0))
    for block in blocks:
        pygame.draw.rect(okno, (0, 255, 0), block)
    for enemy in wrog:
        pygame.draw.rect(okno, (0, 100, 100), enemy)
    for zbiornik in fuel:
        pygame.draw.rect(okno, (160, 32, 50), zbiornik)

    pygame.display.flip()
    clock.tick(40)
