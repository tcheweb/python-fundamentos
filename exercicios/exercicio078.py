# Faça um programa que leia 5 valores núméricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# em caso de valores repetidos, mostrar todos
valores = []
listamaior = []
listamenor = []
for valor in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
for pos, valor in enumerate(valores):
    if valor == maior:
        listamaior.append(pos)
    elif valor == menor:
        listamenor.append(pos)
print(f'Os números digitados foram {valores}')
print(f'O maior valor é {maior} e está na(s) posição(ções) {listamaior}.\n Já o menor valor é {menor} e se encontra em {listamenor}')

