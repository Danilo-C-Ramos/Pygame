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
pygame.display.set_caption('Motinha')

game = True

clock = pygame.time.Clock()

assets = load_assets()

all_sprites = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites

player = Moto(assets)
all_sprites.add(player)

# ======== Loop Principal ========
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 5
            if event.key == pygame.K_RIGHT:
                player.speedx += 5
            if event.key == pygame.K_UP:
                player.speedy -= 5
            if event.key == pygame.K_DOWN:
                player.speedy += 5
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 5
            if event.key == pygame.K_RIGHT:
                player.speedx -= 5
            if event.key == pygame.K_UP:
                player.speedy += 5
            if event.key == pygame.K_DOWN:
                player.speedy -= 5


    player.update()

    window.fill(BLACK)  # Preenche com a cor branca
    window.blit(assets[BACKGROUND], (0, 0))
    all_sprites.draw(window)

    pygame.display.update()


#game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

