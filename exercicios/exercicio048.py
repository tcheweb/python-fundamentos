# calcule a soma entre todos os números impares que são multiplos de 3 e que se encontram
# entre 1 até 500
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
print('O total da soma dos números ímpares múltiplos por 3 é: {}'.format(soma))
