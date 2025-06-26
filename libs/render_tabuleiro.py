def render_tabuleiro(renders, sep=3):
    for linhas in zip(*renders):
        print((' ' * sep).join(linhas))
    return linhas