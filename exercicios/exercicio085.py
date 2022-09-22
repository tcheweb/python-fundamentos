# Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre numa lista
# que mantenha separados os números pares e impares.
# no final mostre os valores pares e ímpares em ordem crescente.
numeros = list()
pares = list()
impares = list()
for n in range(0,7):
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
numeros.append(pares)
numeros.append(impares)
numeros.sort()
print(f'Os números PARES são: {numeros[0]} e os números IMPARES são: {numeros[1]}')

