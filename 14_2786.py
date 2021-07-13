# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: O código em questão permite o cálculo do número de lajotas do tipo 1 e 2
# necessárias para compor o piso de uma dada sala. Como as diagonais das lajotas do tipo 1 deverão estar alinhadas
# com as laterais da sala, percebe-se que serão necessárias L*C + (L-1 * C-1) lajotas de tal categoria. L*C para
# as "extremidades" e L-1 * C-1 para os espaços deixados entre elas. Como o ainda existem
# buracos nas laterais da sala, é necessário preenche-los com lajotas dos tipos 2 e 3. Cada vértice da sala
# é preenchido por uma lajota do tipo 3, que tem tamanho igual à metade daquelas de tipo 2, fazendo com que seja
# possível concluir que serão necessárias (L-1)*2 + (C-1)*2 lajotas do tipo 2, ou seja,o tamanho de cada lado da
# sala menos 1 (pois já preenchemos este valor com as lajotas do tipo 3).
# **************************************************************************************************

largura = int(input())
comprimento = int(input())

tipo1 = largura*comprimento + ((largura-1)*(comprimento-1))
tipo2 = (largura-1)*2+(comprimento-1)*2

print(tipo1)
print(tipo2)
