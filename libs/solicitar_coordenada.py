def solicitar_coordenada():
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

        return linha, coluna