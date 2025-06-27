
from modulos.gera_partida import gera_partida
from libs.solicitar_coordenada import solicitar_coordenada
from libs.aplica_tiro import aplica_tiro
from libs.atualizar_tabuleiro import atualizar_tabuleiro
import random

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
vez_jogador = True


is_start = input('Para começar aperte qualquer tecla....')
if is_start.strip():
    matriz_jogador, tabuleiro_jogador, matriz_oponente, tabuleiro_oponente = gera_partida(letra_coluna, cores, HEADER, ENDC)
        
    while True:
        is_oponente = not vez_jogador
        if vez_jogador:
            linha, coluna = solicitar_coordenada()
            matriz, msg = aplica_tiro(matriz_oponente, linha, coluna, FAIL, ENDC)
        
            tabuleiro_jogador, tabuleiro_oponente = atualizar_tabuleiro(matriz, tabuleiro_jogador, msg, is_oponente, cores)
        else:
            linha_idx  = random.randint(1, 7)
            coluna_idx = random.randint(1, 7)
            matriz, msg = aplica_tiro(matriz_jogador,linha_idx, coluna_idx, FAIL, ENDC)
        
            tabuleiro_jogador, tabuleiro_oponente = atualizar_tabuleiro(matriz, tabuleiro_oponente, msg, is_oponente, cores)
        
    
        vez_jogador = not vez_jogador
        


        





