# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: O código lê a quantidade de casos de teste que o usuário deseja executar, em
# seguida ele entra em um for, para cada string dada irá tirar a areia (pontos - ".") e verificar a
# existência de diamantes ("<>"). Assim, enquanto houver diamantes, ele os contabiliza, retira da
# sequência e repete o processo. Ao final ele imprime a quantidade de diamantes encontrados.
# **************************************************************************************************

n = int(input())

for c in range(n):
    mina = input().replace(".", "")
    q = 0

    while mina.count("<>") > 0:
        q += mina.count("<>")
        mina = mina.replace("<>", "")
    
    print(q)
