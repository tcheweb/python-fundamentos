#Crie um programa que vai ler vários números e colocar em uma lista.
#depois disso, mostre:
#a) Quantos números foram digitados;
#b) A lista de valores ordenada de forma decrescente.
#c) e se o valor 5 foi digitado e está ou não na lista
numeros = list()
while True:
    numeros.append(int(input('Digite o número: ')))
    if numeros[len(numeros)-1] == 0:
        numeros.pop()
        print(f'Foram digitados {len(numeros)} números.')
        numeros.sort(reverse=True)
        print(f'Números digitados em ordem decrescente: {numeros}')
        print('O valor 5 foi digitado' if 5 in numeros  else 'Não encontrei o número 5')
        break