# escreva um programa que leia um numero inteiro e peça para o usuário escolher qual
# será a base de conversão
# 1 - para binario
# 2 - para octal
# 3 - hexadecimal
num = int(input('Digite um número inteiro: '))
print('O número {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
print('O número {} em OCTAL é {}'.format(num, oct(num)[2:]))
print('O número {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
