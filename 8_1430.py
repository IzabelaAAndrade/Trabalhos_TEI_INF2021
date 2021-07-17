# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do Código: O seguinte programa recebe uma string que representa uma composição. Ela é
# divida em compassos, sendo que cada um é composto de notas. Cada uma dessas notas possui uma
# duração. O código a seguir calcula quantos compassos possui a duração total igual a um. Para isso,
# o código divide a string composição em um vetor de compassos através de um comando split. Esse vetor
# é percorrido através de um for. Dentro desse for, nós iteramos sobre cada uma das notas e calculamos
# a soma total da duração através de um dicionário que contém o valor de cada uma delas. No final, é
# apresentado na tela o número total de compassos com a duração correta.
# **************************************************************************************************


notas = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

while(True):

    composicao = input().split('/')

    if composicao[0] == '*':

        break

    else:

        soma = 0
        correto = 0

        composicao.pop(0)

        for compasso in composicao:

            for nota in compasso:

                soma += notas[nota]

            if soma == 1:

                correto += 1

            soma = 0

        print(correto)
