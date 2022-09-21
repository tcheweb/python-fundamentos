# Simule o funcionamento de um caixa eletronico. No inicio pergunte o valor a ser sacado.
# informar quantas cedulas de # cada valor serão entregues: notas de 50, 20, 10 e 1
print('CAIXA ELETRÖNICO')
while True:
    saque = int(input('Valor R$ '))
    resto = 0
    nota50 = 0
    nota20 = 0
    nota10 = 0
    nota1 = 0
    if saque >= 50:
        nota50 = int(saque / 50)
        resto = saque - (nota50 * 50)
    if resto >= 0 and resto >= 20:
        nota20 = int(resto / 20)
        resto = resto - (nota20 * 20)
    if resto >= 0 and resto >= 10:
        nota10 = int(resto / 10)
        resto = resto - (nota10 * 10)
    if resto >= 0 and resto >= 1:
        nota1 = int(resto / 1)
        resto = resto - (nota1 * 1)
    print(f'Você receberá R$ {saque}, sendo:')
    print(f'{nota50} notas de R$50')
    print(f'{nota20} notas de R$20')
    print(f'{nota10} notas de R$10')
    print(f'{nota1} notas de R$1')
    print('='*20)
    opcao = input('Deseja fazer um novo saque [S/N]? ').upper()
    if opcao == 'N':
        break
