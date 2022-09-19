# aprovar o emprestimo para a compra de uma casa
# perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# calcular o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou o
# empréstimo será negado

vlcasa = float(input('Qual é o valor do imóvel: R$'))
salario = float(input('Qual é seu salário: R$'))
tempo = int(input('Em quando anos você deseja pagar?'))*12 # já convertido em meses

mensalidade = vlcasa / tempo

if mensalidade <= salario*0.30:
    print('Seu financiamento será em {:.0f} prestações de R$ {:.2f}'.format(tempo, mensalidade))
else:
    print('Seu empréstimo foi negado!')
