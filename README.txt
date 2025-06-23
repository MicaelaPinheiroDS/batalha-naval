gera_tabuleiro() : list[[]] de ints
{
retorna um tabuleiro com configuraçoes aleatorias de navios
cada navio tem um numero correspondente (1, 2, 3, ..., por enquanto vamos considerar até 4)
}

tiro_valido(tabuleiro, linha, coluna) : boolean
{
    verificar se a jogada é valida
    exemplo, se já jogou a casa de a1, retorna falso, pois não pode atirar onde ja atirou
}

atirar(tabuleiro, linha, coluna) : int
{
linha, coluna sao ints que correspondem a coordenada da matriz tabuleiro

retorna o numero do navio que foi acertado (1, 2, 3, ..., por enquanto vamos considerar até 4)
se nao houve acerto retorna zero
}

jogada_ia(tabuleiro_jogador) : string
{
    calcula uma jogada de IA valida para acertar o tabuleiro_jogador
    altera o tabuleiro do jogador passado como referencia
    retorna a casa que foi atirada (exemplo A4, G2, nesse formato)
}