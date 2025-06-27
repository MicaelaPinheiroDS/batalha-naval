from libs.render_tabuleiro_jogador import render_tabuleiro_jogador
from libs.render_tabuleiro_oponente import render_tabuleiro_oponente
from libs.render_tabuleiro import render_tabuleiro


def atualizar_tabuleiro(letra_coluna, matriz_oponente, cores, HEADER, ENDC):
    


    print_tabuleiro_jogador = render_tabuleiro_jogador(letra_coluna, cores, HEADER, ENDC)

    print_tabuleiro_oponenete = render_tabuleiro_oponente(matriz_oponente, HEADER, ENDC, cores)
    
    
        
    tabuleiro = render_tabuleiro([print_tabuleiro_jogador, print_tabuleiro_oponenete])
    
    return  tabuleiro
    
    
    

