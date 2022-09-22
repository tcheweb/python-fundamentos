# crie um programa onde o usuáiro possa digitar vários valores núméricos e cadastre um lista
# caso o número já exista na lista ele não é adicionado. Mostrar mensagem avisando e perguntar se quer continuar.
# no final serão exibidos todos os valores em ordem crescente.
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[len(valores)-1] in valores[:-1]:
        print('Já existe!')
        valores.pop()
    if 999 in valores:
        valores.pop()
        valores.sort()
        print(valores)
        break

