# leia um número qualquer e mostre seu fatorial.
num = int(input('Digite um número: '))
print('Fatorial do número {}'.format(num))
fatorial = 1
controle = num
while controle != 0:
    fatorial = fatorial * controle
    print('{}'.format(controle), end=' ')
    controle -= 1
print('\nO fatorial de {} é: {} '.format(num, fatorial))

