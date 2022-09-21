#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns
#termos. o programa encerra quando ele disser que quer mostrar 0 termos
primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Entre com a razão da progressão: '))
termo = primeiro
contador = 1
fim = 10
while contador <= fim:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
    if contador == fim + 1:
        continuar = int(input('\nDeseja mostrar mais termos? Informe quantos:').strip().upper()[0])
        if continuar != 0:
            fim = continuar
            contador = 1
print('FIM')
