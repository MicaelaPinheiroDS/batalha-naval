# ── constantes ─────────────────────────────────────────────────────────
AGUA          = 0
TIRO_NA_AGUA  = -1
HIT           = -2
SINK          = -3

# ── 1. Aplica tiro ─────────────────────────────────────────────────────
def aplicar_tiro(tab, coluna, linha):
    """
    Modifica a matriz `tab` in-place e devolve:
        'agua', 'acerto', 'afundou' ou 'repetido'
    """
    valor = tab[coluna][linha]

    # 1) Água ainda não tentada
    if valor == AGUA:
        tab[coluna][linha] = TIRO_NA_AGUA
        return 'agua'

    # 2) Parte inédita de navio
    if valor > 0:
        tamanho_navio = valor
        tab[coluna][linha] = HIT

        # verifica se sobrou alguma parte intacta desse navio
        ainda_resta = any(
            cel == tamanho_navio
            for linha_tab in tab
            for cel in linha_tab
        )

        if not ainda_resta:
            # marca todas as partes HIT desse navio como SINK
            for i in range(8):
                for j in range(8):
                    if tab[i][j] == HIT:
                        tab[i][j] = SINK
            return 'afundou'
        return 'acerto'

    # 3) Qualquer valor negativo => já atirado ali
    return 'repetido'
