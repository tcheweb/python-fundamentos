# faça um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
# se o passo for zero, contar de um em um. se inserir número negativo, tornar positivo.

def área(largura, comprimento):
    print(f' Para a largura {largura}m e o comprimento {comprimento}m a área é {largura * comprimento}m².')
    

# Programa principal
larg = float(input('Digite a largura em metros: '))
comp = float(input('Digite o comprimento em metros: '))

área(larg, comp)