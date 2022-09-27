# faça uma programa que  tenha uma lista chamada números e duas funções.
# uma função chamada sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocála dentro de
# uma lista e a segunda função vai mostrar a soma entre todos os valores Pares sorteados pela função anterior
from random import randint

def sorteia():
    num = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
    return(num)

def somaPar(lista):
    total = 0
    for c in lista:
        if c % 2 == 0:
            total += c
    print(total)


#programa
numeros = sorteia()
print(numeros)
somaPar(numeros)