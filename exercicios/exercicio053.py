# Leia uma frase qualquer e diga se ela é um palíndromo. desconsiderando os espacos
#apos a sopa
#a sacada da casa
#a torre da derrota
# o lobo ama o bolo
# anoratam a data da maratona

frase = str(input('Digite uma frase: '))
semespaco = frase.replace(' ', '').upper()
invert = str('')

for c in range(len(semespaco)-1, -1, -1):
    invert = invert + semespaco[c]
if semespaco == invert:
    print('{} é um palíndromo!'.format(frase))
else:
    print('{} não é um palíndromo'.format(frase))







