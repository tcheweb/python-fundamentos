# faça um programa que ajude um jogador da mega-sena a criar palpites.
# o programa perguntará quantos jogos serão gerados e vai sortear 6 números entre 01 e 60
# para cada jogo, cadastrando tudo em uma lista composta. colocar em ordem e usar um timer
from random import randint
from time import sleep
apostas = list()
jogo = list()
print(f'{" GERADOR DE APOSTAS DA MEGA-SENA ":=^40}')
nuApostas = int(input('Digite o número de apostas que você deseja fazer: '))
for aposta in range(0, nuApostas):  # laço para a quantidade de apostas escolhida
    for num in range(0, 6):  # laço para gerar as 6 dezenas de uma aposta
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    print(f'Aposta {aposta +1} -> {jogo}')
    sleep(1)
    jogo.sort()
    apostas.append(jogo[:])
    jogo.clear()

print(f'{len(apostas)} APOSTAS GERADAS COM SUCESSO!')
print('BOA SORTE!')

