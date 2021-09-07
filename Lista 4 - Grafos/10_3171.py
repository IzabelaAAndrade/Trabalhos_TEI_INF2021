# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# O código em questão precisa descobrir se o cordão de LED está totalmente ligado, ou seja, se eu consigo
# visitar todos os vertices a partir de um inicial. Como podemos observar pelo codigo desenvolvido, nada
# mais é do que uma aplicacao simples da busca em profundidade em grafo não direcionado. Nós partirmos de
# um ponto inicial e precisamos encontrar todos os outros a partir dele. Para isso, foi utilizada a forma
# recursivada solucao que consiste em visitar todos os filhos dos filhos do vertice em questão encontrado
# atraves de um for. Isso gera como resultado, uma lista que, no index correspondente ao vertice, é guardado
# o valor True ou False, visitado ou não. Nós utilizamos essa lista para conferir se todos os LEDs foram 
# ligados de forma correta no final.
# **********************************************************************************************************

def dfs_rec(g, u, visitados):
    visitados[u] = True
    for v in g[u]:
        if not visitados[v]:
            dfs_rec(g, v, visitados)

#incializacao

resposta = ""

#leitura do grafo
num_vertices, num_arestas = map(int, input().split())
grafo = [[] for i in range(num_vertices+1)]

for cont in range(num_arestas):

    vertice1, vertice2 = map(int, input().split())
    grafo[vertice1].append(vertice2)
    grafo[vertice2].append(vertice1)

vertice1 = 1

visitados = [False]*(num_vertices+1)

dfs_rec(grafo, vertice1, visitados)

for cont, vertice in enumerate(visitados):

    if vertice == False and cont != 0:

        resposta = "INCOMPLETO"

        break

if not resposta == "INCOMPLETO":

    resposta = "COMPLETO"

print(resposta)
