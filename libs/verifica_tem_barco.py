from libs.verifica_valor_puro_coordenada import verifica_valor_puro_coordenada

def verifica_tem_barco(matriz: list[list[str]]) -> bool:
    for lin in range(1, 9):
        for col in range(1, 9):
            if verifica_valor_puro_coordenada(matriz, lin, col).isdigit():
                return False         
    return True                   