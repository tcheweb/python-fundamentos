#faça um programa que tenha uma função chamada contador que receba tres paramtros:
# inicio, fim e passo e realize a contegem.
#seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até zero, de 2 em 2
#c) uma contagem personalizada.
from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio <= fim:
        if passo < 0:
            # Se o número for positivo, torna negativo
            passo *= -1
        for c in range(inicio, fim+1, passo):
            print(f'{c}', end=' ')
            sleep(.5)
        print('\n')
    elif inicio >= fim:
        if passo > 0:
            passo *= -1
        for c in range(inicio, fim-1, passo):
            print(f'{c}', end=' ')
            sleep(.5)
        print('\n')


contador(0, 10, 2)
contador(10, 0, 2)
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)


