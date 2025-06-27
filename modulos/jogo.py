from libs.gera_tabuleiro_jogador import gera_tabuleiro_jogador
from libs.render_tabuleiro_jogador import print_tabuleiro_jogador
from libs.render_tabuleiro_oponente import print_tabuleiro_oponente


def jogo(letra_coluna, cores, ENDC, WARNING, FAIL):
    print("Batalha Naval!")
    tabuleiro_jogador = []
    tabuleiro_oponente = []

    while 1:
       tabuleiro_jogador = gera_tabuleiro_jogador()
       print_tabuleiro_jogador(tabuleiro, letra_coluna, cores, ENDC)
       print(f"{WARNING}Confirmar esta posição para seus navios? (S confirma){ENDC}")
       if input().lower() == 's':
           break 
       
    tabuleiro_oponente = gera_tabuleiro_oponente()
    #Jogo
    while 1:
        print_tabuleiro_oponente(tabuleiro_oponente, letra_coluna, cores, ENDC)
        
        #loop turno do jogador
        while 1: #a8
            print(f"{WARNING}Coordenada para atirar:{ENDC}")
            entrada = input()
            if len(entrada) != 2:
                print("Formato de entrada inválido.")
                continue
            coluna_char = entrada[0]
            linha = entrada[1]

            if not (linha.isdigit()):
                print("Formato de entrada inválido.")
                continue
            if not ('A' <= coluna_char.upper() <= 'H'):
                print("Formato de entrada inválido.")
                continue

            #distancia até o char A
            coluna = 65 - ord(coluna_char.upper())

            valido = True#tiro_valido(linha, coluna)

            if not valido:
                print("Entrada inválida, tente atirar em outra posição.")
                continue

            #pensei nesse algoritmo, talvez se encaixa melhor na parte funcional
            acerto = atirar(tabuleiro_oponente, linha, coluna)

            #se não acertar, pula a vez
            if acerto == 0:
                break
            #se não, repete enquanto estiver acertando

            #mudar o tabuleiro
            tabuleiro_oponente[linha][coluna] = -acerto
            
        
        #turno do oponente
        ataque_oponente = 'A1' #jogada_ia(tabuleiro_jogador, tabuleiro_oponente)

        print(f"{FAIL}Seu oponente joga {ENDC}{WARNING}{ataque_oponente}{ENDC}")
        print("Seu tabuleiro: ")
        print_tabuleiro_jogador()
