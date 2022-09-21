#leia vários números inteiros. no final mostre a média entre todos os valores e qual foi o maior e o menor número
# deve perguntar se o usuário quer parar ou não.
from time import sleep
num = maior = menor = soma = media = contagem = 0
controle = 1
while controle == 1:
    num = int(input('Digite um número: '))
    #print('Computando informações...')
    #sleep(1)
    contagem += 1
    soma += num
    if  num > maior:
        maior = num
        if menor == 0:
            menor = num
    elif num < maior and num < menor:
        menor = num
    continuar = input('Deseja continuar [S/N]: ').upper()
    if continuar =='N':
        controle = 0
print('Foram digitados {} números.'.format(contagem))
print('A soma destes números resulta em {}.'.format(soma))
print('O maior número diditado foi {} e o menor {}'.format(maior, menor))





