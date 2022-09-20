# leia o primeiro termo e a razão de uma progressão aritmetica. No final, mostre os 10 primeiros termos dessa progresssão

termo = int(input('Digite o termo da progressão aritmética: '))
progre = int(input('Entre com a raão da progressão '))
decimo = primeiro + (10 - 1) * progre

for c in range(termo, 11 , progre):
    print(c)
