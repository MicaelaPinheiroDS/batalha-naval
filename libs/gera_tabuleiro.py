import random

def gera_tabuleiro():
    tabuleiro = [[0 for _ in range(8)] for _ in range(8)]
    quantidade_barcos = random.randint(8, 10)
    barcos = [random.randint(1, 4) for _ in range(quantidade_barcos)]
    
    for tamanho in barcos:
        colocado = False
        tentativas = 0

        while not colocado and tentativas < 100:
            linha = random.randint(0, 7)
            col = random.randint(0, 8 - tamanho)
            if all(tabuleiro[linha][col + i] == 0 for i in range(tamanho)):
                for i in range(tamanho):
                    tabuleiro[linha][col + i] = tamanho
                colocado = True
            tentativas += 1

    return tabuleiro