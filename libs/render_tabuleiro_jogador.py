from libs.gera_tabuleiro import gera_tabuleiro

def render_tabuleiro_jogador( letras_coluna, cores,HEADER, ENDC):
    linhas = []
    tabuleiro = gera_tabuleiro()

    # 1 ── Cabeçalho
    linhas.append('+---' * 9 + '+')  # 9 blocos: 1 vazio + 8 letras
    letra_cabecalho = ''.join(f'| {HEADER}{l}{ENDC} ' for l in letras_coluna) + '|'
    linhas.append(letra_cabecalho)
    linhas.append('+---' * 9 + '+')

    # 2 ── Grade 8×8 com números
    for idx, linha in enumerate(tabuleiro, start=1):
        linha_str = f'| {HEADER}{idx}{ENDC} '  

        for val in linha:
            if val > 0:                       
                char = str(val)
                cor  = cores[val-1]
            else:                               
                char = ' '
                cor  = ''
            linha_str += f'| {cor}{char}{ENDC} '
        linha_str += '|'
        linhas.append(linha_str)
        linhas.append('+---' * 9 + '+')

    return linhas