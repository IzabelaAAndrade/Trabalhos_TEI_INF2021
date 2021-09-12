# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ************************************************************************************************************
# O codigo a seguir utiliza o algoritmo de prim para encontrar o custo minimo em uma arvore geradora minima.
# O objetivo do codigo é encontrar o caminho de menor custo que o Papai Noel pode percorrer de modo a visitar
# todas as cidades. Esse custo foi calculado dentro do algoritmo de prim que trabalha com listas de prioridade.
# Ele visita os caminhos atraves dessa lista e, portanto, consegue trabalhar com os caminhos que possuem um 
# peso menor.
# ***********************************************************************************************************

from heapq import heappush, heappop

def prim(grafo, num_vertices):

    vertice1 = 0
    agm = []
    custo = 0
    inserido = [False] * num_vertices
    fila_prioridade = [] 

    inserido[vertice1] = True

    for vertice2, peso in grafo[vertice1]:

        if not inserido[vertice2]:

            heappush(fila_prioridade, (peso, vertice1, vertice2))

    while fila_prioridade:

        peso, vertice1, vertice2 = heappop(fila_prioridade)

        if not inserido[vertice2]:

            inserido[vertice2] = True

            agm.append((vertice1, vertice2))

            custo += peso

            for vertice3, peso in grafo[vertice2]:

                if not inserido[vertice3]:

                    heappush(fila_prioridade, (peso, vertice2, vertice3))

    return agm, custo

while True:

    num_vertices, num_arestas = map(int, input().split())

    if num_vertices == 0 and num_arestas == 0:

        break

    else:

        grafo = [[] for num_vertice in range(num_vertices)]

        for num_aresta in range(num_arestas):

            vertice1, vertice2, peso = map(int, input().split())

            grafo[vertice1].append([vertice2, peso])
            grafo[vertice2].append([vertice1, peso])

        agm, custo = prim(grafo, num_vertices)

        print(custo)