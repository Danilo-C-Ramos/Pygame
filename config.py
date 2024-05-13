from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
#FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

MOTO_WIDTH = 50
MOTO_HEIGHT = 60
CARRO_WIDTH = 80
CARRO_HEIGHT = 120  #Tamanhos aleatorios ate o momento

#Dados gerais
WIDTH = 1280
HEIGHT = 720
FPS = 60

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
FIM = 2
QUIT = 3