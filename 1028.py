# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: De modo a permitir o cálculo do tamanho máximo das pilhas de figurinhas foi
# criada uma função que calcula o Máximo Divisor Comum (MDC) de cada par de valores. Tal
# função tem como base o método da "Grade de Euclides", estudado em anos anteriores pelas alunas.
# Utiliza-se dos valores passados à função para realizar uma sequência de divisões, a qual se inicia
# com os valores recebidos e então o menor destes valores e o resto da divisão. O processo se mantém
# até que seja encontrado o último resto não nulo. Este valor será o MDC, e, consequentemente, o
# tamanho máximo das pilhas de figurinhas.
# **************************************************************************************************

def mdc(numero1, numero2):

    maior = max(numero1, numero2)
    menor = min(numero1, numero2)

    while maior % menor != 0:

        maior, menor = menor, maior % menor

    return menor


casos = int(input())

for caso in range(casos):

    amigo1, amigo2 = [int(val) for val in input().split()]

    print(mdc(amigo1, amigo2))
