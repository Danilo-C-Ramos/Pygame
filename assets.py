import pygame
import os


MOTO = 'moto'

def load_assets():
    assets = {}
    assets[MOTO] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[MOTO] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    return assets