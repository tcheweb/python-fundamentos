# Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde esses resultados
#em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# mostrar os valores sorteados listando o jogador e o número que tirou.
# depois disso ordenar eles e mostrar o ranking.
from random import randint
from time import sleep
apostas = list()
jogadas = dict()
ranking = []
for jogador in range(1, 5):
    jogada = randint(1, 6)
    jogadas['jogador'] = f'Jogador {jogador}'
    jogadas['jogada'] = jogada
    apostas.append(jogadas.copy())
    jogadas.clear()
    print(f'Jogador {jogador} tirou {jogada}')
    sleep(.5)
print('RANKING DO JOGO DE DADOS')
cont = 0
for c in range(6, 0, -1):
    for aposta in apostas:
        if aposta['jogada'] == c:
            ranking.append(aposta.copy())

print(f'Ranking:')
for k, v in enumerate(ranking):
    print(f'{k+1} lugar: {v["jogador"]} ')







