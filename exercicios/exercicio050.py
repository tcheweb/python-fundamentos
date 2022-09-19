#Leia seis números inteiros e mostre a soma apenas daqueles que foram pares. Se for impar desconsiderar
soma = 0
for c in range(1,7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos pares é: {}'.format(soma))


