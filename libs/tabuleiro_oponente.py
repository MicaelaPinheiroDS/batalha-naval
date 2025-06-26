from libs.gera_tabuleiro import gera_tabuleiro

def render_tabuleiro_oponente(letras_coluna, cores,ATINGIU_NENHUM, HEADER, ENDC, FAIL):
    linhas = []
    tab = gera_tabuleiro()

    # ── cabeçalho ──
    linhas.append('+---' * 9 + '+')                 # 1 bloco vazio + 8 colunas
    letra_cabecalho = ''.join(f'| {HEADER}{l}{ENDC} ' for l in letras_coluna) + '|'
    linhas.append(letra_cabecalho)
    linhas.append('+---' * 9 + '+')

    # ── grade 8×8 ──
    for i, linha in enumerate(tab, start=1):
        linha_str = f'| {HEADER}{i}{ENDC} '
        for val in linha:
            if val > 0:                           # barco revelado
                char, cor = str(val), cores[val -1] 
            else:                                 #sem barco
                char, cor = ' ', ''
            linha_str += f'| {cor}{char}{ENDC} '
        linha_str += '|'
        linhas.append(linha_str)
        linhas.append('+---' * 9 + '+')

    return linhas