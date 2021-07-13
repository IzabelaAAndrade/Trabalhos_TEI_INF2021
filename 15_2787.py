# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: O código em questão permite definir a cor da posição mais à direita e mais à
# baixo de um tabuleiro de xadres. Conforme as regras, a primeira posição (mais à esquerda e mais à
# cima) é sempre branca e as posições subsequentes são alternadas entre preto e branco, respectivamente.
# Tendo a primeira posição da primeira linha (branca) como referência, sabemos que a próxima ocorrência branca somente
# ocorrerá a cada 2 casas, ou seja, sempre nas casas ímpares nesta linha: 1, 2, 5 e assim sucessivamente,
# até o valor mais à direita. Ao alcançá-lo, podemos efetuar a mesma lógica, contudo, na vertical. Caso a Largura e o
# comprimento do tabuleiro sejam ambos pares ou ambos ímpares, tem-se que sua soma menos 1 (para não contar o quadrado
# mais superior à direita duas vezes), ou seja, o caminho preenchido até a posição a ser calculada, é ímpar.
# Como consequência, pela lógica anteriormente apresentada, tal casa é branca. Caso os valores sejam de paridades
# diferentes, o caminho até a última posição será par, fazendo com que a casa seja preta.
# **************************************************************************************************


largura = int(input())
comprimento = int(input())

if (largura % 2 == 0 and comprimento % 2 == 0) or (largura % 2 != 0 and comprimento % 2 != 0):
    print(1)
else:
    print(0)
