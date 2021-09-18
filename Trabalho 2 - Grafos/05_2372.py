# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# O código a seguir tem o objetivo de encontrar o melhor local para sediar uma reunião de caminhoneiros onde
# a maior distância percorrida por um deles deve ser a menor possível. Para tal utilizamos o algoritmo de 
# Floyd Warshall, pois ele nos possibilita encontrar a a menor distância de todos os vértices para cada um.
# 
# O código começa lendo o número de vértices e arestas, em seguida ele inicializa a matriz utilizada pelo 
# algoritmo e lê as entradas já conferindo se o peso a ser inserido é menor que o atual, já que inicialmente 
# este é infinito. Depois ele executa o algoritmo de Floyd Warshall normalmente e verifica o valor máximo de 
# cada linha da matriz, já comparando se este é o menor possível. Cada linha representa uma possibilidade de 
# escolha para a sede, portanto, ao verificar a linha que possui o menor valor máximo, estaremos verificando 
# qual cidade é a melhor opção, juntamente com o valor da distância máxima que um caminhoneiro pode 
# percorrer. Por fim imprimimos esse valor, que é o pedido do enunciado.   
# **********************************************************************************************************

def floyd(mat):
    for k in range(len(mat)):
        for u in range(len(mat)):
            for v in range(len(mat)):
                mat[u][v] = min(mat[u][v], mat[u][k] + mat[k][v])

n, m = map(int, input().split())

mat = [[float('inf')] * (n) for _ in range(n)]

for i in range(n):
    mat[i][i] = 0 

for _ in range(m):
    u, v, w = map(int, input().split())
    mat[u][v] = min(mat[u][v], w)
    mat[v][u] = min(mat[v][u], w)

floyd(mat)

min_max = float('inf')

for i in range(n):
    maximo = max(mat[i])
    if maximo < min_max:
        min_max = maximo

print(min_max)
