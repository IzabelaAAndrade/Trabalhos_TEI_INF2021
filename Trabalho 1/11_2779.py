# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do Código: O programa em questão recebe o número de espaços existentes em um álbum de 
# figurinhas e, através do número de figurinhas compradas, tal como da lista de figurinhas, calcula
# quantas figurinhas ainda são necessárias para completar o álbum. Para tanto, faz-se um laço de 
# repetição o qual recolhe as figurinhas adquiridas, uma por vez, e as coloca em uma lista. Caso 
# a figurinha da vez não esteja na lista, ela é adicionada. Caso contrário, ela é descartada. 
# Ao fim do laço, é impressa a diferença entre o número de espaços do álbum e o tamanho da lista
# obtida. 
# **************************************************************************************************

numero_espacos = int(input())

figurinhas_compradas = int(input())

figurinhas = []

for figurinha in range(figurinhas_compradas):

    figura_atual = int(input())
    
    if figurinhas.count(figura_atual) == 0:
        
        figurinhas.append(figura_atual)


print(numero_espacos - len(figurinhas))
