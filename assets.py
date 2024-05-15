import pygame
import os
from config import MOTO_WIDTH, MOTO_HEIGHT, CARRO_WIDTH, CARRO_HEIGHT, IMG_DIR, SND_DIR, WIDTH, HEIGHT
from assets import *


BACKGROUND = 'background'
MOTO = 'moto_img'
B_RETA = 'b_reta_img'
B_RETA_E = 'b_reta_e_img'
B_RETA_D = 'b_reta_d_img'
B_DOIS_VE = 'b_dois_ve_img'
B_DOIS_VD = 'b_dois_vd_img'
B_DOIS_H = 'b_dois_h_img'
B_TRES = 'b_tres_img'

G_RETA = 'g_reta_img'
G_RETA_E = 'g_reta_e_img'
G_RETA_D = 'g_reta_d_img'
G_DOIS_VE = 'g_dois_ve_img'
G_DOIS_VD = 'g_dois_vd_img'
G_DOIS_H = 'g_dois_h_img'
G_TRES = 'g_tres_img'

'''
CARRO = 'carro_img'
GRAMA = 'grama_img'
ARVORE = 'arvore_img'
BUEIRO = 'bueiro_img'
CACHORRO = 'cachorro_img'
'''

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,"background.png")).convert() # Os backgrounds devem mudar conforme o jogador muda de tela
    assets[MOTO] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[MOTO] = pygame.transform.scale(assets['moto_img'], (MOTO_WIDTH, MOTO_HEIGHT))


    assets[B_RETA] = pygame.image.load(os.path.join(IMG_DIR, "b_reta.png")).convert()
    assets[B_RETA] = pygame.transform.scale(assets[B_RETA], (WIDTH, HEIGHT))

    assets[G_RETA] = pygame.image.load(os.path.join(IMG_DIR, "g_reta.png")).convert_alpha()
    assets[G_RETA] = pygame.transform.scale(assets[G_RETA], (WIDTH, HEIGHT))


    assets[B_RETA_E] = pygame.image.load(os.path.join(IMG_DIR, "b_reta_e.png")).convert()
    assets[B_RETA_E] = pygame.transform.scale(assets[B_RETA_E], (WIDTH, HEIGHT))

    assets[G_RETA_E] = pygame.image.load(os.path.join(IMG_DIR, "g_reta_e.png")).convert_alpha()
    assets[G_RETA_E] = pygame.transform.scale(assets[G_RETA_E], (WIDTH, HEIGHT))


    assets[B_RETA_D] = pygame.image.load(os.path.join(IMG_DIR, "b_reta_d.png")).convert()
    assets[B_RETA_D] = pygame.transform.scale(assets[B_RETA_D], (WIDTH, HEIGHT))

    assets[G_RETA_D] = pygame.image.load(os.path.join(IMG_DIR, "g_reta_d.png")).convert_alpha()
    assets[G_RETA_D] = pygame.transform.scale(assets[G_RETA_D], (WIDTH, HEIGHT))


    assets[B_DOIS_VE] = pygame.image.load(os.path.join(IMG_DIR, "b_dois_ve.png")).convert()
    assets[B_RETA_D] = pygame.transform.scale(assets[B_DOIS_VE], (WIDTH, HEIGHT))

    assets[G_DOIS_VE] = pygame.image.load(os.path.join(IMG_DIR, "g_reta_d.png")).convert_alpha()
    assets[G_DOIS_VE] = pygame.transform.scale(assets[G_DOIS_VE], (WIDTH, HEIGHT))


    assets[B_DOIS_VD] = pygame.image.load(os.path.join(IMG_DIR, "b_dois_vd.png")).convert()
    assets[B_DOIS_VD] = pygame.transform.scale(assets[B_DOIS_VD], (WIDTH, HEIGHT))

    assets[G_DOIS_VD] = pygame.image.load(os.path.join(IMG_DIR, "g_dois_vd.png")).convert_alpha()
    assets[G_DOIS_VD] = pygame.transform.scale(assets[G_DOIS_VD], (WIDTH, HEIGHT))

    assets[B_DOIS_H] = pygame.image.load(os.path.join(IMG_DIR, "b_dois_h.png")).convert()
    assets[B_DOIS_H] = pygame.transform.scale(assets[B_DOIS_H], (WIDTH, HEIGHT))

    assets[G_DOIS_H] = pygame.image.load(os.path.join(IMG_DIR, "g_dois_h.png")).convert_alpha()
    assets[G_DOIS_H] = pygame.transform.scale(assets[G_DOIS_H], (WIDTH, HEIGHT))

    assets[B_TRES] = pygame.image.load(os.path.join(IMG_DIR, "b_tres.png")).convert()
    assets[B_TRES] = pygame.transform.scale(assets[B_TRES], (WIDTH, HEIGHT))

    assets[G_TRES] = pygame.image.load(os.path.join(IMG_DIR, "g_tres.png")).convert_alpha()
    assets[G_TRES] = pygame.transform.scale(assets[G_TRES], (WIDTH, HEIGHT))
    
    
    '''
    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, "Arvore.png")).convert()
    assets[BUEIRO] = pygame.image.load(os.path.join(IMG_DIR, "Bueiro.png")).convert()
    assets[CACHORRO] = pygame.image.load(os.path.join(IMG_DIR, "Cachorro.png")).convert()
    assets[CARRO] = pygame.image.load(os.path.join())
    assets[CARRO] = pygame.transform.scale(assets['carro_img'], (CARRO_WIDTH, CARRO_HEIGHT))
    '''
    return assets