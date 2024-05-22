from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

MOTO_WIDTH = 170
MOTO_HEIGHT = 170
CARRO_WIDTH = 80
CARRO_HEIGHT = 120  #Tamanhos aleatorios ate o momento



#Dados gerais
WIDTH = 720
HEIGHT = 720
FPS = 60
END_TIME = 180
X_TIMER = 60
Y_TIMER = 60
CANTO_SUPERIOR = (WIDTH-200, 70)
CANTO_INFERIOR_E = (125, HEIGHT-80)
CANTO_INFERIOR_D = (WIDTH-120, HEIGHT-125)
CANTO_SUPERIOR_E = (80, 300)
MEIO = (WIDTH-120, 120)

POSICOES = [CANTO_INFERIOR_E, CANTO_INFERIOR_D, CANTO_SUPERIOR, MEIO, CANTO_SUPERIOR_E]


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