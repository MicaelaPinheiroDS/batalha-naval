def solicitar_coordenada(matriz_oponente, FAIL, ENDC):
    while True:
        entrada = input("Insira a coordenada (EX: B3): ").strip().upper()

        if len(entrada) < 2:
            print("Formato inválido.")
            continue

        letra = entrada[0]           
        numero = entrada[1:]           

        if letra not in "ABCDEFGH":
            print("Coluna inválida (use letras de A até H).")
            continue
        if not numero.isdigit():
            print("Linha inválida (precisa ser número de 1 a 8).")
            continue

        coluna = ord(letra) - ord("A")     
        linha = int(numero) - 1              

        if not (0 <= linha < 8):
            print("Linha fora do tabuleiro.")
            continue

        #Verificar se já foi jogado
        char = matriz_oponente[linha+1][coluna+1]

        if char == f'✔' or char == f'{FAIL}✖{ENDC}':
            print('Posição já jogada, tente atirar em outra posição.')
            continue

        return linha, coluna