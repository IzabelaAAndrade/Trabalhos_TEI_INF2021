
from heapq import heappush, heappop

def dijkstra(grafo, num_vertices, origem):

    anterior = [-1] * num_vertices

    distancia = [float('inf')] * num_vertices

    anterior[origem] = origem

    distancia[origem] = 0

    #fila de prioridade de tupla (distancia, vertice)
    fila_prioridade = []

    heappush(fila_prioridade, (0, origem))

    while fila_prioridade:

        dist, u = heappop(fila_prioridade)

        if dist > distancia[u]:
            
            continue    #distancia maior do que encontrada
        
        for v, peso in grafo[u]:

            if distancia[u] + peso < distancia[v]:

                distancia[v] = distancia[u] + peso
                anterior[v] = u
                heappush(fila_prioridade, (distancia[v], v))
    
    return distancia, anterior

while True:

    num_cidades, num_estradas, num_cidades_rota, cidade_conserto = map(int, input().split())

    if num_cidades == 0:

        break

    else:

        grafo = [[] for num_vertice in range(num_cidades)]

        for num_cidade in range(num_cidades):

            vertice1, vertice2, peso = map(int, input().split())

            grafo[vertice1].append([vertice2, peso])
            grafo[vertice2].append([vertice1, peso])

        dijkstra(grafo, num_cidades, cidade_conserto)
        

        


