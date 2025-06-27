from libs.gera_tabuleiro import gera_tabuleiro
from libs.gera_matriz import gera_matriz
from libs.render_tabuleiro import render_tabuleiro
def gera_partida(letra_coluna, cores, HEADER, ENDC):
    
    matriz_jogador = gera_matriz(letra_coluna, cores, HEADER, ENDC)
    matriz_oponente = gera_matriz(letra_coluna, cores, HEADER, ENDC)
    
    tabuleiro_jogador = gera_tabuleiro(matriz_jogador, cores, ocultar_navios=False)
    tabuleiro_oponente = gera_tabuleiro(matriz_oponente, cores, ocultar_navios=True)
    
    render_tabuleiro([tabuleiro_jogador, tabuleiro_oponente])
    

    
    
    
    return matriz_jogador, tabuleiro_jogador, matriz_oponente, tabuleiro_oponente
    
    
    

