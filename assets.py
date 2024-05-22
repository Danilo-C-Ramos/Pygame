import pygame
import os
from config import *
from assets import *
import math
import time


BACKGROUND = 'background'
T_INI = 'fundo_init_img'
INIT_FONT = 'fonte_inicio'
TIMER_FONT = 'fonte_timer'
RETA_IMAGEM = 'reta_imagem_img'

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
PLACA_RETO = 'placa_reto_img'
PLACA_ANIMAL = 'placa_animal_img'
PLACA_PROIBIDO = 'placa_proibido_img'
HIDRANTE = 'hidrante_img'
JOIA = 'joia_img'
POLICIA = 'policia_img'
BUEIRO = 'bueiro_img'
OUTDOOR_INSPER = 'outdoor_insper_img'
OUTDOOR_ESPM = 'outdoor_espm_img'

TELA_VITORIA = 'tela_vitoria_img'
TELA_DERROTA = 'tela_derrota_img'
TELA_PRESO = 'tela_preso_img'
ULTIMA_TELA = 'ultima_tela_img'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,"background.png")).convert() # Os backgrounds devem mudar conforme o jogador muda de tela
    assets[RETA_IMAGEM] = pygame.image.load(os.path.join(IMG_DIR,"reta_imagem.png")).convert()
    assets[RETA_IMAGEM] = pygame.transform.scale(assets[RETA_IMAGEM], (WIDTH, HEIGHT))

    assets[MOTO] = pygame.image.load(os.path.join(IMG_DIR, 'moto.png')).convert_alpha()
    assets[MOTO] = pygame.transform.scale(assets['moto_img'], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[T_INI] = pygame.image.load(os.path.join(IMG_DIR, 'fundo_init.png')).convert_alpha()
    assets[T_INI] = pygame.transform.scale(assets[T_INI], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_TRAS] = pygame.image.load(os.path.join(IMG_DIR, 'moto_tras.png')).convert_alpha()
    assets[MOTO_TRAS] = pygame.transform.scale(assets[MOTO_TRAS], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIREITA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_direita.png')).convert_alpha()
    assets[MOTO_DIREITA] = pygame.transform.scale(assets[MOTO_DIREITA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_ESQUERDA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_esquerda.png')).convert_alpha()
    assets[MOTO_ESQUERDA] = pygame.transform.scale(assets[MOTO_ESQUERDA], (MOTO_WIDTH, MOTO_HEIGHT))

    '''
    assets[MOTO_DIAGONAL_DIREITA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_direita.png')).convert_alpha()
    assets[MOTO_DIAGONAL_DIREITA] = pygame.transform.scale(assets[MOTO_DIAGONAL_DIREITA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_ESQUERDA] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_esquerda.png')).convert_alpha()
    assets[MOTO_DIAGONAL_ESQUERDA] = pygame.transform.scale(assets[MOTO_DIAGONAL_ESQUERDA], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_SUDESTE] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_sudeste.png')).convert_alpha()
    assets[MOTO_DIAGONAL_SUDESTE] = pygame.transform.scale(assets[MOTO_DIAGONAL_SUDESTE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[MOTO_DIAGONAL_ESQUERDA_BAIXO] = pygame.image.load(os.path.join(IMG_DIR, 'moto_diagonal_esquerda_baixo.png')).convert_alpha()
    assets[MOTO_DIAGONAL_ESQUERDA_BAIXO] = pygame.transform.scale(assets[MOTO_DIAGONAL_ESQUERDA_BAIXO], (MOTO_WIDTH, MOTO_HEIGHT))
    '''

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

    assets[PLACA_DE_PARE] = pygame.image.load(os.path.join(IMG_DIR, 'pare.png')).convert_alpha()
    assets[PLACA_DE_PARE] = pygame.transform.scale(assets[PLACA_DE_PARE], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[PLACA_RETO] = pygame.image.load(os.path.join(IMG_DIR, 'reto.png')).convert_alpha()
    assets[PLACA_RETO] = pygame.transform.scale(assets[PLACA_RETO], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[PLACA_PROIBIDO] = pygame.image.load(os.path.join(IMG_DIR, 'proibido.png')).convert_alpha()
    assets[PLACA_PROIBIDO] = pygame.transform.scale(assets[PLACA_PROIBIDO], (MOTO_WIDTH, MOTO_HEIGHT))

    assets[PLACA_ANIMAL] = pygame.image.load(os.path.join(IMG_DIR, 'animal.png')).convert_alpha()
    assets[PLACA_ANIMAL] = pygame.transform.scale(assets[PLACA_ANIMAL], (MOTO_WIDTH, MOTO_HEIGHT))

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


    assets[INIT_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'pixeled.ttf'), 60)
    assets[TIMER_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'ds-digi.ttf'), 40)

    assets[TELA_VITORIA] = pygame.image.load(os.path.join(IMG_DIR, 'tela_vitoria.png')).convert_alpha()
    assets[TELA_VITORIA] = pygame.transform.scale(assets[TELA_VITORIA], (WIDTH, HEIGHT))

    assets[TELA_DERROTA] = pygame.image.load(os.path.join(IMG_DIR, 'tela_derrota.png')).convert_alpha()
    assets[TELA_DERROTA] = pygame.transform.scale(assets[TELA_DERROTA], (WIDTH, HEIGHT))

    assets[TELA_PRESO] = pygame.image.load(os.path.join(IMG_DIR, 'tela_preso.png')).convert_alpha()
    assets[TELA_PRESO] = pygame.transform.scale(assets[TELA_PRESO], (WIDTH, HEIGHT))

    pygame.mixer.music.load(os.path.join(SND_DIR, 'pizzatron_3000.mp3'))
    pygame.mixer.music.set_volume(0.4)

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

def init_screen(screen, assets):
    font = pygame.font.SysFont(None, 40)

    # Carrega o fundo da tela inicial
    background = assets[T_INI]
    background = pygame.transform.scale(assets[T_INI], (WIDTH, HEIGHT))
    background_rect = background.get_rect()
  
    transparencia = pygame.Surface((WIDTH, HEIGHT))
    transparencia.set_alpha(220)
    transparencia.fill(BLACK)

    texto1 = font.render("Pressione Qualquer Tecla", True, WHITE)
    texto1_rect = texto1.get_rect()
    texto1_rect.center = (WIDTH / 2, HEIGHT - 100)

    nome = assets[INIT_FONT].render('Insper Eats', True, RED)
    nome_rect = nome.get_rect()
    nome_rect.center = (WIDTH / 2, HEIGHT / 2)

    pulso = 3  # Velocidade da pulsação
    max_alpha = 255  # Transparência máxima
    min_alpha = 20   # Transparência mínima

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    running = True
    state = TELA_INICIO

    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP and state == TUTORIAL:
                print('indo para a tela preta')
                state = TELA_OLHO
                background = assets[B_RETA_D]

            if event.type == pygame.KEYUP and state != TUTORIAL and state != TELA_OLHO:
                print('tutorial')
                state = TUTORIAL
            

        if state == TELA_INICIO:
            #Efeito de piscar na tela:
            tempo = pygame.time.get_ticks() / 1000.0
            alpha = (max_alpha - min_alpha) / 2 * (math.sin(pulso * tempo) + 1) + min_alpha
            texto1.set_alpha(alpha)

            # A cada loop, redesenha o fundo e os sprites
            screen.fill(BLACK)
            screen.blit(background, background_rect)
            screen.blit(transparencia, (0, 0))

            screen.blit(texto1, texto1_rect)
            screen.blit(nome, nome_rect)

            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()

        if state == TUTORIAL:
                screen.fill(BLACK)
                background = assets[B_RETA_E]
                background_rect = background.get_rect()
                screen.blit(background, background_rect)
                pygame.display.flip()

        if state == TELA_OLHO:
                i = 255
                while i > 0:
                    texto1 = font.render("Esta tela é apenas para os seus olhos", True, WHITE)
                    texto1.set_alpha(i)
                    texto1_rect = texto1.get_rect()
                    texto1_rect.center = (WIDTH / 2, HEIGHT/2)

                    background = assets[RETA_IMAGEM]
                    background_rect = background.get_rect()
                    
                    transparencia = pygame.Surface((WIDTH, HEIGHT))
                    transparencia.set_alpha(i + 40)
                    transparencia.fill(BLACK)

                    screen.blit(background, background_rect)
                    screen.blit(transparencia, (0,0))
                    screen.blit(texto1, (texto1_rect))

                    pygame.display.flip()
                    time.sleep(0.018)
                    i -= 1

                
                state = RETA
                running = False

    return state


def timer(screen, assets, tempo):
    minutos = tempo // 60
    segundos = tempo % 60

    fundo_digitos = assets[TIMER_FONT].render(" 8:88", True, GRAY)
    fundo_digitos.set_alpha(100)
    
    digitos = assets[TIMER_FONT].render(f" {int(minutos)}:{int(segundos):02}", True, YELLOW)
    digitos_rect = digitos.get_rect()
    digitos_rect.center = (X_TIMER, Y_TIMER)

    sobra = 15
    fundo_rect = pygame.Rect(
        X_TIMER - sobra, Y_TIMER - sobra,
        X_TIMER + digitos_rect.width - sobra, Y_TIMER + sobra,
                   )
    
    # Desenha o retângulo atrás do texto do timer
    pygame.draw.rect(screen, GRAY, fundo_rect)
    
    #borda para o triangulo:
    inner_rect = fundo_rect.inflate(-10, -10)
    pygame.draw.rect(screen, BLACK, inner_rect)

    screen.blit(fundo_digitos, digitos_rect.center)
    screen.blit(digitos, (X_TIMER,Y_TIMER))
    return 

def end_screen(assets, state):
     
    if state == FIM_V:
        background = assets[ULTIMA_TELA]
        nome = assets[INIT_FONT].render('VOCÊS VENCERAM!', True, RED)
    if state == FIM_D:
          background = assets[ULTIMA_TELA]
          nome = assets[INIT_FONT].render('VOCÊS PERDERAM!', True, RED)
    if state == FIM_P:
          background = assets[ULTIMA_TELA]
          nome = assets[INIT_FONT].render('VOCÊ ESTÁ PRESO!', True, RED)

     


