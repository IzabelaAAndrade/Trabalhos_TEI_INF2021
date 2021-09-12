# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão realiza a fusão de bancos através de seus códigos, tal como verifica
# se dois códigos bancários se referem a um mesmo banco. Para tanto, implementa-se uma técnica de ranked union find.
# Cria-se um vetor o qual tem o número de bancos + 1 posições para representar os bancos e seus códigos, ademais,
# cria-se um array para representar o tamanho da árvore que representa cada banco e o número de bancos a ele fundidos.
# Em ambos os casos, O índice do vetor indica o código do banco. Inicialmente, cada posição do array que representa
# os bancos tem um valor distinto (igual ao seu índice), indicando que não existe fusão entre nenhum dos bancos. O array
# que indica as árvores tem, no ínicio, todas as suas posições zeradas, uma vez que não há bancos fundidos, ou seja,
# nenhuma das árvores tem algum item a elas ligado.
#
# Para cada consulta ou fusão é chamada a função find_root ou
# "encontra raiz", responsável por encontrar o banco do qual derivam todos os outros que foram fundidos direta ou
# indiretamente a partir dele. Para tanto, utiliza-se de recursão para encontrar o banco que faz referência a si
# próprio, ou seja, cujo índice (código) seja igual ao conteúdo referente a ele (banco). Caso essa condição não seja
# atendida, a função é chamada até que o valor seja encontrado. Ao longo destas chamadas recursivas, adota-se a técnica
# de path-compression, na qual se inserem "cortes de caminho" entre bancos fundidos, de modo que a cada vez que o método
# find_root é chamado, o banco raíz é associado à todos aqueles percorridos ao longo do caminho de busca pelo mesmo.
#
# Uma vez encontrados os bancos raízes referentes aos códigos inseridos, pode-se realizar tanto a fusão quanto a
# consulta. A fusão tem como base a função "union", a qual une as árvores que representam os conjuntos de bancos
# fundidos. De modo a deixar o código mais efetivo, a união das árvores é feita de modo que as de menor tamanho sejam
# inseridas no fim daquelas de maior tamanho. Para tanto, são comparados os tamanhos das árvores de acordo com suas
# raízes (encontradas anteriormente através da função find_root). Cada vez que uma árvore é adicionada à outra,
# o tamanho desta outra árvore se torna o seu somado do da árvore que lhe foi acrescida.
# A consulta, que diz respeito
# a verificar se dois bancos foram fundidos, simplesmente se baseia na comparação entre as raízes dos bancos cujos
# códigos estão sendo consultados. Caso as raízes sejam as mesmas, os bancos estão dentro do mesmo conjunto e foram
# fundidos.
#
# ***************************************************************************************************************

numero_bancos, numero_consultas = map(int, input().split())

bancos = []
tamanho_arvore = [0]*(numero_bancos+1)

def find_root(cod):
    global bancos
    if bancos[cod] != cod:
        bancos[cod] = find_root(bancos[cod])

    return bancos[cod]


def union(raiz1, raiz2):
    # Juntar a arvore menor na maior
    if raiz1 != raiz2:
        if tamanho_arvore[raiz1] < tamanho_arvore[raiz2]:
          bancos[raiz1] = raiz2
          tamanho_arvore[raiz1] += tamanho_arvore[raiz2] + 1
        else:
            bancos[raiz2] = raiz1
            tamanho_arvore[raiz2] += tamanho_arvore[raiz1] + 1


for i in range(numero_bancos+1):
    bancos.append(i)

for consulta in range(numero_consultas):
    operacao, cod1, cod2 = input().split()
    cod1, cod2 = int(cod1), int(cod2)
    raiz1, raiz2 = find_root(cod1), find_root(cod2)
    if operacao == 'F':
        # Realizar a união
        union(raiz1, raiz2)
    elif operacao == 'C':
        # Realizar a busca e verificar se estão na mesma componente
        if raiz1 == raiz2:
            print("S")
        else:
            print("N")

