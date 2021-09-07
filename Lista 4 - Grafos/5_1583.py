# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# O codigo a seguir utiliza o algoritmo de busca em profundidade em grid. Ele comeca com a leitura do mapa
# que pode possuir os caractres definidos nas constantes AGUA, ROCHA e AGENTE (A, X e T). Durante a leitura,
# cada linha e percorrida em busca de um possivel agente contaminante. Ao encontrarmos um agente, as coordenadas
# correspondentes sao armazenadas em uma lista chamada contaminados. Apos a conclusao da leitura, a lista
# contaminados e percorrida, e, a partir de cada elemento dela, ocorre a busca em profundidade em grid. Dentro
# da funcao dfs_grid, e possivel encontrar todos os barris contaminados e os marcar com um T. O mapa resultante
# e impresso logo em seguida.
# **********************************************************************************************************

AGUA = "A"
ROCHA = "X"
AGENTE = "T"

def dfs_grid(grid, inicio):

    altura = len(grid)
    largura = len(grid[0])

    para_visitar = [inicio]

    while para_visitar:
        
        linha1, coluna1 = para_visitar.pop()
        
        for linha2, coluna2 in [(linha1 + 1, coluna1), (linha1, coluna1 + 1), (linha1 - 1, coluna1), (linha1, coluna1 - 1)]:

            if (0 <= linha2 < altura and 0 <= coluna2 < largura) and (grid[linha2][coluna2] == AGUA):

                grid[linha2][coluna2] = AGENTE
                para_visitar.append([linha2, coluna2])

while True:

    #inicializacao de variaveis
    contaminados = []
    mapa = []

    #leitura tamanho do mapa
    num_linhas, num_colunas = map(int, input().split())
    
    if num_linhas == 0 or  num_colunas == 0:

        break

    else:

        #leitura mapa
        for num_linha in range(num_linhas):

            linha = list(input())

            for num_coluna, valor in enumerate(linha):

                if valor == AGENTE:

                    contaminados.append([num_linha, num_coluna])

            mapa.append(linha)

        #percorrer mapa
        for contaminado in contaminados:

            dfs_grid(mapa, contaminado)
        
        #impressao dos dados
        for linha in mapa:

            print(''.join(linha))
        
        print()