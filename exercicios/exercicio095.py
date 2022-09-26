# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
# mostrar tabela com código, nome, gols e total de gols
# perguntar dados de qual jogador quer mostrar.
tabela = []
ficha = {}
gols = []

while True:
    # obtendo informações do jogador
    ficha['nome'] = str(input('Nome do Atleta:'))
    ficha['partidas'] = int(input('Quantidade de partidas: '))
    ficha['total_gols'] = 0
    if ficha['partidas'] != 0:
        for partida in range(0, ficha['partidas']):
            gol = int(input(f'Quantidade de Gols na partida {partida +1} : '))
            ficha['total_gols'] += gol
            gols.append(gol)
        ficha['gols'] = gols[:]
        gols.clear()
    tabela.append(ficha.copy())
    resp = input('Deseja inserir outro Jogador? [S/N]: ').upper().strip()
    if resp == 'N':
        break
while True:
    print('ESTATÍSTICAS ESPORTIVAS 1.0')
    print('=' *20)
    print('| CODIGO | ATELTA    |')
    for codigo, jogador in enumerate(tabela):
        print(f'| [{codigo}]   | {jogador["nome"]} |')
    op = int(input('Selecione o Atleta (999 para sair): '))
    if op == 999:
        break
    else:
        for cod, item in enumerate(tabela):
            if cod == op:
                print(f'CÓD: {cod} | {tabela[op]["nome"]}')
                print(f'Gols: {tabela[op]["gols"]}')
                print(f'Total de Gols: {tabela[op]["total_gols"]}')
