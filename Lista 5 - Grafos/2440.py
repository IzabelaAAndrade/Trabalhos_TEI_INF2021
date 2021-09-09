# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# Para encontrar a quantidade de famílias proposta pelo problema, basta visualizar cada pessoa como um dos
# vétices de um grafo, onde um vértice é conectado ao outro caso as duas pessoas relacionadas sejam 
# parentes, dessa forma, basta contar o número de componentes conexos desse grafo formado.
# 
# O código funciona lendo o número de elementos do grafo e a quantidade de relações que serão colocadas na 
# entrada. Depois inicializa-se duas listas, uma representando o grafo e outra que irá relacionar os 
# vértices visitados. Em seguida as entradas são lidas e armazenadas no grafo, no qual o índice representa 
# uma pessoa e a lista armazenada nesse índice representa os parentes dessa pessoa. Logo depois 
# inicializamos uma váriavel para contar a quantidade de famílias e inicializamos um for que chamará a 
# função dfs caso o vértice em questão não tenha sido visitado. Dentro da dfs visitamos todos parentes da 
# pessoa correspondente ao vértice passado, selecionando todo o componente conexo que representa uma 
# família. Caso alguns dos vértices não tenham sido visitados significa que eles pertencem a outra família,
# o que posteriormente levará a uma outra chamada da função dfs. A variável familias é incrementada toda 
# vez que um novo componente do grafo é achado, o que resulta na quantidade total de famílias, a qual é 
# impressa ao final do código.  
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

elementos, entradas = map(int, input().split())

grafo = [[] for i in range(elementos + 1)]
visitados = [False for i in range(elementos + 1)]

for i in range(entradas):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

familias = 0

for i in range(1, elementos + 1):
    if not visitados[i]:
        dfs(grafo, visitados, i)
        familias += 1

print(familias)
