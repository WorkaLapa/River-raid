import pygame
import sys 
import random 

#OKNO
pygame.init()
okno = pygame.display.set_mode((900, 600))
pygame.display.set_caption("River raid")
clock=pygame.time.Clock()
bok = 50*(random.randint(1,8))

#LISTA SPRITÓW
lista_spritow= pygame.sprite.Group()
lista_paliwa= pygame.sprite.Group()
lista_przeciwnikow=pygame.sprite.Group()
strzelanie=pygame.sprite.Group()
lista_kolizji_z_paliwem=pygame.sprite.Group()
lista_kolizji_z_przeciwnikami=pygame.sprite.Group()

obiekt=object

#ZMIENNE KOLORÓW ORAZ WYMIATY PASKA PALIWA
BLACK = (0, 0, 0)
GREEN = (0, 225, 0)
YELLOW = (225, 225, 0)
RED = (225, 0, 0)
x = 10
y = 30
wys = 25

#PĘTLA DZIAŁANIA GRY
trwanie_gry=True
while trwanie_gry:
    for event in pygame.event.get():
        pygame.time.delay(10)
        if event.type == pygame.QUIT:
            trwanie_gry = False
          
#PĘTLA ZURZYCIA PALIWA I JEGO DOŁADOWYWANIA
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
