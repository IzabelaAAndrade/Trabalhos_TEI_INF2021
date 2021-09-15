# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***************************************************************************************************************
# Descrição do código: O código em questão verifica se é possível sair de um bairro e chegar em outro a partir
# das conexões dadas entre os mesmos. De modo a implementar tal lógica, foi utilizado um algoritmo de ranked union
# find com path compression, o qual nos permite verificar se dois vértices de um grafo estão ou não na mesma componente
# conexa, tal como associar duas componentes. Inicialmente, criam-se dois vetores, ambos com o número de bairros + 1
# posições os quais representarão os bairros e o tamanho das árvores/componentes conexas nas quais cada um se situa.
# No começo, o vetor bairros terá cada posição igualada ao índice da mesma, afinal, ainda não se sabe quais bairros
# são unidos. Cada vez que se tem a informação de que dois bairros são conectados, chama-se a função find_root para
# os mesmos. De tal modo, é possível encontrar o vértice raíz ou bairro raiz da componente conexa, ou seja, aquele
# que tem, no vetor bairros, a posição igual ao índice do vetor. As raizes retornadas pela função find_root são passadas
# à função union, que realiza a união dos dois bairros em questão, através da união das componentes conexas ou árvores
# em que eles se situam. Verifica-se primeiro qual das raizes possui menor árvore, para que esta possa ser ligada
# à maior. Então, realiza-se a ligação e a árvore formada terá como tamanho a soma do tamanho daquelas que
# a originaram. 
# Para cada consulta relacionada à possibilidade de ir de um bairro à outro, é chamada a função find_root para os
# dois bairros ou vértices. Caso eles possuam as mesmas raízes, pode-se concluir que eles estão na mesma componente
# conexa e estão conectados direta ou indiretamente. Caso contrário, eles não estão conectados e não é possível atingir
# um bairro a partir do outro. 
# Verifica-se o uso da técnica de path compression em find_root nas chamadas recursivas da mesma, de modo associar
# cada posição do vetor bairros visitada durante a consulta diretamente à raiz, facilitando consultas futuras. 
# ***************************************************************************************************************


bairros = []

def union(r1, r2):
    global bairros, tam_arvore
    if tam_arvore[r1] < tam_arvore[r2]:
        bairros[r1] = r2
        tam_arvore[r1] += tam_arvore[r2]
    else:
        bairros[r2] = r1
        tam_arvore[r2] += tam_arvore[r1]

def find_root(v):
    global bairros
    if v != bairros[v]:
        bairros[v] = find_root(bairros[v])
    return bairros[v]

nbairros, conexoes, perguntas = map(int, input().split())
tam_arvore = [1] * (nbairros + 1)
for i in range(nbairros + 1):
    bairros.append(i)
for i in range(conexoes):
    b1, b2 = map(int, input().split())
    r1, r2 = find_root(b1), find_root(b2)
    union(r1, r2)
for i in range(perguntas):
    bc1, bc2 = map(int, input().split())
    cr1, cr2 = find_root(bc1), find_root(bc2)
    if cr1 == cr2:
        print("Lets que lets")
    else:
        print("Deu ruim")
