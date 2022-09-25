# Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde esses resultados
#em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# mostrar os valores sorteados listando o jogador e o número que tirou.
# depois disso ordenar eles e mostrar o ranking.
from random import randint
from time import sleep
from operator import itemgetter #  pegar um determinado item no dicionário
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)
           }
ranking = []
print('VALORES SORTEADOS')
for k, v in jogadas.items():
    print(f'{k} tirou {v}.')
    sleep(.5)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')





