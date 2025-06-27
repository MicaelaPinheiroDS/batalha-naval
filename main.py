
from libs.gera_matriz import gera_matriz
from modulos.gera_partida import gera_partida

#Códigos de escape para colorir
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

ATINGIU_NENHUM = -100

          #vermei     #azul      #verde       #amarelo
cores = ['\033[91m', '\033[94m', '\033[92m', '\033[93m']

letra_coluna = ["A", "B", "C", "D", "E", "F", "G", "H"]

matriz_oponente, tabuleiro_oponente = gera_partida(letra_coluna, cores, HEADER, ENDC)


