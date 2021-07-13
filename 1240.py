# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do Código: O seguinte código armazena a quantidade de casos de teste e, por meio de um
# for, lê e compara dois valores. É feita uma seleção de caracteres do primeiro valor lido na qual
# o seu final será comparado ao segundo valor (a partir da posição que correponde à diferença do tamanho
# das duas cadeias de caracteres). Assim, caso essa comparação seja verdadeira, a segunda cadeia está
# contida no final da primeira. 
# **************************************************************************************************

casos = int(input())

for caso in range(casos):

    valor1, valor2 = input().split()

    if valor1[len(valor1)-len(valor2):] == valor2:

        print("encaixa")

    else:

        print("nao encaixa")
