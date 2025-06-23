import random

def print_tabuleiro_jogador(tabuleiro, letra_coluna, cores, ENDC):
    #Colunas
    for i in range(len(letra_coluna)): 
        print('+---', end='')
    print()

    for i in range(len(letra_coluna)): 
        print(f'| {letra_coluna[i]} ', end='')
    print()

    for i in range(len(letra_coluna)): 
        print('+---', end='')
    print()

    for i in range(8): 
        print(f'|   ', end='')
        
        for j in range(len(letra_coluna) - 1):
            valor = tabuleiro[i][j]
            char = f"{(tabuleiro[i][j])}"     
            cor = cores[valor - 1]

            if valor <= 0:
                char = ' '
                cor = cores[valor - 1]

            print(f'| {cor}{char}{ENDC} ', end='')
        print('|')

        for i in range(len(letra_coluna)): 
            print('+---', end='')
        print('+')