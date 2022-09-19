#refaça o exercicio 035 dos triangulos
# informar também:
# equilatero: todos os lados iguais
# isoceles = dois lados iguais
# escaleno = todos os lados diferentes

# desafio 35
# Leia o comprimento de tres retas e diga ao usuario se
# elas podem ou não formar um triângulo.
import math
r1 = float(input('Tamanho da reta 1: '))
r2 = float(input('Tamanho da reta 2: '))
r3 = float(input('Tamanho da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    tipo = 'escaleno' # todas as retas com tamanhos diferentes
    if r1 == r2 and r1 == r3:
        tipo = 'equilátero' # todas as retas tem o mesmo tamanho
    elif r1 == r2 or r1 ==r3 or r2 == r3:
        tipo = 'isóceles' # duas retas tem o mesmo tamanho

    print('A retas podem formar um triãngulo {}.'.format(tipo))

else:
    print('As retas não podem formar um triângulo')