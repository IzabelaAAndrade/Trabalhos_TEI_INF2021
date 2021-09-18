# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão nos permite calcular, dentre um conjunto de aeroportos, aqueles que
# terão maior congestionamento no futuro. Para tanto, conforme o enunciado, deve-se levar em consideração o número
# de voos que partem ou chegam a um aeroporto. Para fazer a implementação da solução, será utilizada uma matriz ou
# uma lista de listas (circulacao_aeroportos). Essa terá como tamanho o número de aeroportos + 1, de modo que cada
# posição de 1 até o número de aeroportos represente um aeroporto.
# Inicialmente, cada posição da lista circulacao_aeroportos possui um array com os valores [0,0].
# Cada vez que se lê um voo, a posição da lista que contém aquele aeroporto recebe como valor um vetor de duas posições,
# sendo a primeira posição o índice do aeroporto (para que quando a ordenação da lista seja feita, não se perca o
# índice de cada aeroporto) e a segunda, o número de voos que chegam ou partem daquele aeroporto (fator de ordenação).
# Este último valor é incrementado sempre que um aeroporto é lido, seja como um local de partida ou destino.
# Ao fim do recebimento de todos os voos, realiza-se a ordenação (em ordem decrescente) da lista de listas
# que representa os aeroportos e os voos que passam por eles. Para tanto, usa-se a função sort(), adotando
# como parâmetro o segundo item das listas que compõem cada posição da matriz, ou seja, os voos que passam por
# cada aeroporto. Ademais, faz-se com que o parâmetro reverse da função seja igual a True.
# Para a saída, faz-se a impressão dos índices dos aeroportos que possuem mais voos partindo ou chegando
# em si. Para tanto, utiliza-se de um laço de repetição que imprime o índice do aeroporto armazenado na
# primeira posição da lista de
# listas pois o aeroporto em questão necessariamente conterá o maior numero de voos, afinal, a lista
# foi ordenada em ordem decrescente conforme a quantidade dos voos. Caso a posição seguinte da matriz contenha
# um número de voos igual ao da primeira posição, ou seja, igual ao maior número de voos que passa por um ou mais
# aeroportos, a iteração continua e o índice do aeroporto da posição em questão é impresso, caso contrário,
# a execução do laço é interrompida e um novo caso de teste é iniciado.
# ***************************************************************************************************************
caso = 1
while True:
    n_aeroportos, n_voos = map(int, input().split())
    if n_aeroportos == 0 and n_voos == 0:
        break

    circulacao_aeroportos = [[0,0] for i in range(n_aeroportos + 1)]
    for voo in range(n_voos):
        partida, destino = map(int, input().split())
        circulacao_aeroportos[partida] = [partida, circulacao_aeroportos[partida][1] + 1]
        circulacao_aeroportos[destino] = [destino, circulacao_aeroportos[destino][1] + 1]
    circulacao_aeroportos.sort(key=lambda ajuste: ajuste[1], reverse=True)
    maior_c = circulacao_aeroportos[0][1]
    print("Teste {0}".format(caso))
    for i in range(n_aeroportos):
        print(circulacao_aeroportos[i][0], end=" ")
        if circulacao_aeroportos[i + 1][1] != maior_c:
            break
    print()
    print()
    caso += 1

