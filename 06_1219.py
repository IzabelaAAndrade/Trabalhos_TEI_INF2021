# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: O código em questão calcula as áreas destinadas ao plantio de três tipos de
# flores (sunflowers, violets e roses), conforme a geometria do jardim esperado. Verifica-se que a
# área voltada ao cultivo de violetas e rosas corresponde à área de um triângulo cujos lados são disponibilizados
# pelo programa. Tal área pode ser calculada pela fórmula de Heron, que a associa com os lados do triângulo
# e seu semiperímetro: S = sqrt(p * (p - a) * (p - b) * (p - c)). Uma vez calculada a área do triângulo, podemos
# utilizá-la para calcular o raio da circunferência referente ao plantio de rosas, circunscrita ao espaço das
# triângulo que contém as áreas de plantio de rosas e violetas. Pode-se dividir o triângulo em 3, sendo a área
# total recalculada por (a * r)/2 + (b * r)/2 + (c * r)/2. Como a área do triângulo maior já havia sido calculada,
# podemos reorganizar a equação, de modo a encontrar o raio: r = (a * b * c)/2. Em posse deste raio é possível
# calcular a área referente às rosas pela fórmula da área da circunferência Ac = pi * (raio ** 2). A área destinada
# às violetas poderá então ser calculada pela subtração da área de rosas da área do triângulo. Por fim, resta
# calcular a área ocupada pelos girassóis. Pode-se utilizar da lei dos senos para encontrar uma fórmula que
# descreve a associação entre a área do triângulo inscrito na circunferência do jardim e seu raio, que é
# raio = (a * b * c)/4 * S, sendo S a área do triângulo. Em posse deste raio, pode-se
# calcular a área total do jardim pela fórmula da área da circunferência, apresentada anteriormente.
# Finalmente, para encontrar a área ocupada pelos girassois, basta subtrair a área do triângulo da área total do
# jardim. Em posse de todas as áreas, resta formatar a saída usando a função "format" para que os valores
# exibam apenas 4 casas decimais.
# **************************************************************************************************
import math

while True:
  try:

    # Medidas Triangulo
    lados_triangulo = [int(val) for val in input().split()]
    semiperimetro_triangulo = sum(lados_triangulo)/2
    lados_multiplicados = 1

    for lado in lados_triangulo:
      lados_multiplicados *= lado

    # Triangulo
    area_triangulo = math.sqrt(semiperimetro_triangulo*(semiperimetro_triangulo-lados_triangulo[0])*(semiperimetro_triangulo-lados_triangulo[1])*(semiperimetro_triangulo-lados_triangulo[2]))

    # Rosas - circunferência inscrita no triângulo
    raio_rosas = area_triangulo/semiperimetro_triangulo
    rosas = math.pi*(raio_rosas**2)

    # Violetas - área do triângulo subtraida da área da circunferência nele inscrita
    violetas = area_triangulo - rosas

    # Sunflowers - área da circunferência circunscrita ao triângulo subtraida da área do triângulo
    raio_jardim = lados_multiplicados / (4 * area_triangulo)
    area_total_jardim = math.pi * (raio_jardim ** 2)
    sunflowers = area_total_jardim - area_triangulo
    print("{0:.4f} {1:.4f} {2:.4f}".format(sunflowers, violetas, rosas))

  except EOFError:
    break
