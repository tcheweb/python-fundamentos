# refaça o desafio da taboada usando laços

num = int(input('Digite um número para ver sua taboada: '))

for c in range(1, 11):
    print(' {:2} X {:2} = {}'.format(c, num, c*num))
