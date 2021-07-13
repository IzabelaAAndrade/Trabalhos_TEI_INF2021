# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: O código em questão auxilia o papai noel na elaboração de etiquetas de maneira
# eficiente. Através do nome de cada criança e da lingua falada por ela, são geradas etiquetas contendo
# o nome mencionado, tal como uma mensagem de "Feliz Natal" no idioma especificado. Para tanto, foi criado
# um dicionário vazio, o qual foi preenchido com os idiomas (chaves) e as mensagens em cada um deles (valor),
# através de um laço de repetição. Este tinha como parâmetro o número de línguas faladas pelas crianças contempladas.
# Um segundo laço recebe o nome das crianças e a língua falada por elas. Cada nome é impresso, seguido
# pela mensagem no idioma especificado, que é usado como chave para o acesso do dicionario anteriormente citado.
# **************************************************************************************************

lingua_mensagem = {} #dicionário para armazenar países e listas
numero_linguas = int(input())
lingua = ""
crianca = ""

for i in range(numero_linguas):
    lingua = input()
    lingua_mensagem[lingua] = input()


numero_criancas = int(input())

for i in range(numero_criancas):
    print(input())
    print(lingua_mensagem[input()])
    print()
