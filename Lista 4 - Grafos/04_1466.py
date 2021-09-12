# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# O problema em questão trata da busca em largura em uma arvore binaria de busca. Esse tipo de arvore
# segue alguns principios para a sua construcao: todos os nodos a direita de de um devem ser maiores do que
# ele (ou iguais) e todos os nodos a esquerda devem ser menores (ou iguais). Portanto, o nosso primeiro problema
# e como montar a arvore a partir da entrada. Apos a leitura, e definido a raiz, que consiste do primeiro valor.
# A partir dela, os outros valores sao inseridos seguindo as regras expostas anteriormente. Para tanto, foi
# criado uma classe que represanto um nodo. Ela tera a referencia dos proximos dois, a direita e a esquerda.
# A funcao inserir, coloca o valor atual do for (que percorre a entrada) no lugar correto da arvore. Apos a
# construcao da estrutura, nos percorremos a arvore com um algoritmo adaptado de busca em largura. Dentro do
# algoritmo, a ordem de visita e armazena em uma lista e retornada ao final. Essa ordem é a resposta do
# blema.
# **********************************************************************************************************

from collections import deque

def bfs(nodo):

    ordem = []
    para_visitar = deque()
    para_visitar.appendleft(nodo)

    while para_visitar:

        nodo = para_visitar.pop()
        ordem.append(nodo.valor)
        
        if nodo.esquerda is not None:

            if nodo.esquerda.valor not in ordem:

                para_visitar.appendleft(nodo.esquerda)
        
        if nodo.direita is not None:

            if nodo.direita.valor not in ordem:

                para_visitar.appendleft(nodo.direita)

    return ordem


def inserir(nodo, valor):

    if nodo.valor < valor:

        if nodo.direita is None:

            nodo.direita = Nodo(valor)
        
        else:

            inserir(nodo.direita, valor)
    
    if nodo.valor > valor:

        if nodo.esquerda is None:

            nodo.esquerda = Nodo(valor)

        else:

            inserir(nodo.esquerda, valor)

class Nodo:

    def __init__(self, valor=None, esquerda=None, direita=None):
        
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

casos = int(input())

for caso in range(casos):

    quant_numeros = int(input())

    valores = map(int, input().split())

    for posicao, val in enumerate(valores):

        if posicao == 0:

            raiz = Nodo(val)
        
        else:
            
            inserir(raiz, val)

    ordem = bfs(raiz)

    print("Case " + str(caso+1) + ":")
    print(" ".join(map(str, ordem)))
    print()
