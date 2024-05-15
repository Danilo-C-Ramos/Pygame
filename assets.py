import pygame
import os
from config import MOTO_WIDTH, MOTO_HEIGHT, CARRO_WIDTH, CARRO_HEIGHT, IMG_DIR, SND_DIR
from assets import *


BACKGROUND = 'background'
MOTO = 'moto_img'
'''
CARRO = 'carro_img'
GRAMA = 'grama_img'
ARVORE = 'arvore_img'
BUEIRO = 'bueiro_img'
CACHORRO = 'cachorro_img'
'''

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,"Background.png")).convert() # Os backgrounds devem mudar conforme o jogador muda de tela
    assets[MOTO] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[MOTO] = pygame.transform.scale(assets['moto_img'], (MOTO_WIDTH, MOTO_HEIGHT))
    '''
    assets[GRAMA] = pygame.image.load(os.path.join(IMG_DIR, "Gramabkgrnd.png")).convert()
    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, "Arvore.png")).convert()
    assets[BUEIRO] = pygame.image.load(os.path.join(IMG_DIR, "Bueiro.png")).convert()
    assets[CACHORRO] = pygame.image.load(os.path.join(IMG_DIR, "Cachorro.png")).convert()
    assets[CARRO] = pygame.image.load(os.path.join())
    assets[CARRO] = pygame.transform.scale(assets['carro_img'], (CARRO_WIDTH, CARRO_HEIGHT))
    '''
    return assets