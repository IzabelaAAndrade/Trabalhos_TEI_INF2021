# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão recebe um conjunto de indivíduos e seus relacionamentos e após uma busca
# em profundidade (dfs) exibe o número de famílias existentes. De modo a resolver tal problema, interpretaremos os
# indivíduos como vértices de um grafo e seus relacionamentos como arestas, sendo famílias diferentes, componentes
# conexas distintas do grafo. De modo a indicar participação em uma família, basta um relacionamento, independentemente
# # de qual seja, logo, o parentesco pode ser ignorado.
#
# Primeiro são armazenados os parentes. Eles são recebidos na linha 59 através de um input().split() e guardados como 
# vértices ou conexões de vértices de um grafo. Caso o indivíduo em questão ainda não tenha sido mencionado, atribui-se
# a ele um número e ele é armazenado, junto a esse número, em um dicionário. Uma vez recebido um valor numérico 
# identificador, o familiar em análise é inserido no grafo conforme o número identificador, através da chamada do 
# dicionario "familiares" na posição referente ao nome do parente
# corrente. Com o grafo montado, é feita então a ordenação do mesmo. Em sequência, é chamada a função dfs. No interior
# desta, um laço de repetição invoca a função dfs_recursiva para todos os vértices não visitados do grafo. Inicialmente,
# a lista "visitados" estará vazia, contudo, com a chamada da função dsf_recursiva para o primeiro vértice, tal situação
# é alterada. No interior de dsf_recursiva, o vértice em questão é marcado como visitado (inserido na lista 'visitados')
# e então é feita uma busca por suas adjacências em um processo recursivo de chamada da função em cheque. Tais chamadas
# recursivas farão com que todos os vértices alcançáveis (todos os pertencentes a uma dada família) a partir daquele 
# parente inicial sejam visitados. Como consequência,
# tem-se o mapeamento de uma família. Percebe-se então que, toda vez que a dfs_recursiva é invocada na linha 46,
# ou seja, para um vértice não ligado a nenhum dos anteriores ou de suas componentes, temos uma nova componente
# conexa ou uma nova família a ser contabilizada. Por isso, sempre que esta situação se repete, a variável
# "numero_familias" é incrementada.
#
# Por fim, com o término da execução do laço de repetição em dfs, a função retorna numero_familias ao código principal,
# que imprime o valor em questão.

# ***************************************************************************************************************

def dfs(grafo, numero_vertices):

    def dfs_recursiva(grafo, vertice):
        visitados.add(vertice)
        for conexao in grafo[vertice]:
            if conexao not in visitados:
                dfs_recursiva(grafo, conexao)

    visitados = set()
    numero_familias = 0

    for vertice in range(numero_vertices):
        if vertice not in visitados:
            dfs_recursiva(grafo, vertice)
            numero_familias += 1

    return numero_familias

# Dicionário com os parentes seus respectivos índices como vértices do grafo
familiares = {}

numero_vertices, numero_arestas = [int(val) for val in input().split()]
grafo = [[] for k in range(numero_vertices)]
aux = []
participante_familia = 0
for j in range(numero_arestas):
    vertice, parentesco, conexao = input().split()
    if vertice not in familiares:
        familiares[vertice] = participante_familia
        participante_familia+=1
    if conexao not in familiares:
        familiares[conexao] = participante_familia
        participante_familia+=1
    aux.append([familiares[vertice], familiares[conexao]])
    aux.append([familiares[conexao], familiares[vertice]])
aux.sort()
for j in range(len(aux)):
    grafo[aux[j][0]].append(aux[j][1])
print((dfs(grafo, numero_vertices)))
