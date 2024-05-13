# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from game_loop import *
from assets import *

pygame.init()
pygame.mixer.init()

WIDTH = 920
HEIGHT = 920
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Motinha')

game = True

# ======== Loop Principal ========
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    assets = load_assets()
    window.fill(BLACK)  # Preenche com a cor branca
    window.blit(assets[BACKGROUND], (0, 0))

    pygame.display.update()


#game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

