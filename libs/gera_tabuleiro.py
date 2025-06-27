def gera_tabuleiro(matriz, cores, ocultar_navios=False, mapa_chars=None):
    def contem_cor(texto: str, cores) -> bool:
        return any(cor in texto for cor in cores)

    if mapa_chars is None:
        mapa_chars = {' ': ' '}      

    linhas   = []
    moldura  = '+---' * 9 + '+'

    # ── percorre linhas e colunas ───────────────────────────────────
    for lin in range(9):
        linhas.append(moldura)
        linha_str = ''

        for col in range(9):
            val = str(matriz[lin][col])
            is_header = lin == 0 or col == 0
            is_barco = contem_cor(val, cores)        
            
            if is_header:
                char = str(val)
                
            elif ocultar_navios and is_barco:
                char = ' '
                
        
            else:
                char = mapa_chars.get(char, val).strip()
        

            if is_header:
                linha_str += f'| {char} ' if len(char) == 1 else f'|{ char}'
            elif is_barco:
                linha_str += f'| {char} ' if len(char) == 1 else f'| { char} '
            else:
                 linha_str += f'| {char} ' if len(char) == 1 else f'| { char}  '
        

        linha_str += '|'
        linhas.append(linha_str)

    linhas.append(moldura)
    return linhas