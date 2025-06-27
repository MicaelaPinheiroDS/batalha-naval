def gerar_matriz_atualizada(matriz_oponente,coluna, linha, resultado):
    lin_vis = linha + 1  
    col_vis = coluna + 1  

    match resultado:
        case 'agua':
            matriz_oponente[lin_vis][col_vis] = '✖' 
        case 'acerto':
            matriz_oponente[lin_vis][col_vis] = '⬤' 
        case 'afundou':
            matriz_oponente[lin_vis][col_vis] = '☠'  
        
    return matriz_oponente