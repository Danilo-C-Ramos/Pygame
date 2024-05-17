# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from game_loop import *
from assets import *

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH + 100, HEIGHT + 100))
pygame.display.set_caption('Motinha')

game = True

clock = pygame.time.Clock()

assets = load_assets()

all_sprites = pygame.sprite.Group()
paredes = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['paredes'] = paredes

keys_down = {}

player = Moto(assets)
all_sprites.add(player)

state = RETA
g = Grama(assets, state)
paredes.add(g)
states = [DOIS_H, DOIS_VD, DOIS_VE, DOIS_H, TRES]
retas = [RETA, RETA, RETA, RETA, RETA, RETA_D, RETA_E]

vertices = [(0, 0), (0, 0), (0, HEIGHT), (0, HEIGHT)]

quadrado = pygame.draw.polygon(window, RED, vertices)

tempo = 0

# ======== Loop Principal ========
while state != FIM:
    clock.tick(FPS)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = FIM
        if event.type == pygame.KEYDOWN:
            keys_down[event.key] = True
            
            if event.key == pygame.K_a:
                player.image = assets[MOTO_ESQUERDA]
                player.speedx -= 5
            elif event.key == pygame.K_d:
                player.image = assets[MOTO_DIREITA]
                player.speedx += 5
            elif event.key == pygame.K_w:
                player.image = assets[MOTO]
                player.speedy -= 5
            elif event.key == pygame.K_s:
                player.image = assets[MOTO_TRAS]
                player.speedy += 5
        if event.type == pygame.KEYUP:
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_a and player.speedx < 0:
                    player.speedx += 5
                elif event.key == pygame.K_d and player.speedx > 0:
                    player.speedx -= 5
                elif event.key == pygame.K_w and player.speedy < 0:
                    player.speedy += 5
                elif event.key == pygame.K_s  and player.speedy > 0:
                    player.speedy -= 5

    #bateu = pygame.sprite.spritecollide(player, obstaculo, True)
    #if bateu:

    if player.rect.bottom > HEIGHT:
        player.speedy = 0
        player.rect.bottom = HEIGHT
        
    
    if (player.rect.bottom <= 0 or player.rect.left > WIDTH or player.rect.right < 0) and (state == RETA or state == RETA_E or state == RETA_D):
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        
        
        paredes.empty()
        #state_i = (state_i + 1) % len(states)
        #state = states[state_i]
        
        state = random.choice(states)
        print('TROCA')
        print(state)
        
        g = Grama(assets, state)
        paredes.add(g)
        tempo = 0 

    elif (player.rect.bottom <= 0 or player.rect.left > WIDTH or player.rect.right < 0) and state != RETA:
        
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        
        paredes.empty()
        #state_i = (state_i + 1) % len(states)
        #state = states[state_i]
        
        state = random.choice(retas)
        
        g = Grama(assets, state)
        paredes.add(g)
        
        tempo = 0


    player.update()

    
    for parede in pygame.sprite.spritecollide(player, paredes, False, pygame.sprite.collide_mask):

        #if player.rect.bottom <= HEIGHT/2 and event.key == pygame.K_s:
        #    player.speedy = 0
        #    player.rect.bottom -= 1
        if player.rect.bottom > HEIGHT/2:
            player.rect.bottom -= 1
            player.speedy = 0

        elif player.rect.top < HEIGHT/2:
            player.rect.top += 1
            player.speedy = 0

        
        if player.rect.left < WIDTH/2:
            print('a doida passou!')
            player.rect.left += 1
            player.speedx = 0
 
        elif player.rect.right > WIDTH/2:
            player.rect.right -= 1
            player.speedx = 0

        vertices = [(parede.rect.left, 0), (parede.rect.right, 0), (parede.rect.bottom, HEIGHT), (parede.rect.top, HEIGHT)]

        quadrado = pygame.draw.polygon(window, RED, vertices)

        


        '''
        if parede.rect.right >= player.rect.left:
            print('a doida passou!')
            player.rect.left += 1
            player.speedx = 0
            player.speedy = 0
            break
        
        elif parede.rect.left <= player.rect.right:
            player.rect.right -= 1
            player.speedx = 0
            player.speedy = 0
            break

        elif parede.rect.top >= player.rect.bottom:
            player.rect.top -= 1
            player.speedx = 0
            player.speedy = 0
            break

        elif parede.rect.bottom >= player.rect.top:
            player.rect.bottom += 1
            player.speedx = 0
            player.speedy = 0
            break
        '''
    #all_sprites.add(g)

    #window.fill(BLACK)  # Preenche com a cor preta
    #window.blit(assets[BACKGROUND], (0, 0))
    

    if state == 1:
        window.blit(assets[B_RETA], (0, 0))
    elif state == 2:
        window.blit(assets[B_RETA_E], (0, 0))
    elif state == 3:
        window.blit(assets[B_RETA_D], (0, 0))
    elif state == 4:
        window.blit(assets[B_DOIS_VE], (0, 0))
    elif state == 5:
        window.blit(assets[B_DOIS_VD], (0, 0))
    elif state == 6:
        window.blit(assets[B_DOIS_H], (0, 0))
    elif state == 7:
        window.blit(assets[B_TRES], (0, 0))
    
    
    tempo += 1
    if tempo == 60*300:
        state = FIM
    
    paredes.draw(window)
    all_sprites.draw(window)

    pygame.display.update()


#game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

