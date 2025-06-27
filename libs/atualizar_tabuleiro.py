from libs.gera_tabuleiro import gera_tabuleiro
from libs.render_tabuleiro import render_tabuleiro

import os



def atualizar_tabuleiro(matriz, tabuleiro, msg, is_oponente, cores):
    
    os.system('cls' if os.name == 'nt' else 'clear')

    if is_oponente:
        tabuleiro_jogador = gera_tabuleiro(matriz, cores)
        render_tabuleiro([tabuleiro_jogador, tabuleiro])
        tabuleiro_oponente = tabuleiro
    else:
        tabuleiro_oponente = gera_tabuleiro(matriz, cores,ocultar_navios=True)
        tabuleiro_jogador = tabuleiro
        tabuleiro = render_tabuleiro([tabuleiro_jogador, tabuleiro_oponente])
    
    return  tabuleiro_jogador, tabuleiro_oponente
    
    

    
    
    
    

