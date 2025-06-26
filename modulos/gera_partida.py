from libs.tabuleiro_jogador import render_tabuleiro_jogador
from libs.tabuleiro_oponente import render_tabuleiro_oponente
from libs.render_tabuleiro import render_tabuleiro

def gera_partida(letra_coluna, cores, HEADER, ENDC):
    ATINGIU_NENHUM = -100
    FAIL = '\033[91m'


    print_tabuleiro_jogador = render_tabuleiro_jogador(letra_coluna, cores, HEADER, ENDC)

    print_tabuleiro_oponenete = render_tabuleiro_oponente(letra_coluna, cores, ATINGIU_NENHUM, HEADER, ENDC, FAIL)
    
        
    render_tabuleiro([print_tabuleiro_jogador, print_tabuleiro_oponenete])
    
    
    
