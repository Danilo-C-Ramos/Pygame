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

class Entrega(pygame.sprite.Sprite):
    def __init__(self, assets, info, posicao):
         
        self.image = assets[info]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicao
        


def info(assets, modulo, dicas, n, mapa, m_anterior):
    sorteadas = []
    infos = pygame.sprite.Group()

    p_sort = []
    qtd = random.randint(2, 5)
   

    escolha = random.choice(dicas)
    posicao = random.choice(POSICOES)
    
    p_sort.append(posicao)
    sorteadas.append(escolha)
    
    
    dica = Informacao(assets, escolha, posicao)
    infos.add(dica)

    for _ in range(qtd - 1):
        escolha = random.choice(dicas)
        posicao = random.choice(POSICOES)

        while escolha in sorteadas:
           
            escolha = random.choice(dicas)
        
        while posicao in p_sort:
            posicao = random.choice(POSICOES)
        
        p_sort.append(posicao)
        sorteadas.append(escolha)
       
        dica = Informacao(assets, escolha, posicao)
        infos.add(dica)  
        
        if m_anterior == RETA:
            if n == 0:
                if modulo == OUTDOOR_ESPM:
                    if PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                        certa = ESQUERDA
                    elif ARVORE in sorteadas and PLACA_ANIMAL in sorteadas and mapa in P_DIREITA:
                        certa = DIREITA
                    elif mapa in P_RETO:
                        certa = RETO
                    else:
                        certa = DIREITA
                if modulo == OUTDOOR_INSPER:
                    if mapa in P_RETO:
                        certa = RETO
                    elif mapa in P_ESQUERDA:
                        certa = ESQUERDA
                    else:
                        certa = RETO



                if modulo == POLICIA:
                    if ARVORE in sorteadas and BUEIRO in sorteadas and mapa in P_ESQUERDA:
                        certa = ESQUERDA
                    elif CARAMELO in sorteadas and HIDRANTE in sorteadas and mapa in P_RETO:
                        certa = RETO
                    elif mapa in P_DIREITA:
                        certa = DIREITA
                    else:
                        certa = RETO

                if modulo == CAVALO:
                    if CARAMELO in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                        certa = ESQUERDA
                    elif CARRO_ESTACIONADO in sorteadas and ARVORE in sorteadas and mapa in P_RETO:
                        certa = RETO
                    elif mapa in P_DIREITA:
                        certa = DIREITA
                    else:
                        certa = RETO

                if modulo == CASA:
                    if CARAMELO in sorteadas and BUEIRO in sorteadas and mapa in P_DIREITA:
                        certa = DIREITA
                    elif PLACA_PROIBIDO in sorteadas and HIDRANTE in sorteadas and mapa in P_RETO:
                        certa = RETO
                    elif mapa in P_ESQUERDA:
                        certa = ESQUERDA
                    else:
                        certa = DIREITA

        if m_anterior == RETA_D:
            if n == 0:

                if modulo == OUTDOOR_INSPER:
                    if mapa in P_RETO:
                        certa = RETO
                    elif ARVORE in sorteadas and JOIA in sorteadas and mapa in P_DIREITA:
                        certa = DIREITA
                    elif mapa in P_ESQUERDA:
                        certa = ESQUERDA
                    else:
                        certa = RETO
            
    '''
    elif n == 1:
        if modulo == OUTDOOR_ESPM or modulo == OUTDOOR_INSPER:
            if PLACA_DE_PARE in sorteadas and ARVORE in sorteadas and mapa in P_RETO:
                certa = RETO
            elif CARRO_ESTACIONADO in sorteadas and BUEIRO in sorteadas and mapa in P_DIREITA:
                certa = DIREITA
            else:
                certa = ESQUERDA
    
        if modulo == POLICIA:
            if CARRO_ESTACIONADO in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_DIREITA:
                certa = DIREITA
            elif CARAMELO in sorteadas and JOIA in sorteadas and mapa in P_RETO:
                certa = RETO
            else:
                certa = ESQUERDA

        if modulo == CASA:
            if CARRO_ESTACIONADO in sorteadas and IDOSO in sorteadas and mapa in P_RETO:
                certa = RETO
            elif BUEIRO in sorteadas and ARVORE in sorteadas and mapa in P_DIREITA:
                certa = DIREITA
            else:
                certa = ESQUERDA

        if modulo == CAVALO:
            if CARAMELO in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                certa = ESQUERDA
            elif CARRO_ESTACIONADO in sorteadas and ARVORE in sorteadas and mapa in P_RETO:
                certa = RETO
            else:
                certa = DIREITA

    elif n == 2:
        if modulo == OUTDOOR_ESPM:
            if PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                certa = ESQUERDA
            elif ARVORE in sorteadas and PLACA_ANIMAL in sorteadas and mapa in P_DIREITA:
                certa = DIREITA
            else:
                certa = RETO
        if modulo == OUTDOOR_INSPER:
            if mapa in P_RETO:
                certa = RETO
            else:
                certa = ESQUERDA


        if modulo == POLICIA:
            if CARRO_ESTACIONADO in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_DIREITA:
                certa = DIREITA
            elif CARAMELO in sorteadas and JOIA in sorteadas and mapa in P_RETO:
                certa = RETO
            else:
                certa = ESQUERDA

    
        if modulo == CASA:
            if CARRO_ESTACIONADO in sorteadas and IDOSO in sorteadas and mapa in P_RETO:
                certa = RETO
            elif BUEIRO in sorteadas and ARVORE in sorteadas and mapa in P_DIREITA:
                certa = DIREITA
            else:
                certa = ESQUERDA

        if modulo == CAVALO:
            if CARAMELO in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                certa = ESQUERDA
            elif CARRO_ESTACIONADO in sorteadas and ARVORE in sorteadas and mapa in P_RETO:
                certa = RETO
            else:
                certa = DIREITA
        '''
    
    return infos, certa