# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from game_loop import *
from assets import *
import time

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Motinha')

game = True

clock = pygame.time.Clock()

assets = load_assets()

font = pygame.font.SysFont(None, 55)

state = init_screen(window, assets)




all_sprites = pygame.sprite.Group()
paredes = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['paredes'] = paredes

keys_down = {}

player = Moto(assets)
all_sprites.add(player)


g = Grama(assets, state)
paredes.add(g)
states = [DOIS_H, DOIS_VD, DOIS_VE, DOIS_H, TRES]
retas = [RETA, RETA, RETA, RETA, RETA, RETA_D, RETA_E]

dicas= [HIDRANTE, RETO, PROIBIDO, ANIMAL, CARAMELO, ARVORE]
modulos= [OUTDOOR_INSPER, OUTDOOR_ESPM, POLICIA]
modulo= 0


#vertices = [(0, 0), (0, 0), (0, HEIGHT), (0, HEIGHT)]

#quadrado = pygame.draw.polygon(window, RED, vertices)

tempo = 0

# ======== Loop Principal ========
while state != FIM:
    clock.tick(FPS)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = FIM
        if event.type == pygame.KEYDOWN:
            keys_down[event.key] = True
            
            #if event.key == pygame.K_w and event.key == pygame.K_a:
                #player.speedx = -3.53
                #player.speedy = -3.53
                #player.image = assets[MOTO_DIAGONAL_ESQUERDA]
            if event.key == pygame.K_w:
                player.image = assets[MOTO]
                player.speedy -= 5
            elif event.key == pygame.K_a:
                player.image = assets[MOTO_ESQUERDA]
                player.speedx -= 5
            elif event.key == pygame.K_d:
                player.image = assets[MOTO_DIREITA]
                player.speedx += 5
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

    if player.speedy == -5:
        player.image = assets[MOTO]
    
    if player.rect.bottom > HEIGHT:
        player.speedy = 0
        player.rect.bottom = HEIGHT
        
    
    if (player.rect.bottom <= 0 or player.rect.left > WIDTH or player.rect.right < 0) and (state == RETA or state == RETA_E or state == RETA_D):
        
        
        time.sleep(0.25)
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        player.speedx=0

        paredes.empty()
        #state_i = (state_i + 1) % len(states)
        #state = states[state_i]

        state = random.choice(states)
        print('TROCA')
        print(state)
        modulo = random.choice(modulos)
      
        g = Grama(assets, state)
        paredes.add(g)

    elif (player.rect.bottom <= 0 or player.rect.left > WIDTH or player.rect.right < 0) and state != RETA:
        
        time.sleep(0.25)
        player.speedx= 0
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        
        paredes.empty()
        #state_i = (state_i + 1) % len(states)
        #state = states[state_i]
        
        state = random.choice(retas)
        
        g = Grama(assets, state)
        paredes.add(g)
        
    player.update()

    
    for parede in pygame.sprite.spritecollide(player, paredes, False, pygame.sprite.collide_mask):
        
        if player.rect.bottom > HEIGHT:
            player.speedy = 0
            player.rect.bottom = HEIGHT

        elif player.rect.top <= 0:
            player.speedy = 0
            player.rect.top = 1

        elif player.rect.left <= 0:
            player.speedx = 0
            player.rect.left = 0
            
        elif player.rect.right >= WIDTH:
           player.speedx = 0
           player.rect.right = WIDTH
        
        tempo += 2


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

    
    
   
    
    paredes.draw(window)
    all_sprites.draw(window)
    
    tempo_faltando = 300 - int(tempo / 60)
    timer_text = font.render(f"Tempo restante: {tempo_faltando}s", True, (255, 255, 255))
    window.blit(timer_text, (20, 20))

    if modulo==POLICIA and state in retas:
        window.blit(assets[POLICIA],(10,10))
        #print('UÉ')
    elif modulo==OUTDOOR_INSPER and state in retas:
        #print('inxper')
        window.blit(assets[OUTDOOR_INSPER],(10,10))
    elif modulo==OUTDOOR_ESPM and state in retas:
        #print('festa')
        window.blit(assets[OUTDOOR_ESPM],(10,10))


    tempo += 1
    if tempo == 60*300:
        state = FIM

    pygame.display.update()


#game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados