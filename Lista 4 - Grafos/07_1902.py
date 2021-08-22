# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **********************************************************************************************************
# O código em questão visa determinar a quantidade máxima de casamentos possíveis de acordo com as condições
# do enunciado. Para tal, primeiramente a função dfs é definida. Em seguida temos a inicialização dos
# dicionários que armazenarão as relações a serem definidas na entrada e um dicionário que indicará quais 
# pessoas dessa relação já foram analisadas, respectivamente. Logo depois, temos um loop que lê a entrada 
# até o fim de arquivo e armazena tal entrada no dicionário de relações, no qual a chave indica uma pessoa 
# e o valor indica a pessoa que ela gosta. Simultaneamente, a lista de visitados é inicializada com False. 
# Após isso, temos um for que percorre cada relação na lista de relações, armazenando em uma varíavel o 
# retorno da função dfs que faz a busca de casamentos na relação inicializada.

# A função dfs funciona recebendo o grafo no qual será realizada a busca (relações), o vétice inicial 
# (relação) e a lista de visitados. A função funciona iterativamente para evitar problemas com empilhamento 
# máximo de função recursiva. No início, definimos uma lista que armazenará os visitados especificamente 
# naquela seção. Inicializamos uma lista de vértices a visitar com o própria relação que foi passada 
# inicialmente para a função. O loop funciona enquanto houverem vértices a serem visitados. Definimos o 
# vértice atual na varíavel vertice e verificamos se esse vértice já foi visitado. Em caso positivo, a 
# execução da função para, retornando 0, o que significa que não foi possível formar um casamento na seção 
# em questão. Em caso negativo, ele define o vértice como visitado, o adiciona na lista de visitados na 
# seção, e continua a execução da função, passando para o próximo bloco condicional. Nesse bloco verificamos
# se a pessoa gostada pela pessoa atual já foi visitada e, em caso negativo, ela é adicionada na lista de 
# vértices a visitar. Em caso positivo, ou seja, a pessoa gostada já foi visitada, fazemos outra condição 
# que verifica se a pessoa gostada está na relação atual e se essa relação tem 2 ou mais pessoas. Em caso 
# posivo, encontramos um cilco, o que representa um casamento possível, dessa forma a função retorna 1. Por 
# fim, temos um retorno após o while do valor 0, para que, quando os vértices a visitar acabarem sem que um
# casamento seja encontrado, tal seja retornado para a soma de casamentos. No final, a variável casamentos 
# é impressa, informando a quantidade de casamentos que é possível formar.
# **********************************************************************************************************

def dfs(grafo, vertice, visitados):
    
    visitados_na_secao = []

    vertices_visitar = [vertice]

    while vertices_visitar:

        vertice = vertices_visitar.pop()

        if not visitados[vertice]:

            visitados[vertice] = True
            visitados_na_secao.append(vertice)

            if not visitados[grafo[vertice]]:
                vertices_visitar.append(grafo[vertice])
            elif grafo[vertice] in visitados_na_secao and len(visitados_na_secao) >= 2: return 1

        else: return 0
    return 0

relacoes, visitados = {}, {}

while True:
    try:
        e = input().split()
        relacoes[e[0]] = e[1]
        visitados[e[0]] = False

    except:
        break

casamentos = 0

for relacao in relacoes:
    casamentos += dfs(relacoes, relacao, visitados)

print(casamentos)
