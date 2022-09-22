# programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. o programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if num < 0 or num > 20:
            print('Intervalo inválido! Tente novamente.')
        else:
            break
    print(f'O número digitado foi {numeros[num]}')
    op = input('Deseja continuar [S/N]? ')
    if op in 'Nn':
        break


