# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from game_loop import *
from assets import *

pygame.init()
pygame.mixer.init()

<<<<<<< Updated upstream
WIDTH = 920
HEIGHT = 920
=======
WIDTH = 900
HEIGHT = 900
>>>>>>> Stashed changes
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Motinha')

game = True

clock = pygame.time.Clock()

assets = load_assets

player = Moto(assets[MOTO])

# ======== Loop Principal ========
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
<<<<<<< Updated upstream
    
    assets = load_assets()
    window.fill(BLACK)  # Preenche com a cor branca
    window.blit(assets[BACKGROUND], (0, 0))
=======
        

    window.fill((255, 0, 0))
>>>>>>> Stashed changes

    pygame.display.update()


#game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

