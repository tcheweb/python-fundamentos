# Mostre na tela uma contagem regressiva para o estou de fogos de artifício
# Indo de 10 até 0 com uma pausa de 1 segundo entre eles.
import emoji
from time import sleep
print('=-', 'Contagem Regressiva!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('Feliz ano novo! \n :fireworks:'))
