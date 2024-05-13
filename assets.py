import pygame
import os
from config import MOTO_WIDTH, MOTO_HEIGHT, CARRO_WIDTH, CARRO_HEIGHT, IMG_DIR, SND_DIR


BACKGROUND = 'background'
MOTO = 'moto_img'
CARRO = 'carro_img'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join("IMAGEM DOS CAMINHOS")).convert_alpha # Os backgrounds devem mudar conforme o jogador muda de tela
    assets[MOTO] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[MOTO] = pygame.transform.scale(assets['moto_img'], (MOTO_WIDTH, MOTO_HEIGHT))
    assets[CARRO] = pygame.image.load(os.path.join())
    assets[CARRO] = pygame.transform.scale(assets['carro_img'], (CARRO_WIDTH, CARRO_HEIGHT))


    return assets