#leia dois valores e mostre um menu na tela.
# 1 - somar, 2 - multiplicar, 3 -maior, 4 - novos números, 5 -  sair do programa
# deve realizar a operação solicitada em cada caso.
from time import sleep
opcao = 0
vl1 = int(input('Primeiro número:'))
vl2 = int(input('Segundo número: '))
while opcao != 5:
    sleep(1)
    print('''
            PRIMEIRO: {}  | SEGUNDO: {}
            [ 1 ] SOMAR
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEROS
            [ 5 ] SAIR'''.format(vl1, vl2))
    opcao = int(input('ESCOLHA UMA DAS OPÇÕES ACIMA:'))
    if opcao == 1:
        soma = vl1 + vl2
        print('A soma de {} + {} = {}'.format(vl1, vl2, soma))
        opcao = 0
    elif opcao == 2:
        multiplicacao = vl1 * vl2
        print('A multiplicação de {} x {} = {}'.format(vl1, vl2, multiplicacao))
        opcao = 0
    elif opcao == 3:
        if vl1 > vl2:
            print('{} é maior que {}'.format(vl1, vl2))
        else:
            print('{} é maior que {}'.format(vl2, vl1))
    elif opcao == 4:
        vl1 = int(input('Primeiro número:'))
        vl2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Saindo...')
    else:
        print('Opção inválida!')
        opcao = 0







