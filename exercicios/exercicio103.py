# Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmtros opcionais: o nome de um jogador e quantos gols ele marcou.
# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.
def ficha(jogador='', gols=''):
    if jogador == '':
        jogador ='<desconhecido>'
    if not gols.isnumeric():
        gols = 0

    print(f'O jogador {jogador} fez {gols} gols. ')

nome = input('Nome do Jogador: ')
gols = str(input('Quantidade de Gols: '))

ficha(nome, gols)
