# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão nos permite identificar, dada uma espécie de analógimôn, o mínimo
# número de espécies que são direta ou indiretamente do mesmo tipo dela. Para tanto, foi utilizada a técnica de
# busca em profundidade (dfs). Considera-se cada espécie como um vértice de um grafo não direcionado. A medida que
# são recebidas as entradas que apresentam espécies do mesmo tipo, o grafo, montado através de uma lista de adja
# cências, é preenchido. As arestas são ligadas em ambos os sentidos, uma vez que o grafo não é direcionado.
# Finalizada a construção do grafo, recebe-se a espécie da qual se deseja realizar a consulta. Esta espécie,
# tal como o grafo, são passados à função dfs_iterativa a qual percorre todos os vértices possíveis de se alcançar
# através daquele que representa a espécie de consulta. Para tanto, utilizam-se duas listas do tipo set(), as quais
# armazenam os vértices que ainda precisam ser visitados e os que já foram visitados. Enquanto a lista de vértices
# a serem visitados não estiver vazia, utiliza-se de um laço de repetição para remover da mesma um vértice por vez
# e então analisar suas conexões. Caso essas não tenham sido visitadas, elas são inseridas na lista de vértices
# a serem visitados. Inicialmente, a lista de vértices não visitados contém apenas o vértice que representa a espécie
# de consulta, mas esta situação pode ser modificada ao longo do processo de execução da função e do laço de repetição
# em seu interior.
# Ao fim da execução do laço, é retornado o tamanho da lista de vértices visitados, indicando o número de espécies
# que são do mesmo tipo que aquela de consulta.
# Os casos de teste são lidos até que seja encontrado o fim do arquivo, o qual dispara uma exeção EOFError, capturada
# pela cláusula except (linha 50) que interrompe a execução do programa.
# ***************************************************************************************************************

def dfs_iterativa(grafo, v):
    visitados = set()
    a_visitar = set()
    a_visitar.add(v)
    while a_visitar:
        vertice_atual = a_visitar.pop()
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            for conexao in grafo[vertice_atual]:
                if conexao not in visitados:
                    a_visitar.add(conexao)

    return len(visitados)


while True:
    try:
        numero_especies, numero_infos = map(int, input().split())
        grafo = [[] for especie in range(numero_especies + 1)]
        for i in range(numero_infos):
            especie1, especie2 = map(int, input().split())
            grafo[especie1].append(especie2)
            grafo[especie2].append(especie1)
        minha_especie = int(input())
        print(dfs_iterativa(grafo, minha_especie))
    except EOFError:
        break
