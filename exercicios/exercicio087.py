# aprimore o desafio anterior mostrando no final:
# a) a soma de todos os valores pares digitados
# b) A soma dos valores da terceira coluna
# c) O maior valor da segunda linha
matriz = list()
linhas = list()
colunas = list()
somapares = 0
coluna3 = 0
maiorlinha2 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor de [{linha}, {coluna}]: '))
        colunas.append(valor)
        # soma dos pares
        if valor % 2 ==0:
            somapares += valor
        # soma dos valores da coluna 3
        if coluna == 2:
            coluna3 += valor
    matriz.append(colunas[:])
    colunas.clear()
    # maior valor da linha 2
    if linha == 1:
        if maiorlinha2 == 0 or valor > maiorlinha2:
            maiorlinha2 = valor

print(f'{"PRIMEIRA MATRIZ":=^30}')
for linha in matriz:
    print(f'[{linha[0]:^5}]  [ {linha[1]:^5} ]  [ {linha[2]:^5} ]')
print(f'A soma de todos os números pares digitados é: {somapares}')
print(f'A soma dos valores da coluna 3 é: {coluna3}')
print(f'O maior valor da linha 2 é: {maiorlinha2}')



