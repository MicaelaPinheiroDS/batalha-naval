from itertools import zip_longest

def render_tabuleiro(renders, sep='   '):
    saida = []
    largura_padrao = max(len(l) for tab in renders for l in tab)  # p/ preencher

    for partes in zip_longest(*renders, fillvalue=' ' * largura_padrao):
        linha = sep.join(partes)
        print(linha)          # imprime imediatamente (opcional)
        saida.append(linha)   # guarda para reutilizar

    return saida
