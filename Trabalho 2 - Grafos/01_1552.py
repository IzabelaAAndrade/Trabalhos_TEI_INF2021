# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# A presente solução ao problema apresentado implementa o algoritmo de Prim para encontrarmos a árvore 
# geradora mínima do grafo formado pelas pessoas a serem salvas. Como recebemos apenas as coordemadas de 
# cada pessoa, montamos o grafo criando uma aresta entre cada um dos pontos a todos os outros utilizando 
# como peso a distância entre esses pontos.
# 
# O código lê a quantidade de casos de teste e, para cada um deles, implementa uma solução. Primeiramente 
# lemos o número de pontos e as coordenadas de cada ponto. Em seguida inicializamos o grafo fazendo uma 
# combinação de todas as duplas de pontos possíveis, cada uma com sua distância entre si. Em seguida 
# executamos o algoritmo de Prim modificado para que, ao invés de gerar uma lista de custos e outra de 
# vértices anteriores, apenas pegarmos a distância total para percorrer a árvore geradora mínima. Por fim, 
# imprimimos essa distância dividida por 100, pois a queremos em metros, não em centímetros.
# **********************************************************************************************************

from math import sqrt
from heapq import heappush, heappop

def prim(g, n):

    u = 0
    agm = []
    distancia = 0
    inserido = [False] * n
    pq = [] 

    inserido[u] = True

    for v, peso in g[u]:
        if not inserido[v]:
            heappush(pq, (peso, u, v))

    while pq:
        peso, u, v = heappop(pq)

        if not inserido[v]:
            inserido[v] = True
            agm.append((u, v))
            distancia += peso

            for w, peso in g[v]:
                if not inserido[w]:
                    heappush(pq, (peso, v, w))
        if len(agm) == n - 1: break

    return distancia

c = int(input())

for _ in range(c):

    n = int(input())
    coord = [[0, 0] for _ in range(n)]

    for i in range(n):
        coord[i][0] , coord[i][1] = map(float, input().split())

    g = [[] for _ in range(n)]

    for u in range(n):
        for v in range(u + 1, n):
            d = sqrt((coord[u][0] - coord[v][0])**2 + (coord[u][1] - coord[v][1])**2)
            g[u].append([v, d])
            g[v].append([u, d])

    print("{:0.2f}".format(prim(g, n)/100))
