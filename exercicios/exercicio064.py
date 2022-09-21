#leia vários números inteiros. o programa só vai parar quando digitar 999
# no final mostre quantos números foram digitados e a soma entre eles. menos o 999
num = 0
contagem = 0
total = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        total += num
        contagem += 1
print('Foram digitals {} números e seu total é {}'.format(contagem, total))



