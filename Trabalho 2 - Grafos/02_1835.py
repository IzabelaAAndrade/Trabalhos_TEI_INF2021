# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# Nesse problema é preciso verificar se os pontos principais da cidade já foram conectados por estradas 
# asfaltadas. Em caso negativo, informaremos também a quantidade mínima de estradas que devem ser 
# construídas para alcançar o objetivo. Para resolvermos a questão, representaremos os pontos e as estradas
# como um grafo. Ao verificar a quantidade de componentes conexos poderemos determinar se há ou não ligações
# entre todos os pontos. Caso tenhamos mais de um componente conexo, a quantidade faltante de estradas será 
# justamente a quantidade de componentes conexos menos 1. 
# 
# O código trabalha lendo a quantidade de casos de teste e, para cada um deles, executa o processo citado 
# acima. Primeiramente, ele lê o número de elementos do grafo e a quantidade de relações que serão lidas.
# Em seguida, inicializamos a variável conectados juntamente com duas listas, uma representando o grafo e 
# outra que irá relacionar os vértices visitados. Em seguida, as entradas são lidas e armazenadas no grafo. 
# Por fim, executamos um dfs para cada vertíce que ainda não foi visitado e incrementamos a variável de 
# conectados, imprimindo que a promessa foi cumprida caso haja apenas um componente conexo ou a quantidade
# de estradas faltantes caso tenhamos mais de um componente conexo. 
# **********************************************************************************************************

def dfs(g, vis, v):
    visitar = [v]
    while visitar:
        u = visitar.pop()
        if not vis[u]:
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    visitar.append(v)

def ler():
    entrada = input()
    if entrada == "": entrada = input()
    return entrada

t = int(ler())

for i in range(1, t + 1):

    entrada = ler()
    if " " not in str(entrada):
        n = int(entrada)
        m = int(ler())
    else:
        n, m = map(int, entrada.split())

    conectados = 0

    grafo = [[] for _ in range(n + 1)]
    visitados = [False for _ in range(n + 1)]

    for j in range(m):
        v1, v2 = map(int, ler().split())
        grafo[v1].append(v2)
        grafo[v2].append(v1)

    for j in range(1, n + 1):
        if not visitados[j]:
            dfs(grafo, visitados, j)
            conectados += 1
    
    if conectados == 1:
        print(f"Caso #{i}: a promessa foi cumprida")    
    else:
        print(f"Caso #{i}: ainda falta(m) {conectados-1} estrada(s)")
