# Crie um programa que tenha uma função fatorial() que receba dois paramtros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo
# cálculo do fatorial. Inserir docstring
def fatorial(num, show=False):
    """
    Cálculo de fatorial
    :param num: informe o número que deseja obter o fatorial
    :param show: Padrão: False. Para exibir o processo de calculo passe o valor True
    :return: Imprimirá o fatorial do número escolhido
    """
    fat = num
    print(f'!{num} -> {num}', end=' ')
    for c in range(num, 1, -1):
        fat *= (c-1)
        cont = c-1
        if show:
            print(f'x {cont}', end=' ')

    print(f'= {fat}')


fatorial(5, True)

