
from modulos.gera_partida import gera_partida
from libs.solicitar_coordenada import solicitar_coordenada
from libs.aplica_tiro import aplica_tiro
from libs.atualizar_tabuleiro import atualizar_tabuleiro
from libs.verifica_tem_barco import verifica_tem_barco
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
is_venceu = verifica_tem_barco
is_start = input('Para começar aperte qualquer tecla....')
if is_start.strip():
    matriz_jogador, tabuleiro_jogador, matriz_oponente, tabuleiro_oponente = gera_partida(letra_coluna, cores, HEADER, ENDC)
        
    while True:
        is_oponente = not vez_jogador
        if vez_jogador:
            linha, coluna = solicitar_coordenada(matriz_oponente, FAIL, ENDC)
            matriz, msg = aplica_tiro(matriz_oponente, linha, coluna, FAIL, ENDC)
        
            tabuleiro_jogador, tabuleiro_oponente = atualizar_tabuleiro(matriz, tabuleiro_jogador, msg, is_oponente, cores)
            
            if is_venceu(matriz_oponente):
                print(f"{OKGREEN}Parabéns! Você afundou todos os navios inimigos!{ENDC}")
                break
        else:
            linha_idx = 0
            coluna_idx = 0
            
            while True:
                linha_idx  = random.randint(0, 7)
                coluna_idx = random.randint(0, 7)

                #Verificar se já foi jogado
                char = matriz_jogador[linha_idx+1][coluna_idx+1]

                if not (char == f'✔' or char == f'{FAIL}✖{ENDC}'):
                    break
            
            matriz, msg = aplica_tiro(matriz_jogador,linha_idx, coluna_idx, FAIL, ENDC)
        
            tabuleiro_jogador, tabuleiro_oponente = atualizar_tabuleiro(matriz, tabuleiro_oponente, msg, is_oponente, cores)
            if is_venceu(matriz_jogador):
                print(f"{FAIL}O oponente afundou todos os seus navios. Você perdeu!{ENDC}")
                break
        
    
        vez_jogador = not vez_jogador
        


        





