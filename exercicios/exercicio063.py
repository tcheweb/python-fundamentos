#leia um número inteiro e mostre na tela  os n primeiros elementos de uma sequencia de fibonacci.
print('SEQUÊNCIA DE FIBONACCI')
quantos = int(input('quantos termos quer mostrar? '))
num1 = 0
num2 = 1
controle = 3
print('{} -> {}'.format(num1, num2), end='')
while controle <= quantos:
    fibo = num1 + num2
    print(' -> {}'.format(fibo), end='')
    num1 = num2
    num2 = fibo
    controle += 1