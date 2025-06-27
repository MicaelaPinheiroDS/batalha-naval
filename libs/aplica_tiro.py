from libs.verifica_valor_puro_coordenada import verifica_valor_puro_coordenada

def aplica_tiro(matriz, linha, coluna, FAIL, ENDC):
    linha += 1
    coluna += 1
    if verifica_valor_puro_coordenada(matriz, linha, coluna).isdigit():
        matriz[linha][coluna] = f'⬤'
        return matriz, f'Acerto na coordenada ({linha}, {coluna})'
    else:
        matriz[linha][coluna] = f'{FAIL}✖{ENDC}'
        return matriz, f'Água na coordenada ({linha}, {coluna})'