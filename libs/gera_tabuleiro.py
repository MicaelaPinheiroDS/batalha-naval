import re

def gera_tabuleiro(matriz, ocultar_navios=False, mapa_chars=None):
    _ansi = re.compile(r'\033\[0-9]*m')
    if mapa_chars is None:
        mapa_chars = {' ': ' '}      

    linhas   = []
    moldura  = '+---' * 9 + '+'

    # ── percorre linhas e colunas ───────────────────────────────────
    for lin in range(9):
        linhas.append(moldura)
        linha_str = ''

        for col in range(9):
            val = matriz[lin][col]         
            _is_number = _ansi.sub('', str(val))
            
            if lin == 0 or col == 0:
                char = str(val)
                
            if ocultar_navios and _is_number.isdigit() and (lin != 0 and col != 0):
                char = ' '
                
        
            else:
                char = mapa_chars.get(char, str(val))
        
            linha_str += f'| {char} ' if len(char) == 1 else f'|{char}'

        linha_str += '|'
        linhas.append(linha_str)

    linhas.append(moldura)
    return linhas
