# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from game_loop import *
from assets import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Motinha')

game = True

clock = pygame.time.Clock()

assets = load_assets()

all_sprites = pygame.sprite.Group()
paredes = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['paredes'] = paredes

player = Moto(assets)
all_sprites.add(player)

states = [RETA, RETA_D, RETA_E]

tempo = 0
state_i = 0
state = states[state_i]
# ======== Loop Principal ========
while state != FIM:
    clock.tick(FPS)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = FIM
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.speedx -= 5
            if event.key == pygame.K_d:
                player.speedx += 5
            if event.key == pygame.K_w:
                player.speedy -= 5
            if event.key == pygame.K_s:
                player.speedy += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.speedx += 5
            if event.key == pygame.K_d:
                player.speedx -= 5
            if event.key == pygame.K_w:
                player.speedy += 5
            if event.key == pygame.K_s:
                player.speedy -= 5

    #bateu = pygame.sprite.spritecollide(player, obstaculo, True)
    #if bateu:



    if tempo % 100 == 0:
        paredes.empty()
        state_i = (state_i + 1) % len(states)
        state = states[state_i]
        g = Grama(assets, state)
        paredes.add(g)
        tempo = 0

    tempo += 1
    player.update()

    
    for parede in pygame.sprite.spritecollide(player, paredes, False, pygame.sprite.collide_mask):
        player.speedx = 0
        break
    #all_sprites.add(g)

    #window.fill(BLACK)  # Preenche com a cor preta
    #window.blit(assets[BACKGROUND], (0, 0))
    
    window.blit(assets[B_RETA], (0, 0))

    paredes.draw(window)
    all_sprites.draw(window)

    pygame.display.update()


#game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

