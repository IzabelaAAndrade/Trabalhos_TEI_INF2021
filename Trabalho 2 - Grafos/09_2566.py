# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão nos permite calcular o custo mínimo necessário para ir de uma cidade
# natal 1 até BH, representada por N (número de cidades existentes). Para tanto, é utilizado o algoritmo de
# dijkstra, o qual auxilia no cálculo do caminho mínimo existente entre um vértice de origem e um de destino
# em um grafo com pesos nas suas arestas.
# Para a implementação, consideraremos que as rotas entre as cidades serão representadas por dois grafos direcionados,
# um representando os caminhos existentes através de ônibus e outro representando os caminhos existentes através de
# avião. Caso a entrada indique T = 0, as arestas e seus respectivos pesos são armazenados em grafo_onibus. Caso
# T = 1, em grafo_aviao. Uma vez que os grafos estão montados, eles são passados à função dijkstra para o cálculo
# do caminho mínimo. Inicialmente, atribui-se que o custo para atingir cada vértice é infinito, pois não se
# tem conhecimento do mesmo. Aquele necessário para atingir o vértice 1 (origem) é igual a zero, afinal,
# não há custo para o ponto de partida. Feitas estas configurações iniciais, passa-se o
# peso (0) e o vértice de origem (1) para a fila de prioridades. Enquanto esta fila não estiver vazia, busca-se
# pelo menor gasto para atingir cada vértice, até se chegar naquele de destino. Primeiro, retira-se o item
# da lista que possui menor peso. Verifica-se então se o custo para atingir este vértice é maior do que aquele
# já armazenado. Em caso afirmativo, sabe-se que já estamos em posse do menor custo para atingir aquele vértice e
# a verificação seguinte é pulada através do comando continue. Caso contrário, são percorridas as conexões do vértice
# em questão, tal como o custo que se tem para atingir cada uma delas. Se o gasto até o vértice atual somado ao
# peso para atingir a conexão em análise for menor do que aquele armazenado no vetor de gastos na posição referente
# à conexão, temos um novo gasto mínimo, a qual é armazenado no vetor de gastos. Esse custo, tal como
# o vértice em questão (conexao em análise) é inserido na fila de prioridade. A partir de então, o código se repete
# até que a fila de prioridades esteja vazia, conforme mencionado. Uma vez finalizada a execução,
# a menor distância é retornada.
# Como citado anteriormente, a função dijkstra é chamada para o grafo que representa as rotas de ônibus e para aquele
# que representa as rotas de aviao. Os retornos são comparados através da função min() e o menor valor é impresso como o
# custo mínimo necessário para ir de 1 até N.
# Os casos de teste são lidos até que seja encontrado o fim do arquivo, o qual dispara uma exeção EOFError, capturada
# pela cláusula except (linha 81) que interrompe a execução do programa. 
# ***************************************************************************************************************

from heapq import heappush, heappop
import math


def dijkstra(grafo, n_vertices):

    visitados = set()
    fila_prioridade = []
    gastos = [math.inf for i in range(n_vertices + 1)]
    gastos[1] = 0
    # não há custo para atingir a origem
    heappush(fila_prioridade, (0, 1))

    while fila_prioridade:
        peso, vertice = heappop(fila_prioridade)

        if peso > gastos[vertice]:
            continue  # Não vale a pena realizar a verificação, afinal, já existe um caminho menor.

        for conexao, peso_at in grafo[vertice]:
            if gastos[vertice] + peso_at < gastos[conexao]:
                gastos[conexao] = gastos[vertice] + peso_at
                heappush(fila_prioridade, [gastos[conexao], conexao])
                visitados.add(vertice)


    return gastos[n_vertices]


while True:
    try:
        n_cidades, n_trechos = map(int, input().split())

        grafo_onibus = [[] for i in range(n_cidades + 1)]
        grafo_aviao = [[] for i in range(n_cidades + 1)]

        for j in range(n_trechos):
            partida, chegada, veiculo, peso = map(int, input().split())
            if veiculo == 0:
                grafo_onibus[partida].append([chegada, peso])
            elif veiculo == 1:
                grafo_aviao[partida].append([chegada, peso])

        custo_aviao, custo_onibus = dijkstra(grafo_aviao, n_cidades), dijkstra(grafo_onibus, n_cidades)
        print(min(custo_aviao, custo_onibus))


    except EOFError:
        break

