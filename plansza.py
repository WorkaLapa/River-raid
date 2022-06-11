import pygame
import random
import sys
import os
from PLAYERklasa import *

pygame.init()
okno=pygame.display.set_mode((900,600))
pygame.display.set_caption("River raid")
clock=pygame.time.Clock()
bok = 50*(random.randint(1,8))

###LISTA SPRITÓW TO LISTA WSZYSTKICH OBIEKTÓW RUSZAJĄCYCH SIĘ
###PONIŻSZE LINIJKI KODU TWORZĄ TRZY LISTY
lista_spritow= pygame.sprite.Group()
lista_paliwa= pygame.sprite.Group()
lista_przeciwnikow=pygame.sprite.Group()
gracz=Samolot(15,35)
gracz.rect.x=100
gracz.rect.y=550
predkosc_samolotu=2
lista_spritow.add(gracz)

paliwo=Paliwo(5,20)
paliwo.rect.x=random.randint(50,800)
paliwo.rect.y=550
lista_spritow.add(paliwo)
lista_paliwa.add(paliwo)

tankowiec=Tankowiec(5,20)
paliwo.rect.x=random.randint(50,800)
paliwo.rect.y=random.randint(50,550)
lista_spritow.add(tankowiec)
lista_przeciwnikow.add(tankowiec)

helikopter=Helikopter(5,20)
paliwo.rect.x=random.randint(50,800)
paliwo.rect.y=random.randint(50,550)
lista_spritow.add(helikopter)
lista_przeciwnikow.add(helikopter)








trwanie_gry=True
while trwanie_gry:
    for event in pygame.event.get():
        pygame.time.delay(10)
        if event.type == pygame.QUIT:
            trwanie_gry = False
        ###KOORDYNUJE PRZYCISKI
    przyciski = pygame.key.get_pressed()

        ##WCIŚNIĘCIE LEWEGO PRZYCISKU
    if przyciski[pygame.K_LEFT] and gracz.rect.x>0:
        gracz.rect.x -= predkosc_samolotu
        ##I PRAWEGO
    if przyciski[pygame.K_RIGHT] and gracz.rect.x<845:
        gracz.rect.x += predkosc_samolotu

        ##PĘTLA WYŁĄCZA GRĘ W RAZIE KOLIZJI Z PALIWEM - DO ZMIANY
    lista_kolizji_z_paliwem = pygame.sprite.spritecollide(gracz,lista_paliwa, False)
    for obiekt in lista_kolizji_z_paliwem:
        trwanie_gry=False
        lista_spritow.update()
    ##PĘTLA WYŁĄCZA GRĘ W RAZIE KOLIZJI Z PALIWEM - DO ZMIANY
    lista_kolizji_z_przeciwnikami = pygame.sprite.spritecollide(gracz,lista_przeciwnikow, False)
    for obiekt in lista_kolizji_z_przeciwnikami:
        trwanie_gry=False
        lista_spritow.update()
        lista_przeciwnikow.update()

    okno.fill((0,0,255))
    pygame.draw.rect(okno, (0, 255, 0), (0, 0, bok, 600))
    pygame.draw.rect(okno, (0, 255, 0), (900-bok, 0, 900, 600))
    lista_spritow.draw(okno)
    pygame.display.update()
    pygame.display.flip()


pygame.display.update()
clock.tick(15)
