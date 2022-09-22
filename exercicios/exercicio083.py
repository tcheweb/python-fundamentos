# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#exp = list('(a+b)+(b)+(c/2)')  # para testes
exp = input('Digite a expressão: ')
abriu = 0
fechou = 0
if exp.count('(') > 0 or exp.count(')'):  # verifica se a expressão tem parenteses
    if exp.count('(') == exp.count(')'):  # verifica se a quantidade de parenteses é a mesma
        for item in exp:
            if item == '(':
                abriu += 1
            if item == ')' and fechou < abriu:
                fechou +=1
        if abriu == fechou:
            print('A expressão matemática está correta.')
        else:
            print('A expressão está errada')
    else:
        print('A expressão está errada!')
else:
    print('A expressão não possui parenteses')

