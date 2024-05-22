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

class Informacao(pygame.sprite.Sprite):
    def __init__(self, assets, info, posicao):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[info]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicao
        


def info(assets, modulo, dicas):
    sorteadas = []
    infos = pygame.sprite.Group()

    posicoes = [CANTO_INFERIOR_E, CANTO_INFERIOR_D, CANTO_SUPERIOR]
    p_sort = []

    qtd = random.randint(1, 3)
    escolha = random.choice(dicas)

    posicao = random.choice(posicoes)
    p_sort.append(posicao)
    dica = Informacao(assets, escolha, posicao)
    infos.add(dica)
    
    for _ in range(qtd - 1):
        while escolha not in sorteadas:
            escolha = random.choice(dicas)
            sorteadas.append(escolha) 
        while posicao not in p_sort:
            posicao = random.choice(posicoes)
            p_sort.append(posicao)

        dica = Informacao(assets, escolha, posicao)
        infos.add(dica)  
        
    return infos
            
            


'''
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[CACHORRO]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(0, 920)
        self.rect.y = 0
        if self.rect.x == 0:
            self.speedx = random.randint(3, 5)
        else:
            self.speedx = random.randint(-5, -3)
        self.speedy = random.randint(3, 10)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, 920)
            self.rect.y = 0
            if self.rect.x == 0:
                self.speedx = random.randint(3, 5)
            else:
                self.speedx = random.randint(-5, -3)
            self.speedy = random.randint(3, 10)
'''