import pygame
import random
from PLAYERklasa import*


pygame.init()
okno=pygame.display.set_mode(size=(900,600))
clock=pygame.time.Clock()
lvl_speed=3
bok = 50*(random.randint(1,8))
lap=1
lvl_length=1000*50

lista_spritow= pygame.sprite.Group()
lista_paliwa= pygame.sprite.Group()
lista_przeciwnikow=pygame.sprite.Group()
strzelanie=pygame.sprite.Group()
lista_kolizji_z_paliwem=pygame.sprite.Group()
lista_kolizji_z_przeciwnikami=pygame.sprite.Group()
#ZMIENNE KOLORÓW ORAZ WYMIATY PASKA PALIWA
BLACK = (0, 0, 0)
GREEN = (0, 225, 0)
YELLOW = (225, 225, 0)
RED = (225, 0, 0)
x = 10
y = 30
wys = 25

umieszczenie_poziom = 100
umieszczenie_pion = 550
szerokosc_obiektu = 15
wysokosc_obiektu = 35
predkosc_samolotu = 7

zbiornik=pygame.image.load("paliwo.png")
enemy1=pygame.image.load("tankowiec.png")
enemy2=pygame.image.load("helikopter.png")

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
    okno.fill((0, 0, 255))
    samolot=pygame.draw.rect(okno, (255, 223, 0), (umieszczenie_poziom, umieszczenie_pion, szerokosc_obiektu, wysokosc_obiektu))

    for block in blocks:
        block.move_ip(0, lvl_speed)
    for enemy in wrog:
        enemy.move_ip(0, lvl_speed)
    for zbiornik in fuel:
        zbiornik.move_ip(0, lvl_speed)


    okno.blit(enemy1, (0,0))
    okno.blit(enemy2,(0,0))
    okno.blit(zbiornik,(0,0))

    for block in blocks:
        pygame.draw.rect(okno, (0, 255, 0), block)
        if block.colliderect(samolot):
            trwanie_gry=False
    for enemy in wrog:
        if enemy.colliderect(samolot):
            trwanie_gry=False
    for zbiornik in fuel:
        if zbiornik.colliderect(samolot):
            while True:
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 300, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 290, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 280, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 270, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 260, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 250, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 240, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 230, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 220, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 210, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 200, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 190, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 180, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 170, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 160, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 150, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 140, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 130, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 120, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                    pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 110, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 100, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 90, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 80, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 70, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 60, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 50, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 40, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 30, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 20, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, GREEN, (x, y, 10, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                if obiekt in lista_kolizji_z_paliwem:
                    break
                for i in range(500):
                    okno.fill(BLACK)
                    pygame.draw.rect(okno, RED, (x, y, 10, wys))
                    font = pygame.font.SysFont ('comicsans',12)
                    okno.blit(font.render ('fuel', 1, (BLACK)), (15, 33))
                pygame.display.update()
                sys.exit()
    #     pygame.draw.rect(okno, (160, 32, 50), zbiornik)

    pygame.display.flip()
    clock.tick(40)
