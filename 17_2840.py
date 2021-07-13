# Alunas: Izabela A. Andrade (20192004795), Marcela P. Silvério (20192020028) e Tássyla L. Lima (20192001990)
# Turma: INF3A

# **************************************************************************************************
# Descrição do código: O código aqui apresentado calcula o número máximo de balões que podem ser enchidos
# com uma dada quantidade de gás hélio. Para tanto, é necessário calcular o volume dos balões e então dividir
# a quantia de gás disponível por por ele. Como o enunciado afirma que os balões tem formato esférico e o
# usuário digita o raio da esfera que compõe o balão, é possível calcular o volume desejado através da
# fórmula (4 * pi * r ^ 3)/3. Com essse valor em mãos, efetuamos o calculo da divisão mencionada, arredondando
# o resultado para baixo, através da função math.floor().
# **************************************************************************************************
import math

valores = [int(val) for val in input().split()]

baloes = valores[1]/((4 * 3.1415 * (valores[0]**3))/3)

print(math.floor(baloes))