from libs.gera_tabuleiro import gera_tabuleiro
from libs.print_tabuleiro_jogador import print_tabuleiro_jogador

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

letra_coluna = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]


tabuleiro = gera_tabuleiro()

print_tabuleiro_jogador(tabuleiro, letra_coluna, cores, ENDC)
'''
     +---+---+
     | A | B |

| 1  |    |



-1 --> navio 1 atingido
-2 --> navio 2 atingido 
-100

'''


