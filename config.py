from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

MOTO_WIDTH = 160
MOTO_HEIGHT = 160

MAIOR_WIDTH = 220
MAIOR_HEIGHT = 220  #Tamanhos aleatorios ate o momento

DICA_WIDTH = 80
DICA_HEIGHT = 80

VO_WIDTH = 60
VO_HEIGHT = 60

PLACA_WIDTH = 180
PLACA_HEIGHT = 180




#Dados gerais
WIDTH = 720
HEIGHT = 720
FPS = 60
END_TIME = 180
X_TIMER = 60
Y_TIMER = 60

CANTO_SUPERIOR = (WIDTH-180, 40)
CANTO_INFERIOR_E = (120, HEIGHT-60)
CANTO_INFERIOR_D = (WIDTH-120, HEIGHT-90)
CANTO_SUPERIOR_E = (200, 90)

CANTO_SUPERIOR_2 = (WIDTH-120, 50)

CANTO_MODULO = (WIDTH-200, 60)

POSICOES = [CANTO_INFERIOR_E, CANTO_INFERIOR_D, CANTO_SUPERIOR, CANTO_SUPERIOR_2, CANTO_SUPERIOR_E]


# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (110, 110, 110)

# Estados para controle do fluxo da aplicação
INIT = 0
RETA = 1
RETA_E = 2
RETA_D = 3
DOIS_VE = 4
DOIS_VD = 5
DOIS_H = 6
TRES = 7
FIM = 8
QUIT = 9
TUTORIAL = 10
TELA_INICIO = 11
TELA_OLHO = 12
FIM_V = 13
FIM_D = 14
FIM_P = 15

DIREITA = 16
ESQUERDA = 17
RETO = 18

P_DIREITA = [DOIS_VD, DOIS_H, TRES]
P_ESQUERDA = [DOIS_VE, DOIS_H, TRES]
P_RETO = [DOIS_VE, DOIS_VD, TRES]