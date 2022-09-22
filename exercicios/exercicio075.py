# leia quatro valores pelo teclado e guarde-os numa tupla. No final mostre:
# Quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3 (quando não aparecer, informar que nenhum.
# quais foram os números pares
tupla = (int(input('Valor 1: ')),
           int(input('Valor 2: ')),
           int(input('Valor 3:')),
         int(input('Valor 4: ')))
pares = ''
print(f'Você digitou os números:', end='')
for c in tupla:
    print(c, end=' ')
print(f'\nO número 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) > 0:
    print(f'O número 3 apareceu pela primeira vez na posição {tupla.index(3)+1}')
else:
    print('O número 3 não apareceu nenhuma vez.')
for n in tupla:
    if n % 2 == 0:
        pares = str(pares) + ', ' + str(n)
print(f'Os números pares digitados foram {pares[1:]}')




