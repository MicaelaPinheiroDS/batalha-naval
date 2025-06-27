from libs.limpar_ansi import limpar_ansi

def verifica_valor_puro_coordenada(matriz, linha, coluna):

    raw = limpar_ansi(matriz[linha][coluna]).strip()
    return raw           

