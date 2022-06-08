import pygame
import random
from PLAYERklasa import Samolot
pygame.init()
###KOLORY
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
predkosc_samolotu=7
####POKAZUJE OKNO GRY
okno_gry = pygame.display.set_mode((900, 600))
# POKAZJUJE NAZWĘ GRY W PASKU NA GÓRZE
pygame.display.set_caption("River raid")

lista_spritow=pygame.sprite.Group()
samolotGracza=Samolot()
samolotGracza.rect.x=100
samolotGracza.rect.y= 550
tankowiec = Samolot(PURPLE, 60, 80, random.randint(50,100))
tankowiec.rect.x = 60
tankowiec.rect.y = -100

lista_spritow.add(samolotGracza)
lista_spritow.add(tankowiec)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(tankowiec)
###WYPEŁNIA OKNO GRY KOLOREM
trwanie_gry = True
clock=pygame.time.Clock()
# pętla
while trwanie_gry:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            trwanie_gry = False
###KOORDYNUJE PRZYCISKI
    przyciski = pygame.key.get_pressed()

##WCIŚNIĘCIE LEWEGO PRZYCISKU
    if przyciski[pygame.K_LEFT] and x>0:
        x -= predkosc_samolotu
##I PRAWEGO
    if przyciski[pygame.K_RIGHT] and x<900-szerokosc_obiektu:
        x += predkosc_samolotu
###KOLORUJE OKNO GRY NA CZARNO I ROBI PROSTOKĄT_GRACZA

        #Game Logic
    for obiekt in all_coming_cars:
        obiekt.moveForward(speed)
        if obiekt.rect.y > SCREENHEIGHT:
            obiekt.changeSpeed(random.randint(50,100))
            obiekt.repaint(RED)
            obiekt.rect.y = -200
#Check if there is a car collision
        kolizja = pygame.sprite.spritecollide(samolotGracza,all_coming_cars,False)
        for obiekt in kolizja:
            print("Koniec gry")
        #End Of Game
            carryOn=False
            lista_spritow.update()

            screen.fill(GREEN)
    # okno_gry.fill((0, 0, 0))
    # pygame.draw.rect(okno_gry, (255, 223, 0), (x, y, szerokosc_obiektu, wysokosc_obiektu))

    # it refreshes the window ##NIE WIEM< PO CO
    # pygame.display.update()
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()
