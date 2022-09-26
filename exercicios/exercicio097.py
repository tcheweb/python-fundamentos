# faça um programa que tenha a função chamada escreva(), que recebe um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável. acompanhar o tamanho da mensagem. mensagem centralizada.

def escreva(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)


escreva('Adriano Borges Baumart')
