import pygame
import random
import sys

pygame.init()
okno=pygame.display.set_mode(size=(900,700))
clock=pygame.time.Clock()
lvl_speed=3
bok = 50*(random.randint(1,8))
lap=1
lvl_length=22*50
petla = 0
#ZMIENNE KOLORÓW ORAZ WYMIARY PASKA PALIWA
BLACK = (0, 0, 0)
GREEN = (0, 225, 0)
YELLOW = (225, 225, 0)
RED = (225, 0, 0)
x = 10
y = 610
wys = 25


umieszczenie_poziom = 100
umieszczenie_pion = 550
szerokosc_obiektu = 15
wysokosc_obiektu = 35
predkosc_samolotu = 5
enemy_speed=3
def pasmo(kolejnosc, zbior):
    pasl=pygame.Rect(0, -50*(kolejnosc), bok*50, 50)
    pasp=pygame.Rect(900-bok*50, -50*(kolejnosc), bok*50, 50)
    zbior.append(pasl)
    zbior.append(pasp)

def enemy(kolejnosc, szer, zbiorwrog, zbiorpali):
    los = random.randint(1,10)
    if los == 1: #heli
        szerter = random.randint(szer*50, 900-(szer+1)*50)
        wrog = pygame.Rect(szerter, -50*(kolejnosc), 30, 30)
        zbiorwrog.append(wrog)
    elif los == 2: #statek
        szerter = random.randint(szer*50, 900-(szer+1)*50-20)
        wrog = pygame.Rect(szerter, -50*(kolejnosc), 70, 25)
        zbiorwrog.append(wrog)
    elif los == 8: #fuel
        szerter = random.randint(szer*50, 900-(szer+1)*50)
        #szerokość losowana z szer*50 od lewej (lewy bok ściany) do prawego boku ściany (900-szer*50)
        wrog = pygame.Rect(szerter, -50*(kolejnosc), 30, 50)
        zbiorpali.append(wrog)
        print(los)


blocks=[]
wrog=[]
fuel=[]
a=2
b=20
c=22
for i in range(a):
    bok = 7
    pasmo(i, blocks)
    enemy(i, bok, wrog, fuel)
for i in range(a, b):
    bok = 5
    pasmo(i, blocks)
    enemy(i, bok, wrog, fuel)
for i in range(b, c):
    bok = 7
    pasmo(i, blocks)
    enemy(i, bok, wrog, fuel)


for _ in range(30):
    los = random.randint(1,8)
    b = c+los
    for i in range(c, b):
        bok = random.randint(1,8)
        pasmo(i, blocks)
        enemy(i, bok, wrog, fuel)
    los = random.randint(1,8)
    c = b+los
    for i in range(b, c):
        bok = random.randint(1,8)
        pasmo(i, blocks)
        enemy(i, bok, wrog, fuel)

trwanie_gry=True

while trwanie_gry:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            trwanie_gry = False
    przyciski = pygame.key.get_pressed()
    if przyciski[pygame.K_LEFT] and umieszczenie_poziom>0:
        umieszczenie_poziom-= predkosc_samolotu
    if przyciski[pygame.K_RIGHT] and umieszczenie_poziom<900-szerokosc_obiektu:
        umieszczenie_poziom += predkosc_samolotu
    if przyciski[pygame.K_UP]:
        lvl_speed+=0.2
    if przyciski[pygame.K_DOWN] and lvl_speed>=1:
        lvl_speed-=0.2
    okno.fill((0, 0, 255))
    samolot=pygame.draw.rect(okno, (255, 223, 0), (umieszczenie_poziom, umieszczenie_pion, szerokosc_obiektu, wysokosc_obiektu))


    for block in blocks:
        block.move_ip(0, lvl_speed)
    for enemy in wrog:
        enemy.move_ip(0, lvl_speed)
    for zbiornik in fuel:
        zbiornik.move_ip(0, lvl_speed)


    for block in blocks:
        pygame.draw.rect(okno, (0, 255, 0), block)
        if block.colliderect(samolot):
            trwanie_gry=False
    for enemy in wrog:
        pygame.draw.rect(okno, (0, 100, 100), enemy)
        if enemy.colliderect(samolot):
            trwanie_gry=False

    for zbiornik in fuel:
        pygame.draw.rect(okno, (160, 32, 50), zbiornik)
        kolizja_z_paliwem = zbiornik.colliderect(samolot)
        if kolizja_z_paliwem == True:
            petla = 100



#PĘTLA ZUŻYCIA PALIWA I JEGO DOŁADOWYWANIA
    if petla<150:
        poj = 300
    elif petla <200:
        poj = 290
    elif petla <250:
        poj = 280
    elif petla <300:
        poj = 270
    elif petla <350:
        poj = 260
    elif petla <400:
        poj = 250
    elif petla <450:
        poj = 240
    elif petla <500:
        poj = 230
    elif petla <550:
        poj = 220
    elif petla <600:
        poj = 210
    elif petla <650:
        poj = 200
    elif petla <700:
        poj = 190
    elif petla <750:
        poj = 180
    elif petla <800:
        poj = 170
    elif petla <850:
        poj = 160
    elif petla <900:
        poj = 150
    elif petla <950:
        poj = 140
    elif petla <1000:
        poj = 130
    elif petla <1050:
        poj = 120
    elif petla <1100:
        poj = 110
    elif petla <1150:
        poj = 100
    elif petla <1200:
        poj = 90
    elif petla <1250:
        poj = 80
    elif petla <1300:
        poj = 70
    elif petla <1350:
        poj = 60
    elif petla <1400:
        poj = 50
    elif petla <1450:
        poj = 40
    elif petla <1500:
        poj = 30
    elif petla <1550:
        poj = 20
    elif petla <1600:
        poj = 10
    elif petla <1650:
        exit()
    if poj>150:
        col = GREEN
    elif poj>50:
        col = YELLOW
    else:
        col = RED
    okno.fill(BLACK, (0, 600, okno.get_width(), okno.get_height()//7))
    pygame.draw.rect(okno, col, (x, y, poj, wys))
    font = pygame.font.SysFont ('comicsans',12)
    okno.blit(font.render ('fuel', 1, (BLACK)), (x+5, y+3))
    pygame.display.update()
    petla+=1
    pygame.display.flip()
    clock.tick(40)
