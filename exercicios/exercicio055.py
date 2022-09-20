# Leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso

maispesado = 0
maisleve = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if peso >= maispesado:
        maispesado = peso
        if maisleve == 0:
            maisleve = peso
    elif peso < maisleve:
        maisleve = peso
print('A pessoa mais pesada pesa {:.1f}Kg'.format(maispesado))
print('A pessoa mais leve pesa {}Kg'.format(maisleve))

