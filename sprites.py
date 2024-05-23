import random
import pygame
from config import *
from assets import *

#classe para criar a moto do jogador
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

#classe para criar as paredes/gramas da tela em questão 
class Grama(pygame.sprite.Sprite):
    def __init__(self, assets, state):
        pygame.sprite.Sprite.__init__(self)

        if state == 1:
            self.image = assets[G_RETA]
        elif state == 2:
            self.image = assets[G_RETA_E]
        elif state == 3:
            self.image = assets[G_RETA_D]
        elif state == 4:
            self.image = assets[G_DOIS_VE]
        elif state == 5:
            self.image = assets[G_DOIS_VD]
        elif state == 6:
            self.image = assets[G_DOIS_H]
        elif state == 7:
            self.image = assets[G_TRES]
    
    
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

#classe para criar um sprite das informações da tela
class Informacao(pygame.sprite.Sprite):
    def __init__(self, assets, info, posicao):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[info]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicao


#class Entrega(pygame.sprite.Sprite):
#    def __init__(self, assets, info, posicao):
#        self.image = assets[info]
#        self.mask = pygame.mask.from_surface(self.image)
#        self.rect = self.image.get_rect()
#        self.rect.center = posicao