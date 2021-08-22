# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# ***********************************************************************************************************
# Em primeiro lugar, o seguinte código lê a largura (l) e a altura (a) do mapa a ser introduzido. Com tais
# valores, um for lê cada uma das linhas da entrada, armazenando elas em forma de sublista dentro da lista 
# mapa. Ao mesmo tempo é inicializada uma lista que corresponde às posições já visitadas do mapa, que,
# inicialmente é preenchida com False. A segunda parte do código percorre o mapa conforme a direção atual. 
# Essa direção é definida no primeiro bloco condicional, no qual, caso a linha e coluna (que inicialmente 
# são 0) indiquem uma posição que não seja o tesouro (*) nem um ponto (.), é feita a atualização da variável 
# que indica a direção. O próximo bloco condicional verifica se a posição atual já foi visitada. Em caso 
# afirmativo, a repetição é quebrada com uma saída que indica que não foi possível encontrar o tesouro. O 
# último bloco condicional avança a posição do mapa conforme a direção atual. Por fim, todo esse laço de 
# repetição está dentro de um bloco try, o qual verifica uma tentativa de acesso fora dos limites do mapa, o 
# que também indica que não é possível encontrar o tesouro através dele. Finalmente a variável saida é 
# impressa, indicando se foi possível ou não encontrar o tesouro.
# ***********************************************************************************************************

l, a = int(input()), int(input())

mapa, visitados = [], []

for i in range(a):
    mapa.append(list(input()))
    visitados.append([False] * l)

linha, coluna = 0, 0

try:
    while True:
        if mapa[linha][coluna] == '*':
            saida = '*'
            break
        elif mapa[linha][coluna] != '.': direcao = mapa[linha][coluna]
        
        if not visitados[linha][coluna]: visitados[linha][coluna] = True
        else:
            saida = '!'
            break

        if direcao == '>': coluna += 1
        elif direcao == '<': coluna -= 1
        elif direcao == 'v': linha += 1
        else: linha -= 1

except IndexError:
    saida = '!'

print(saida)
