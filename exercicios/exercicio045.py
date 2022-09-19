# crie um programa que faça o computador jogar jokenpo com você
from random import randint
from time import sleep
jogada = {1 : 'PEDRA', 2 : 'PAPEL', 3 : 'TESOURA'}
nomedojogo = ' JOKEMPO '

print('#'*10 + nomedojogo +'#'*10)
print('#'*30)
print('ESCOLHA SUA JOGADA')
print('#'*30)
print('(1) - PEDRA | (2) PAPEL | (3) TESOURA')
print('#'*30)
pessoa = int(input('Selecione sua mão: '))
computador = randint(1, 3)
vencedor = 'COMPUTADOR'

#print('comp:{} jogada:{}'.format(computador, jogada[computador]))
#print('pessoa: {} jogada: {}'.format(pessoa, jogada[pessoa]))
print('Processando...')
sleep(.5)

print('VOCÊ:  {} x {} :COMPUTADOR'.format(jogada[pessoa], jogada[computador]))

if jogada[pessoa] == jogada[computador]:
    vencedor = 'EMPATE! NINGUÉM'
elif jogada[pessoa] == 'PEDRA' and jogada[computador] == 'TESOURA':
    vencedor = 'VOCÊ'
elif jogada[pessoa] == 'PAPEL' and jogada[computador] == 'PEDRA':
    vencedor = 'VOCÊ'
elif jogada[pessoa] == 'TESOURA' and jogada[computador] == 'PAPEL':
    vencedor = 'VOCÊ'

print('{} VENCEU!'.format(vencedor))






