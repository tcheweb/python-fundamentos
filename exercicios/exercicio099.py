# faça um programa que tenha uma função maior() que receba vários parâmetros com valores inteiros.
# analisar os valores e informar o maior. retornar quantos falores foram informados e o maior.
#mostrar os valores informados, a quantidade de valores e o maior.

def maior(*num):
    maior = 0
    print(f'Valores informados: ', end='')
    for c in num:
        print(f'{c}', end=' ')
        if c > maior:
            maior = c
    print(f'\nForam informados {len(num)} valores e o maior é {maior} ')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()