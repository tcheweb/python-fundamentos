# faça um programa que leia o nome e peso de várias pessoas. Mostrar
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais pesadas
# c) Uma listagem com as pessoas mais leves
pessoas = list()
cadastro = list()
pesados = list()
leves = list()
while True:
    nome = input('Nome: ')
    if nome == '0':
        print(f'PESSOAS CADASTRADAS: {pessoas}')
        break
    peso = float(input('Peso: '))
    cadastro.append(nome)
    cadastro.append(peso)
    pessoas.append(cadastro[:])
    cadastro.clear()

for pessoa in pessoas:
    if len(pesados) == 0:
        pesados.append(pessoa)
        leves.append(pessoa)
    elif pessoa[1] > pesados[0][1]:
        pesados.clear()
        pesados.append(pessoa)
    elif pessoa[1] == pesados[0][1]:
        pesados.append(pessoa)
    elif pessoa[1] < leves[0][1]:
        leves.clear()
        leves.append(pessoa)
    elif pessoa[1] == leves[0][1]:
        leves.append(pessoa)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são ', end=' ')
for p in pesados:
    print(p[0], end=' e ')
print(f'tem {pesados[0][1]:.0f} kilos')
print(f'As pessoas mais leves são ', end=' ')
for p in leves:
    print(p[0], end=' e ')
print(f' pesam {leves[0][1]:.0f} kilos')


