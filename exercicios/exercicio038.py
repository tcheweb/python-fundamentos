# leia dois numeros inteiros e compare-os mostrando uma mensagem
# o primeiro valor é maior
#o segundo valor é maior
# não existe valor maior os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 == num2:
    print('Os números são iguais!')
elif num1 > num2:
    print('O primeiro número é maior que o segundo!')
else:
    print('O segundo número é maior que o primeiro!')
