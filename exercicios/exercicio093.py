# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# guardar uma lista dentro do dicionário.
ficha = {}
gols = []
ficha['nome'] = str(input('Nome do Atleta:'))
ficha['partidas'] = int(input(f'Quantidade de partidas de {ficha["nome"]}: '))
ficha['total_gols'] = 0
if ficha['partidas'] != 0:
    for partida in range(0, ficha['partidas']):
        gols.append(int(input(f'Quantidade de Gols na partida {partida +1} : ')))
    ficha['gols'] = gols[:]
    ficha['total_gols'] = sum(gols)

print(f'O jogador {ficha["nome"]} jogou {ficha["partidas"]} partidas, sendo que:')
for k, v in enumerate(ficha['gols']):
    print(f'na partida {k+1} fez {v} gols.')



