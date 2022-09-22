# crie um progrqama que vai gerar cinco números aleatórios e vai colocar numa tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla
from random import randint
tupla = (randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
#####################################################################
print(f'Os números sorteados foram:', end='')
for c in tupla:
    print(f'{c}', end=' ')

print(f'\nO maior número gerado foi {max(tupla)}')
print(f'e o menor número foi {min(tupla)}')

