import random
import pygame
from config import *
from assets import *


class Moto(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MOTO]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.assets = assets

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy



class Dog(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CACHORRO]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(0, 920)
        self.rect.y = 0
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(3, 10)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Resto a ver...
