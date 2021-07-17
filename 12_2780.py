# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do Código: O código recebe o valor da distância correspondente a posição de um robô em
# relação ao início de uma quadra de basquete. Dependendo dessa variável, nós imprimimos a quantidade
# de pontos que uma cesta feita nessa distância corresponde.
# **************************************************************************************************


distancia = int(input())

if distancia <= 800:

    print(1)

elif distancia <= 1400:

    print(2)

else:

    print(3)
