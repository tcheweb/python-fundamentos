# jogue par ou impar com o computador
# o jogo só será interrompido quando o joador perder
# mostrando o total de vitórias consecutivas do jogador
from random import randint
vitorias = 0
print('JOGO DO PAR OU IMPAR')
while True:
    escolha = str(input('Você escolhe PAR ou IMPAR? [P / I]').upper())
    jogada = int(input('Qual seu número? '))
    computador = randint(0, 6)
    soma = jogada + computador
    print(f'VOCÊ: {jogada} x COMPUTADOR: {computador}')
    if soma % 2 == 0:
        if escolha == 'P':
            print('Você venceu!')
            vitorias += 1
        else:
            break
    else:
        if escolha == 'I':
            print('Você venceu!')
            vitorias += 1
        else:
            break
print('Você perdeu. :-(')
print(f'Você teve {vitorias} consecutivas')




