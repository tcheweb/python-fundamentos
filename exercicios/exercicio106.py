# Faça um mini-sistema que utilize o Interactie Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quano o usuário
# digitar a palavra FIM, o programa encerrará. OBS: use cores.

def ajuda():
    from utils import pinta_texto
    while True:
        pinta_texto('~' * 23, 'branco', 'amarelo')
        pinta_texto('SISTEMA DE AJUDA PYTHON', 'branco', 'amarelo')
        pinta_texto('~' * 23, 'branco', 'amarelo')
        func = str(input('Função ou Biblioteca > ')).lower().strip()
        if func == 'fim':
            print('Saindo...')
            break
        else:
            pinta_texto(help(func), 'preto', 'branco')


ajuda()