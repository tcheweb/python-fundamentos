# crie um programa que crie uma matriz de dimensão 3 x 3 e preencha com valores lidos
# pelo teclado. no final mostre a matriz na tela.
matriz = list()
linhas = list()
colunas = list()
for linha in range(0,3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor de [{linha}, {coluna}]: '))
        colunas.append(valor)
    matriz.append(colunas[:])
    colunas.clear()
print(f'{"PRIMEIRA MATRIZ":=^30}')
for linha in matriz:
    print(f'[{linha[0]:^5}]  [ {linha[1]:^5} ]  [ {linha[2]:^5} ]')



