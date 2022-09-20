# leia um número qualquer e mostre seu fatorial
num = int(input('Digite um número: '))
print('Calculando {}!'.format(num))
fatorial = 1
controle = num
while controle != 0:
    fatorial = fatorial * controle
    print('{}'.format(controle), end=' ')
    print('x' if controle > 1 else '=', end=' ')
    controle -= 1
print('{}'.format(fatorial))

