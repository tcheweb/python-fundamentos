# Leia vários numeros int pelo teclado
# o programa só vai parar quando o valor 999
#no final mostre quantos n. foram digitados e a soma entre eles sem a flag
num = quant = soma = 0
while True:
    num = int(input('Digite o número: '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'{quant} números foram digitados e a soma deles é {soma}')
