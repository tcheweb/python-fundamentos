# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos precos
#  no final mostre uma listagem de precos organizando os dados de forma tabular.
produtos = ('Lápis', 3.00, 'Caneta', 2.5, 'Folha de ofício', 12.99, 'Estojo', 9.67)
print('-'*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('-'*30)
print('PRODUTO                  PREÇO')
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<20} R${produtos[c+1]:>7.2f}')

