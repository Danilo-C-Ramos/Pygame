import random
import pygame
from config import *
from assets import *


class Moto(pygame.sprite.Sprite):
    def __init__(self, assets):
        self.image = assets[MOTO]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
    
    def update(self):
        # Atualização da posição da moto
        self.rect.x += self.speedx