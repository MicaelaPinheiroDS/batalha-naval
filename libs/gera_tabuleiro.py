from libs.verifica_valor_puro_coordenada import verifica_valor_puro_coordenada
def gera_tabuleiro(matriz, cores, ocultar_navios=False, mapa_chars=None):
    if mapa_chars is None:
        mapa_chars = {' ': ' '}      

    linhas   = []
    moldura  = '+---' * 9 + '+'

    for lin in range(9):
        linhas.append(moldura)
        linha_str = ''

        for col in range(9):
            val = str(matriz[lin][col])
            raw = val if isinstance(val, str) else str(val)
            is_header = lin == 0 or col == 0 
            is_barco = verifica_valor_puro_coordenada(matriz, lin, col).isdigit()    
            
            if is_header:
                char = raw
            
                
            elif ocultar_navios and is_barco:
                char = ' '
                
        
            else:
                chave = verifica_valor_puro_coordenada(matriz, lin, col)
                char = mapa_chars.get(chave, raw).strip()
        

            if is_header:
                linha_str += f'| {char} ' if len(char) == 1 else f'|{char}'
            elif is_barco:
                linha_str += f'| {char} ' if len(char) == 1 else f'| {char} '
            elif char == '\033[91m✖\033[0m':
                linha_str += f'| {char} ' if len(char) == 1 else f'| {char} '
            else:
                 linha_str += f'| {char} ' if len(char) == 1 else f'| {char}  '
        

        linha_str += '|'
        linhas.append(linha_str)

    linhas.append(moldura)
    return linhas