# mostre a tabuada de vários números
# 1 de cada vez para
# interromper quando digitar um número negativo.
import math
print('TABUADA MASTER')
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print(f'Tabuada do {num}')
    for c in range(1, 11):
        print(f'{num:2} x {c:2} = {num * c}')
print('F I M ')
