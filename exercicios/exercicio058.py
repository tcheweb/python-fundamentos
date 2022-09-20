#Melhore o jogo do desafio 28
# computador pensa em um número entre 0 e 10
# jogador deve tentar até acertar. mostrando o final quantos palpites necessários para vencer
from random import randint
from time import sleep
jogadas = 0
computador = randint(0, 10)
jogador = 1
print('TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO!')
while computador != jogador:
    jogadas += 1
    jogador = int(input('Digite seu palpite: '))

sleep(1)
print('Parabéns! Você precisou de {} jogadas para acertar.'.format(jogadas))


