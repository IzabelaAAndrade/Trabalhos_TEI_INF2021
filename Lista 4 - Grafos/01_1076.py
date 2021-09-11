# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# O codigo a seguir utiliza o algoritmo de busca em profundidade em grafo para contabilizar quantos movimentos
# sao necessarios para desenhar um labirinto. Para encontrarmos o resultado basta contabilizar atraves de uma
# variavel global quantas visitas sao necessarias para desenhar o labirinto/grafo. Ao final, e preciso voltar
# todo o percurso, ou seja, multiplicar por dois. 
# **********************************************************************************************************

def dfs_rec(grafo, u, visitados):

    global movimentos

    visitados[u] = True

    for vertice in grafo[u]:

        if not visitados[vertice]:

            movimentos += 1
            dfs_rec(grafo, vertice, visitados)

casos = int(input())

for num_caso in range(casos):

    movimentos = 0

    nodo_inic = int(input())

    quant_vertices, quant_arestas = map(int, input().split())

    grafo = [[] for num_vertice in range(quant_vertices+1)]
    visitados = [False]*(quant_vertices+1)
    
    for num_aresta in range(quant_arestas):

        vertice1, vertice2 = map(int, input().split())
        
        grafo[vertice1].append(vertice2)
        grafo[vertice2].append(vertice1)

    dfs_rec(grafo, nodo_inic, visitados)

    print(movimentos*2)

