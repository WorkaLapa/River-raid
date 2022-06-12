import pygame
import random
from PLAYERklasa import *

pygame.init()
okno=pygame.display.set_mode((900,600))
pygame.display.set_caption("River raid")
clock=pygame.time.Clock()
bok = 50*(random.randint(1,8))

###LISTA SPRITÓW TO LISTA WSZYSTKICH OBIEKTÓW RUSZAJĄCYCH SIĘ
###PONIŻSZE LINIJKI KODU TWORZĄ CZTERY LISTY
lista_spritow= pygame.sprite.Group()
lista_paliwa= pygame.sprite.Group()
lista_przeciwnikow=pygame.sprite.Group()
strzelanie=pygame.sprite.Group()
###TWORZENIE GRACZA
gracz=Samolot()
gracz.rect.x=450 ###UMIESZCZENIE W POZIOMIE NA MAPIE
gracz.rect.y=550 ###UMIESZCZENIE W PIONIE NA MAPIE
predkosc_samolotu=2
lista_spritow.add(gracz)

paliwo=Paliwo()
paliwo.rect.x=random.randint(50,800)
paliwo.rect.y=random.randint(50,500)
lista_spritow.add(paliwo)
lista_paliwa.add(paliwo)

tankowiec=Tankowiec()
tankowiec.rect.x=random.randint(50,800)
tankowiec.rect.y=random.randint(50,550)
lista_spritow.add(tankowiec)
lista_przeciwnikow.add(tankowiec)

helikopter=Helikopter()
helikopter.rect.x=random.randint(50,800)
helikopter.rect.y=random.randint(50,550)
lista_spritow.add(helikopter)
lista_przeciwnikow.add(helikopter)








trwanie_gry=True
while trwanie_gry:
    for event in pygame.event.get():
        pygame.time.delay(10)
        if event.type == pygame.QUIT:
            trwanie_gry = False

        ##PĘTLA WYŁĄCZA GRĘ W RAZIE KOLIZJI Z PALIWEM - DO ZMIANY
    lista_kolizji_z_paliwem = pygame.sprite.spritecollide(gracz,lista_paliwa, False)
    for obiekt in lista_kolizji_z_paliwem:
        trwanie_gry=False
        lista_spritow.update()
    ##PĘTLA WYŁĄCZA GRĘ W RAZIE KOLIZJI Z PRZECIWNIKAMI
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
