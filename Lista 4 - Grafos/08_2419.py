# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***********************************************************************************************************
# O presente código lê a quantidade de linhas e colunas do mapa (m e n) e logo em seguida lê o mapa em si.
# Na mesma lista onde é armazenado o mapa, são acrecentados pontos em sua borda para facilitar a comparação
# que é feita posteriormente, evitando a acesso de uma posição inexistente da lista. No segundo for é feita
# a contagem de costas analisando se existe pelo menos um ponto nas proximidades da terra (#), indicando que
# há água nas proximidades. Por fim, essa quantidade é impressa.
# ***********************************************************************************************************

m, n = map(int, input().split())

mapa = [['.'] * (n + 2)]

for i in range(m):
    mapa.append(list('.' + input() + '.'))

mapa.append(['.'] * (n + 2))

costa = 0

for i in range(m + 1):
    for j in range(n + 1):
        if mapa[i][j] == '#' and (mapa[i+1][j] == '.' or mapa[i-1][j] == '.' or mapa[i][j+1] == '.' or mapa[i][j-1] == '.'):
            costa += 1

print(costa)
