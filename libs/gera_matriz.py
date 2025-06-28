import random
def gera_matriz(letras_coluna, cores, HEADER, ENDC):
    matriz = [[' ' for _ in range(9)] for _ in range(9)]
    matriz[0][1:] = [f' {HEADER}{letra}{ENDC} ' for letra in letras_coluna]
    for i in range(1,9):
            matriz[i][0] = f' {HEADER}{str(i)}{ENDC} '
    
    barco = [random.randint(2, 4) for _ in range(4)]  
        
    for barco_id, tamanho in enumerate(barco, 1):
        colocado = False
        while not colocado:
            orient = random.choice(('horizontal', 'vertical'))

            if orient == 'horizontal':
                linha = random.randint(1, 8)
                col   = random.randint(1, 9 - tamanho)

                if all(matriz[linha][c] == ' ' for c in range(col, col + tamanho)):
                    cor = cores[(barco_id - 1) % len(cores)]      
                    for c in range(col, col + tamanho):
                        matriz[linha][c] = f' {cor}{barco_id}{ENDC} '
                    colocado = True

            else: 
                col   = random.randint(1, 8)
                linha = random.randint(1, 9 - tamanho)

                if all(matriz[r][col] == ' ' for r in range(linha, linha + tamanho)):
                    cor = cores[(barco_id - 1) % len(cores)]
                    for r in range(linha, linha + tamanho):
                        matriz[r][col] = f' {cor}{barco_id}{ENDC} '
                    colocado = True
            
    


    return matriz