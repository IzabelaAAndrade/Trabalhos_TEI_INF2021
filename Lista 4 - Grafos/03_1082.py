# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão realiza o mapeamento dos diferentes componentes conexos de um grafo.
# Para tanto, utiliza-se de um algoritmo de busca em profundidade em recursão. Antes de tudo, 
# é feita uma conversão entre letras e números, de modo a facilitar as operações. Em sequência, é criada uma lista
# multidimencional a qual representará o grafo. Tal lista é preenchida de acordo com as entradas digitadas pelo usuário,
# as quais contém as arestas do grafo. As arestas são inseridas em âmbos os sentidos para que não haja problemas na 
# identificação de componentes conexas. Os dados armazenados são dispostos em ordem crescente (usando a função sort)
# para que a exibição dos mesmos se dê em ordem alfabética, conforme solicitado pelo enunciado. Com o grafo pronto, 
# basta passá-lo, juntamente com seu número de vértices, para a função dfs. No interior desta, usa-se de um laço
# de repetição para chamar a função dfs_recursiva para todos os vértices do grafo, até que todos estejam visitados.
# Ao chamar dfs_recursiva, passa-se como parâmetro além do grafo, um vértice de referẽncia e um identificador de 
# componente conexa.
# A dfs_recursiva é executada recursivamente partindo de um vértice, até que não hajam mais componentes conexos ao 
# mesmo. Como consequência, de modo a mapear diferentes componentes, sempre que a chamada a esta função for feita
# por meio do laço de repetição que realiza uma nova busca a partir de um vértice não visitado (linha 48), ela é feita
# com um valor de componente_conexa distinto. Por outro lado, versões da dsf_recursiva executadas recursivamente 
# (linha 40), possuem os mesmos valores de componente_conexa, afinal, indicam que ainda existem conexões entre os
# vértices em análise.
# No interior da função dfs_recursiva, utiliza-se do vetor componentes_grafo para fazer a associação entre cada vértice
# do grafo (índices do array) e a componente conexa da qual eles fazem parte (valor da posição do array). 
# Quando já temos mapeada a relação entre vértices e componentes, basta utilizar de um laço de repetição para
# imprimir os valores convertidos em letras novamente que possuiam o mesmo valor para a componente conexa no vetor
# componentes_grafo. Sempre que um novo valor de componente_conexa fosse explorado, cabia o uso de uma quebra de linha,
# indicando que os vértices em questão seriam de diferentes componentes. 
# ***************************************************************************************************************

def dfs(grafo, numero_vertices, alfabeto):

    def dfs_recursiva(grafo, vertice, componente_conexa):
        visitados.add(vertice)
        componentes_grafo[vertice] = componente_conexa
        for conexao in grafo[vertice]:
            if conexao not in visitados:
                dfs_recursiva(grafo, conexao, componente_conexa)

    visitados = set()
    componente_conexa = 0
    componentes_grafo = [-1] * numero_vertices

    for vertice in range(numero_vertices):
        if vertice not in visitados:
            dfs_recursiva(grafo, vertice, componente_conexa)
            componente_conexa += 1


    for componente in range(componente_conexa):
        for i in range(numero_vertices):
            if componentes_grafo[i] == componente:
                print(alfabeto[i], end=",")

        print()


    return componente_conexa



# Dicionário com o alfabeto e os respectivos índices de cada item
alfabeto = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
            'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
            's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25 }

alfabetoInverso = {0: 'a',1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i',
                   9: 'j',10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
                   18: 's',19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

numero_testes = int(input());
for i in range(numero_testes):
    numero_vertices, numero_arestas = [int(val) for val in input().split()]
    grafo = [[] for k in range(numero_vertices)]
    aux = []
    for j in range(numero_arestas):
        vertice, conexao = input().split()
        aux.append([alfabeto[vertice], alfabeto[conexao]])
        aux.append([alfabeto[conexao], alfabeto[vertice]])
    aux.sort()
    for j in range(len(aux)):
        grafo[aux[j][0]].append(aux[j][1])
    print("Case #{0}:".format(i + 1))
    print("{0} connected components".format(dfs(grafo, numero_vertices, alfabetoInverso)))
    print()
    
