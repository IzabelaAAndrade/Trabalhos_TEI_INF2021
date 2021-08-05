# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão implementa uma busca em profundidade ou "depth-first search" (dfs) em
# um grafo. Para tanto, utiliza-se de duas funções: a primeira, denominada dfs e a segunda, no interior da primeira.
# denominada dfs_recursiva. A dfs cria uma lista (verificados) para armazenar vértices já visitados
# do grafo. Tem-se também as variáveis status e profundidade. Ademais, tem-se um laço de repetição que faz com que todos
# os vértices do grafo sejam visitados, mesmo que eles estejam desconectados dos demais. Para fazer a verificação
# de cada vértice, é chamada a função dfs_recursiva, a qual insere o vértice em análise na lista de vértices já
# verificados e então parte para uma investigação individual de cada um de seus adjacentes. Caso o adjacente em
# estudo não tenha sido verificado, chama-se a função dfs_recursiva em uma rotina de recursão para verificá-lo.
# Também o status de verificação é passado para 1, o que significa que o vértice analisado possui conexões
# (esta análise é importante para a impressão de quebras de linha na formatação de saída, uma vez que nodos totalmente
# desconexos não geram caminhos a serem impressos). Caso a adjacência analisada já tenha sido verificada, temos
# um caminho de via dupla, por exemplo: 3-4 pathR(G,4) também pode ser descrito por 4-3 em alguns casos. Conforme o
# enunciado, imprimem-se estes caminhos secundários em ordem numerica, um nível de profundidade após o caminho adjacente
# já analisado. Sempre que uma parte do grafo é desconexa mas gera caminhos, uma linha é pulada conforme a verificação
# de status, vértices faltantes e vértice analisado.
#
# A impressão dos espaços na frente dos caminhos foi feita através do uso da variável profundidade, a qual era incremen
# tada sempre que um nível de profundidade novo era atingido, ou seja, sempre que a função era chamada recursivamente.
#
# Os grafos que foram analisados são montados através das ligações entre arestas passadas pelo usuário. Primeiro, ar
# mazenamos estas em uma matriz auxiliar, que em sequência, é ordenada, para que as ligações entre os vértices aparecam
# na ordem hierárquica correta. Finalmente, o grafo é montado em uma matriz, na qual as linhas correspondem aos vértices
# do grafo e os itens nas colunas correspondem às adjacências do mesmo. Quando analisamos as adjacências dos vértices
# em dfs_recursiva, fazemos uma busca na lista correspondente à linha que representa o vértice, por isso utiliza-se
# "for conexão in grafo[vertice]" e não "for conexão in grafo".
# ***************************************************************************************************************

def dfs(grafo, numero_vertices):

    def dfs_recursiva(grafo, vertice, profundidade):
        status = 0
        verificados.add(vertice)
        for conexao in grafo[vertice]:
            if not conexao in verificados:
                print(espacos*profundidade+"{0}-{1} pathR(G,{2})".format(vertice, conexao, conexao))
                dfs_recursiva(grafo, conexao, profundidade+1)
                status = 1
            else:
                print(espacos*profundidade+"{0}-{1}".format(vertice, conexao))
        return status

    verificados = set()
    espacos = "  "
    profundidade = 1
    status = 0
    for vertice in range(numero_vertices):
        if not vertice in verificados:
            status = dfs_recursiva(grafo, vertice, profundidade)
            if status and len(verificados) < numero_vertices and vertice != numero_vertices-1:
                print()


numero_testes = int(input());

for i in range(numero_testes):
    numero_vertices, numero_arestas = [int(val) for val in input().split()]
    grafo = [[] for k in range(numero_vertices+1)]
    aux = []
    for j in range(numero_arestas):
        vertice, conexao = [int(val) for val in input().split()]
        aux.append([vertice, conexao])
    aux.sort()
    for j in range(len(aux)):
        grafo[aux[j][0]].append(aux[j][1])
    #grafo[vertice].append(conexao)
    print("Caso {0}:".format(i+1))
    dfs(grafo, numero_vertices)
    if i != numero_testes-1:
        print()
