import pygame
from config import *
from sprites import *
from assets import *
import time
import random

def game_screen(window):
    game = True

    clock = pygame.time.Clock()

    #Pega os assets necessários (imagens, fontes...)
    assets = load_assets()

    #Roda função que carrega as telas de inicio
    state = init_screen(window, assets)

    #Grupos de sprites
    all_sprites = pygame.sprite.Group()
    paredes = pygame.sprite.Group()
    infos = pygame.sprite.Group()
    keys_down = {}
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['paredes'] = paredes

    #criação do sprite do player
    player = Moto(assets)
    all_sprites.add(player)

    #paredes da primeira tela
    g = Grama(assets, state)
    paredes.add(g)

    #listas das possibilidades de telas, dicas e módulos:
    states = [DOIS_H, DOIS_VD, DOIS_VE, DOIS_H, TRES]
    retas = [RETA, RETA, RETA_D, RETA_E]
    dicas = [HIDRANTE,PLACA_DE_PARE, PLACA_RETO, PLACA_PROIBIDO, PLACA_ANIMAL, CARAMELO, ARVORE, JOIA, PINGUIM, CARRO_ESTACIONADO, BUEIRO, IDOSO]
    modulos= [OUTDOOR_INSPER, OUTDOOR_ESPM, POLICIA, CAVALO, CASA]
    
    ressorteia = True
    decisao = False

    acertos = 0
    total_acertos = 4
    max_erros = 4
    erros = 0
    tempo = 0
    anterior = 'banana'
    certa = RETA
    decidiu = DIREITA
    modulo = OUTDOOR_INSPER

    #música de fundo
    pygame.mixer.music.play(loops = -1)
    # ======== Loop Principal ========
    while state != FIM:
        states = [DOIS_H, DOIS_VD, DOIS_VE, DOIS_H, TRES]
        clock.tick(FPS)
    
        #testando teclas presionadas
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

        #bloqueio para o jogador não conseguir escapar da ela por baixo
        if player.speedy == -5:
            player.image = assets[MOTO]
        
        if player.rect.bottom > HEIGHT:
            player.speedy = 0
            player.rect.bottom = HEIGHT
            
        #passa pra tela decisao
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
            
            infos, certa = info(assets, modulo, dicas, state, reta_anterior)
            

            g = Grama(assets, state)
            paredes.add(g)

            decisao=False
            ressorteia=True
        
        #passa para tela reta, verifica acerto e sorteia a próxima tela de decisão
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

        #verifica colisao
        for _ in pygame.sprite.spritecollide(player, paredes, False, pygame.sprite.collide_mask):
            
            #bloqueia o jogador de escapar da tela pelas paredes (parte verde)
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
            
            tempo += 5 #aumenta a velocidade do tempo perdido para "punir" por estar andando fora da rua

        #desenha na tela o background certo
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

        #desenha as paredes
        paredes.draw(window)

        #desenha o módulo se for uma reta
        if state in retas:
            window.blit(assets[modulo],(CANTO_MODULO))

        #desenha dicas e sprites
        infos.draw(window)  
        all_sprites.draw(window)

        #calcula e desenha o timer:
        if state not in [INIT, TUTORIAL, TELA_INICIO, TELA_OLHO]:
            tempo += 1
            tempo_atual = END_TIME - (tempo / FPS)

            #função para desenhar o timer
            timer(window, assets, tempo_atual)
            
        #lógica para finalizar o jogo e chamar função de tela final
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


#Função que segue a lógica do manual para testar as decisões. Retorna as infos que serão desenhadas na tela e a decisão certa
def info(assets, modulo, dicas, mapa, m_anterior):
    sorteadas = []
    infos = pygame.sprite.Group()

    p_sort = []
    qtd = random.randint(2, 5)
   

    escolha = random.choice(dicas)
    posicao = random.choice(POSICOES)
    
    p_sort.append(posicao)
    sorteadas.append(escolha)
    
    
    dica = Informacao(assets, escolha, posicao)
    infos.add(dica)

    for _ in range(qtd - 1):
        escolha = random.choice(dicas)
        posicao = random.choice(POSICOES)

        while escolha in sorteadas:
           
            escolha = random.choice(dicas)
        
        while posicao in p_sort:
            posicao = random.choice(POSICOES)
        
        p_sort.append(posicao)
        sorteadas.append(escolha)
       
        dica = Informacao(assets, escolha, posicao)
        infos.add(dica)  
        


        #testando cada possibilidade para cada seção do manual
        if m_anterior == RETA:
            if modulo == OUTDOOR_ESPM:
                if PLACA_PROIBIDO in sorteadas and PLACA_ANIMAL in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif IDOSO in sorteadas and PLACA_RETO in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = DIREITA

            if modulo == OUTDOOR_INSPER:
                if mapa in P_RETO:
                    certa = RETO
                elif mapa in P_ESQUERDA:
                    certa = ESQUERDA
                else:
                    certa = DIREITA


            if modulo == POLICIA:
                if ARVORE in sorteadas and BUEIRO in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif CARAMELO in sorteadas and HIDRANTE in sorteadas and mapa in P_RETO:
                    certa = RETO
                elif mapa in P_DIREITA:
                    certa = DIREITA
                else:
                    certa = RETO

            if modulo == CAVALO:
                if CARAMELO in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif CARRO_ESTACIONADO in sorteadas and ARVORE in sorteadas and mapa in P_RETO:
                    certa = RETO
                elif mapa in P_DIREITA:
                    certa = DIREITA
                else:
                    certa = RETO

            if modulo == CASA:
                if CARAMELO in sorteadas and BUEIRO in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif PLACA_PROIBIDO in sorteadas and HIDRANTE in sorteadas and mapa in P_RETO:
                    certa = RETO
                elif mapa in P_ESQUERDA:
                    certa = ESQUERDA
                else:
                    certa = DIREITA

        if m_anterior == RETA_D:
           
            if modulo == OUTDOOR_ESPM:
                if PLACA_DE_PARE in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif ARVORE in sorteadas and PLACA_ANIMAL in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = DIREITA

            if modulo == OUTDOOR_INSPER:
                if mapa in P_RETO:
                    certa = RETO
                elif mapa in P_DIREITA:
                    certa = DIREITA
                else:
                    certa = ESQUERDA


            if modulo == POLICIA:
                if PINGUIM in sorteadas and PLACA_PROIBIDO in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif CARRO_ESTACIONADO in sorteadas and IDOSO in sorteadas and mapa in P_RETO:
                    certa = RETO
                elif mapa in P_DIREITA:
                    certa = DIREITA
                else:
                    certa = RETO

            if modulo == CAVALO:
                if JOIA in sorteadas and CARAMELO in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif HIDRANTE in sorteadas and IDOSO in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = ESQUERDA

            if modulo == CASA:
                if CARRO_ESTACIONADO in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif BUEIRO in sorteadas and ARVORE in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = DIREITA
        
        if m_anterior == RETA_E:
            
            if modulo == OUTDOOR_ESPM:
                if CARAMELO in sorteadas and JOIA in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif ARVORE in sorteadas and PLACA_DE_PARE in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = DIREITA

            if modulo == OUTDOOR_INSPER:
                if mapa in P_RETO:
                    certa = RETO
                elif mapa in P_DIREITA:
                    certa = DIREITA
                else:
                    certa = ESQUERDA


            if modulo == POLICIA:
                if JOIA in sorteadas and PLACA_RETO in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif CARRO_ESTACIONADO in sorteadas and BUEIRO in sorteadas and mapa in P_RETO:
                    certa = RETO
                elif mapa in P_DIREITA:
                    certa = DIREITA
                else:
                    certa = ESQUERDA

            if modulo == CAVALO:
                if PINGUIM in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif CARRO_ESTACIONADO in sorteadas and PLACA_RETO in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = ESQUERDA

            if modulo == CASA:
                if JOIA in sorteadas and PINGUIM in sorteadas and mapa in P_DIREITA:
                    certa = DIREITA
                elif PLACA_PROIBIDO in sorteadas and ARVORE in sorteadas and mapa in P_ESQUERDA:
                    certa = ESQUERDA
                elif mapa in P_RETO:
                    certa = RETO
                else:
                    certa = DIREITA
           
    return infos, certa