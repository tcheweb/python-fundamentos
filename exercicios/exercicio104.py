# Crie um programa que tenha a função leiaint(), que vai funcionar de
# forma semelhante à função input() do python, só que para aceitar apenas valor numérico
# ex.: n= leiaint('Digite um n')  não deixar passar se não tiver um inteiro.
from utils import pinta_texto
def leiaint(txt_input):
    while True:
        pergunta = str(input(txt_input))
        if pergunta.isnumeric() is False:
            pinta_texto('ERRO! Digite um número válido!', 'vermelho')
        else:
            break
    return pergunta


n = leiaint('digite um número: ')
print(f'Você digitou o número {n}')

