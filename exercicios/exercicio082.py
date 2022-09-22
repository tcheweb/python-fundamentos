#Crie um programa que vai ler vários números e colocar em uma lista
# depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente
# ao final mostre o conteúdo das três listas geradas.
numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    if numeros[len(numeros)-1] == 0:
        numeros.pop()
        print(f'A lista contem estes valores: {numeros}')
        print(f'Separando pares de impares.')
        for num in numeros:
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
        break
print(f'Pares: {pares}')
print(f'Impares: {impares}')
