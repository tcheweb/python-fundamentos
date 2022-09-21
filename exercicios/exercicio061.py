# refaça o desafio 51, lendo o primeiro termo e a razão de uma pa.
# mostrando os 10 primeiros termos da progressão usando a estrutura while
primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Entre com a razão da progressão: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
