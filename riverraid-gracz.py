import pygame
pygame.init()

####POKAZUJE OKNO GRY
okno_gry = pygame.display.set_mode((900, 600))
# POKAZJUJE NAZWĘ GRY W PASKU NA GÓRZE
pygame.display.set_caption("River raid")
###WYPEŁNIA OKNO GRY KOLOREM


#POKAZUJE, GDZIE DOCELOWO ZNAJDUJE SIĘ SAMOLOT NA MAPIE
x = 100
y = 550

# dimensions of the object
szerokosc_obiektu = 10
wysokosc_obiektu = 20

# wgrana prędkość samolotu w ruchu lewo-prawo
predkosc_samolotu = 7

# Pokazuje, że gra jest uruchomiona
trwanie_gry = True


# pętla
while trwanie_gry:
    # NIE WIEM< CO TO ROBI< CHYBA DO USUNIĘCIA
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
    if przyciski[pygame.K_RIGHT] and x<500-szerokosc_obiektu:
        x += predkosc_samolotu
###KOLORUJE OKNO GRY NA CZARNO I ROBI PROSTOKĄT_GRACZA
    okno_gry.fill((0, 0, 0))
    pygame.draw.rect(okno_gry, (255, 223, 0), (x, y, szerokosc_obiektu, wysokosc_obiektu))

    # it refreshes the window ##NIE WIEM< PO CO
    pygame.display.update()

# closes the pygame window
pygame.quit()
