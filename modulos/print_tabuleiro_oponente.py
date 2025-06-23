def print_tabuleiro_oponente(tabuleiro, letra_coluna, cores, ATINGIU_NENHUM, ENDC):
    #Colunas
    for i in range(9): 
        print('+---', end='')
    print()
    for i in range(9): 
        print(f'| {letra_coluna[i]} ', end='')
    print()
    for i in range(9): 
        print('+---', end='')
    print()

    for i in range(8): 
        print(f'|   ', end='')
        
        for j in range(8):
            valor = tabuleiro[i][j]
            char = ' '
            cor = ''
            if valor < 0:
                char = 'X'
                if valor != ATINGIU_NENHUM:
                   cor = cores[abs(valor) - 1] 
            elif valor > 0:
                char = 'O'
                cor = cores[valor - 1]

            print(f'| {cor}{char}{ENDC} ', end='')
        print('|')
        for i in range(9): 
            print('+---', end='')
        print('+')

