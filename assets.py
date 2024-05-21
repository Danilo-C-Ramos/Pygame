import pygame
import os
from config import *
from assets import *


BACKGROUND = 'background'
MOTO = 'moto_img'
MOTO_ESQUERDA = 'moto_esquerda_img'
MOTO_DIREITA = 'moto_direita_img'
MOTO_DIAGONAL_ESQUERDA = 'moto_diagonal_esquerda_img'
MOTO_DIAGONAL_ESQUERDA_BAIXO = 'moto_diagonal_esquerda_baixo_img'
MOTO_DIAGONAL_SUDESTE = 'moto_diagonal_sudeste_img'
MOTO_DIAGONAL_DIREITA = 'moto_diagonal_direita_img'
MOTO_TRAS = 'moto_tras_img'

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

CARRO = 'carro_img'
GRAMA = 'grama_img'
ARVORE = 'arvore_img'
BUEIRO = 'bueiro_img'
CARAMELO = 'caramelo_img'
PLACA_DE_PARE = 'placa_de_pare_img'
HIDRANTE = 'hidrante_img'
PARE = 'placa_pare_img'
JOIA = 'joia_img'
PROIBIDO = 'placa_proibido_img'
RETO = 'placa_reto_img'
ANIMAL = 'placa_animal_img'
POLICIA = 'policia_img'
BUEIRO = 'bueiro_img'
OUTDOOR_INSPER = 'outdoor_insper_img'
OUTDOOR_ESPM = 'outdoor_espm_img'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,"background.png")).convert() # Os backgrounds devem mudar conforme o jogador muda de tela
    assets[MOTO] = pygame.image.load(os.path.join(IMG_DIR, 'moto.png')).convert_alpha()
    assets[MOTO] = pygame.transform.scale(assets['moto_img'], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_TRAS] = pygame.image.load(os.path.join(IMG_DIR, 'moto_tras.png')).convert_alpha()
    assets[MOTO_TRAS] = pygame.transform.scale(assets[MOTO_TRAS], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIREITA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_direita.png')).convert_alpha()
    assets[MOTO_DIREITA] = pygame.transform.scale(assets[MOTO_DIREITA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_ESQUERDA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_esquerda.png')).convert_alpha()
    assets[MOTO_ESQUERDA] = pygame.transform.scale(assets[MOTO_ESQUERDA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_DIREITA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_direita.png')).convert_alpha()
    assets[MOTO_DIAGONAL_DIREITA] = pygame.transform.scale(assets[MOTO_DIAGONAL_DIREITA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_ESQUERDA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_esquerda.png')).convert_alpha()
    assets[MOTO_DIAGONAL_ESQUERDA] = pygame.transform.scale(assets[MOTO_DIAGONAL_ESQUERDA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_SUDESTE] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_sudeste.png')).convert_alpha()
    assets[MOTO_DIAGONAL_SUDESTE] = pygame.transform.scale(assets[MOTO_DIAGONAL_SUDESTE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_ESQUERDA_BAIXO] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_esquerda_baixo.png')).convert_alpha()
    assets[MOTO_DIAGONAL_ESQUERDA_BAIXO] = pygame.transform.scale(assets[MOTO_DIAGONAL_ESQUERDA_BAIXO], (MOTO_WIDTH, MOTO_HEIGHT))

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
    assets[B_DOIS_VE] = pygame.transform.scale(assets[B_DOIS_VE], (WIDTH, HEIGHT))

    assets[G_DOIS_VE] = pygame.image.load(os.path.join(IMG_DIR, "g_dois_ve.png")).convert_alpha()
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
    
    
    assets[HIDRANTE] = pygame.image.load(os.path.join(IMG_DIR, 'hidrante.png')).convert_alpha()
    assets[HIDRANTE] = pygame.transform.scale(assets[HIDRANTE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[PARE] = pygame.image.load(os.path.join(IMG_DIR, 'pare.png')).convert_alpha()
    assets[PARE] = pygame.transform.scale(assets[PARE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[PARE] = pygame.image.load(os.path.join(IMG_DIR, 'pare.png')).convert_alpha()
    assets[PARE] = pygame.transform.scale(assets[PARE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[PROIBIDO] = pygame.image.load(os.path.join(IMG_DIR, 'proibido.png')).convert_alpha()
    assets[PROIBIDO] = pygame.transform.scale(assets[PROIBIDO], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[ANIMAL] = pygame.image.load(os.path.join(IMG_DIR, 'animal.png')).convert_alpha()
    assets[ANIMAL] = pygame.transform.scale(assets[ANIMAL], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[POLICIA] = pygame.image.load(os.path.join(IMG_DIR, 'policia.png')).convert_alpha()
    assets[POLICIA] = pygame.transform.scale(assets[POLICIA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[BUEIRO] = pygame.image.load(os.path.join(IMG_DIR, 'bueiro.png')).convert_alpha()
    assets[BUEIRO] = pygame.transform.scale(assets[BUEIRO], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[CARAMELO] = pygame.image.load(os.path.join(IMG_DIR, 'caramelo.png')).convert_alpha()
    assets[CARAMELO] = pygame.transform.scale(assets[CARAMELO], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, 'arvore.png')).convert_alpha()
    assets[ARVORE] = pygame.transform.scale(assets[ARVORE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[JOIA] = pygame.image.load(os.path.join(IMG_DIR, 'joia.png')).convert_alpha()
    assets[JOIA] = pygame.transform.scale(assets[JOIA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[OUTDOOR_INSPER] = pygame.image.load(os.path.join(IMG_DIR, 'outdoor_insper.png')).convert_alpha()
    assets[OUTDOOR_INSPER] = pygame.transform.scale(assets[OUTDOOR_INSPER], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[OUTDOOR_ESPM] = pygame.image.load(os.path.join(IMG_DIR, 'outdoor_espm.png')).convert_alpha()
    assets[OUTDOOR_ESPM] = pygame.transform.scale(assets[OUTDOOR_ESPM], (MOTO_WIDTH, MOTO_HEIGHT))


    '''
    assets[ARVORE] = pygame.image.load(os.path.join(IMG_DIR, "Arvore.png")).convert()
    assets[BUEIRO] = pygame.image.load(os.path.join(IMG_DIR, "Bueiro.png")).convert()
    assets[CACHORRO] = pygame.image.load(os.path.join(IMG_DIR, "Cachorro.png")).convert()
    assets[CARRO] = pygame.image.load(os.path.join())
    assets[CARRO] = pygame.transform.scale(assets['carro_img'], (CARRO_WIDTH, CARRO_HEIGHT))
    
    #figuras de teste
    assets[PLACA_DE_PARE]=pygame.draw.rect(RED, 10, 10)
    assets[ARVORE]=pygame.draw.rect(GREEN, 10, 10)
    assets[BUEIRO]=pygame.draw.rect(BLACK, 10, 10)
    assets[CACHORRO]=pygame.draw.rect(WHITE, 10, 10)
    assets[CARRO]=pygame.draw.rect(YELLOW, 10, 10)
    '''
    
    return assets


#figuras de teste

