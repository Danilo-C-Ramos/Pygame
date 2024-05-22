import pygame
from config import *
from sprites import *
from assets import *
import time
import random

def game_screen(window):
    game = True

    clock = pygame.time.Clock()

    assets = load_assets()

    state = init_screen(window, assets)

    all_sprites = pygame.sprite.Group()
    paredes = pygame.sprite.Group()
    infos = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['paredes'] = paredes

    keys_down = {}

    player = Moto(assets)
    all_sprites.add(player)

    g = Grama(assets, state)
    paredes.add(g)

    states = [DOIS_H, DOIS_VD, DOIS_VE, DOIS_H, TRES]
    retas = [RETA, RETA, RETA_D, RETA_E]

    dicas = [HIDRANTE,PLACA_DE_PARE, PLACA_RETO, PLACA_PROIBIDO, PLACA_ANIMAL, CARAMELO, ARVORE, JOIA, PINGUIM, CARRO_ESTACIONADO, BUEIRO, IDOSO]
    modulos= [OUTDOOR_INSPER, OUTDOOR_ESPM, POLICIA, CAVALO, CASA]
    modulo= 0
    decisao_n = 0
    ressorteia= True
    decisao= False
    colisao = 0

    acertos = 0
    total_acertos = 4
    max_erros = 4
    erros = 0
    tempo = 0
    anterior = 'banana'
    certa = RETA
    decidiu = DIREITA
    modulo = OUTDOOR_INSPER

    pygame.mixer.music.play(loops = -1)
    # ======== Loop Principal ========
    while state != FIM:
        states = [DOIS_H, DOIS_VD, DOIS_VE, DOIS_H, TRES]
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = FIM
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
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


        if player.speedy == -5:
            player.image = assets[MOTO]
        
        if player.rect.bottom > HEIGHT:
            player.speedy = 0
            player.rect.bottom = HEIGHT
            
        #passa pra decisao
        if (player.rect.bottom <= 0 or player.rect.left > WIDTH or player.rect.right < 0) and decisao: #and (state == RETA or state == RETA_E or state == RETA_D):

            time.sleep(0.25)
            player.rect.centerx = WIDTH / 2
            player.rect.bottom = HEIGHT - 10
            player.speedx=0

            paredes.empty()
            infos.empty()
        
            anterior = state
            while anterior == state:
                state = random.choice(states)
            
            infos, certa = info(assets, modulo, dicas, decisao_n, state, reta_anterior)
            

            g = Grama(assets, state)
            paredes.add(g)

            decisao=False
            ressorteia=True
        
        #passa pra proxima (decide)
        elif (player.rect.bottom <= 0 or player.rect.left > WIDTH or player.rect.right < 0) and ressorteia: #and state != RETA:
            if player.rect.bottom <= 0:
                decidiu = RETO
                

            elif player.rect.left > WIDTH:
                decidiu = DIREITA
                

            elif player.rect.right < 0:
                decidiu = ESQUERDA
                

            if decidiu == certa:
                acertos += 1
                
            elif decidiu != certa:
                tempo += 600
                erros += 1
                

            time.sleep(0.25)
            player.speedx= 0
            player.rect.centerx = WIDTH / 2
            player.rect.bottom = HEIGHT - 10
            
            infos.empty()
            paredes.empty()
            
            state = random.choice(retas)
            escolha=0
            reta_anterior = state

            g = Grama(assets, state)
            paredes.add(g)

            modulo = random.choice(modulos)
            ressorteia=False
            decisao=True
        
        player.update()

        
        for _ in pygame.sprite.spritecollide(player, paredes, False, pygame.sprite.collide_mask):
            
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
            
            tempo += 5

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


        if state in retas:
            window.blit(assets[modulo],(CANTO_MODULO))
        infos.draw(window)  
        all_sprites.draw(window)

        if state not in [INIT, TUTORIAL, TELA_INICIO, TELA_OLHO]:
            
            tempo += 1
            tempo_atual = END_TIME - (tempo / FPS)

            timer(window, assets, tempo_atual)
            
        if acertos == total_acertos:
            state = FIM_V
            paredes.empty()
            infos.empty()
            all_sprites.empty()
            state = end_screen(window, assets, state)
        
        elif erros == max_erros or tempo_atual <= 0:
            state = FIM_D
            paredes.empty()
            infos.empty()
            all_sprites.empty()
            state = end_screen(window, assets, state)
            
        pygame.display.update()
        