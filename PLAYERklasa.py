import pygame


class Samolot(pygame.sprite.Sprite):
    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        img=pygame.image.load(os.path.join('samolot.png')).convert()
        self.image=img
        self.rect=self.image.get_rect()
        self.strzal=pygame.time.get_ticks()
    def ruch(self):
        predkosc=6
        kiedy_zniknie=150
        czas = pygame.time.get_ticks()
        przyciski = pygame.key.get_pressed()
        if przyciski[pygame.K_LEFT] and gracz.rect.x>0:
            gracz.rect.x -= predkosc_samolotu
        if przyciski[pygame.K_RIGHT] and gracz.rect.x<845:
            gracz.rect.x += predkosc_samolotu
        if przyciski[pygame.K_SPACE] and czas-self.strzal>kiedy_zniknie:
            kula=Pocisk(self.rect.centerx, self.rect.top)
            strzelanie.add(kula)
            self.strzal=czas
            
class Pocisk(pygame.sprite.Sprite):
    def __init__(self,szerokosc,wysokosc):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("kula.png")
        self.rect=self.image.get_rect()
        self.rect.center=[szerokosc,wysokosc]
    def update(self):
        self.rect.y-=5
        if self.rect.bottom<0:
            self.kill()


class Paliwo(pygame.sprite.Sprite):
    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        img=pygame.image.load(os.path.join('paliwo.png')).convert()
        self.image=img
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y+=3
        if pygame.sprite.spritecollide(self, strzelanie,False):
            self.kill()

class Tankowiec(pygame.sprite.Sprite):
    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        img=pygame.image.load(os.path.join('tankowiec.png')).convert()
        self.image=img
        self.rect=self.image.get_rect()
    def update(self):
        if pygame.sprite.spritecollide(self, strzelanie,False):
            self.kill()

class Helikopter(pygame.sprite.Sprite):

    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        img=pygame.image.load(os.path.join('helikopter.png')).convert()
        self.image=img
        self.rect=self.image.get_rect()
    def update(self):
        if pygame.sprite.spritecollide(self, strzelanie,False):
            self.kill()
