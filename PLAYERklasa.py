import pygame
import sys
import os

class Samolot(pygame.sprite.Sprite):

    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        img=pygame.image.load(os.path.join('samolot.png')).convert()
        self.images.append(img)
        self.image=self.images[0]
        self.rect=self.image.get_rect()

class Paliwo(pygame.sprite.Sprite):

    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        img=pygame.image.load(os.path.join('paliwo.png')).convert()
        self.images.append(img)
        self.image=self.images[0]
        self.rect=self.image.get_rect()

class Tankowiec(pygame.sprite.Sprite):

    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        img=pygame.image.load(os.path.join('tankowiec.png')).convert()
        self.images.append(img)
        self.image=self.images[0]
        self.rect=self.image.get_rect()

class Helikopter(pygame.sprite.Sprite):

    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        img=pygame.image.load(os.path.join('helikopter.png')).convert()
        self.images.append(img)
        self.image=self.images[0]
        self.rect=self.image.get_rect()

class Kula(pygame.sprite.Sprite):

    def __init__(self, szerokosc, wysokosc):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        img=pygame.image.load(os.path.join('kula.png')).convert()
        self.images.append(img)
        self.image=self.images[0]
        self.rect=self.image.get_rect()
