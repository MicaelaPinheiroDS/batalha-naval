import random

def gera_tabuleiro():
    tabuleiro = [[0 for _ in range(8)] for _ in range(8)]
    tamanhos = [random.randint(2, 4) for _ in range(4)]  

    for barco_id, tamanho in enumerate(tamanhos, start=1):
        colocado = False
        tentativas = 0

        while not colocado and tentativas < 100:
            linha = random.randint(0, 7)
            col = random.randint(0, 8 - tamanho)
            if all(tabuleiro[linha][col + i] == 0 for i in range(tamanho)):
                for i in range(tamanho):
                    tabuleiro[linha][col + i] = barco_id  
                colocado = True
            tentativas += 1

    return tabuleiro