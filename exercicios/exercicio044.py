## calcule o valor a ser pago por um produto considerando o  seu preço normal e condição de pagamento
# a vista dinheiro/cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Qual é o preço do produto? R$'))

print('='*35)
print('CONDIÇÕES DE PAGAMENTO')
print('='*35)
print('1 - Á vista dinheiro ou cheque')
print('2 - Á vista no cartão de crédito')
print('3 - 2x no cartão de crédito')
print('4 - 3x no cartão de crédito')
print('='*35)
condicao = int(input('Informe a condição de pagamento: '))
apagar = preco

if condicao == 1:
    apagar = preco - (preco * 0.10)
elif condicao == 2:
    apagar = preco - (preco * 0.05)
elif condicao == 3:
    apagar = preco
elif condicao == 4:
    apagar = preco + (preco * 0.2)
else:
    print('Opção inválida!')

print('O Valor final a ser pago pelo produto é R${:.2f}'.format(apagar))
