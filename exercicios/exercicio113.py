# reescreva a função leiaint() que fizemos no 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a
# mesma funcionalidade
from utils import pinta_texto

def leiaint(txt_input):
    while True:
        try:
            pergunta = int(input(txt_input))

        except ValueError:
            pinta_texto('ERRO! Digite um número inteiro!', 'vermelho')

        else:
            return pergunta


def leiafloat(entrada):
    while True:
        try:
            pergunta = float(input(entrada))
        except ValueError:
            pinta_texto('ERRO: Digite um número real!', 'amarelo')
        else:
            return pergunta

n = leiaint('digite um número: ')
print(f'Você digitou o número {n}')

n2 = leiafloat('Digite um número real: ')
print(f'Você digitou {n2}')
