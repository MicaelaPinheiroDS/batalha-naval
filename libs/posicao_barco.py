def posicao_bloco(tabuleiro, i, j):
    val = tabuleiro[i][j]
    cima = i > 0 and tabuleiro[i - 1][j] == val
    baixo = i < len(tabuleiro) - 1 and tabuleiro[i + 1][j] == val
    esquerda = j > 0 and tabuleiro[i][j - 1] == val
    direita = j < len(tabuleiro[i]) - 1 and tabuleiro[i][j + 1] == val

    # barco de 1 bloco
    if not (cima or baixo or esquerda or direita):
        return 'unico'

    # início horizontal ou vertical
    if not cima and not esquerda:
        return 'inicio'

    # fim horizontal ou vertical
    if not baixo and not direita:
        return 'fim'

    # meio do barco
    return 'meio'
