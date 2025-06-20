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

def gera_tabuleiro_jogador():
    base = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for i in range(8):
        for j in range(8):
            base[i][j] = random.randint(0, 1)*random.randint(1, 4)
    return base

def gera_tabuleiro_oponente():
    base = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 3, 0, 0],
        [0, 1, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0]
    ]
    ##for i in range(8):
    ##    for j in range(8):
    #        base[i][j] = random.randint(0, 1)*random.randint(1, 4)
    return base

letra_coluna = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def print_tabuleiro_jogador(tabuleiro):
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
            elif valor > 0:
                char = 'O'
                cor = cores[valor - 1]

            print(f'| {cor}{char}{ENDC} ', end='')
        print('|')
        for i in range(9): 
            print('+---', end='')
        print('+')

def print_tabuleiro_oponente(tabuleiro):
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


def atirar(tabuleiro, linha, coluna):
    return 0

def muda_tabuleiro(tabuleiro, linha, coluna, navio):
    pass

def jogo():
    print("Batalha Naval!")
    tabuleiro_jogador = []
    tabuleiro_oponente = []

    while 1:
       tabuleiro_jogador = gera_tabuleiro_jogador()
       print_tabuleiro_jogador(tabuleiro_jogador)
       print(f"{WARNING}Confirmar esta posição para seus navios? (S confirma){ENDC}")
       if input().lower() == 's':
           break 
       
    tabuleiro_oponente = gera_tabuleiro_oponente()
    #Jogo
    while 1:
        print_tabuleiro_oponente(tabuleiro_oponente)
        
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

    
jogo()

'''
     +---+---+
     | A | B |

| 1  |    |



-1 --> navio 1 atingido
-2 --> navio 2 atingido 
-100

'''


