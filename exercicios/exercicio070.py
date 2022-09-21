# Leia o nome e preço de cada produto
# perguntar se quer continuar
# qual o total gasto na compra
# quantos produtos custam mais de mil
# qual o nome do produto mais barato
total = 0
menor = 0
quantidade = 0
while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Preço R$ '))
    total += preco
    if preco > 1000:
        quantidade += 1
    if menor == 0:
        menor = preco
    elif preco < menor:
        menor = preco
    opcao = input('Deseja inserir mais produtos: [S/N] ').upper()
    if opcao == 'N':
        print(f'O total gasto foi R$ {total}')
        print(f'Você comprou {quantidade} que custaram mais de R$ 1000.')
        print(f'O produto mais barato custou R$ {menor}')
        break
    else:
        print('='*20)




