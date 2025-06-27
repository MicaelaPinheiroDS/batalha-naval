from libs.render_tabuleiro_jogador import render_tabuleiro_jogador
from libs.render_tabuleiro_oponente import render_tabuleiro_oponente
from libs.render_tabuleiro import render_tabuleiro
from libs.gera_matriz import gera_matriz

def gera_partida(letras_coluna, cores, HEADER, ENDC):
    matriz = gera_matriz(letras_coluna)
    render_tabuleiro_oponente(matriz, letras_coluna, cores, HEADER, ENDC)
    
    return 
    
    
    

