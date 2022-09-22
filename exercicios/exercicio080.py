# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista já na posição correta de inserção
# sem usar o sort. No final mostra a lista ordenda na tela.
# informa em qual posição da lista foi adicionado.
lista = list()
for num in range(0, 5):
    valor = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(valor)
        print(f'{valor} adicionado ao FIM da lista!')
    else:
        if valor > max(lista):
            lista.append(valor)
            print(f'{valor} adicionado ao FIM da lista!')
        elif val
            or <= min(lista):
            lista.insert(0, valor)
            print(f'{valor} adicionado no INICIO da lista!')
        elif valor < max(lista) and valor > min(lista):
            for li in lista:
                if valor > li:
                    if valor < lista[lista.index(li)+1]:
                        lista.insert(lista.index(li)+1, valor)
                        print(f'{valor} adicionado no MEIO da lista!')

print(lista)
