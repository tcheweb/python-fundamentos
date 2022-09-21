# leia a idade e sexo  de várias pessoas. a cada pessoa cadastrada
# perguntar se quer cadastrar outra ou não.
# motrar quantos tem mais de 18, quantos homens foram cadastros
#quantas mulheres com menos de 20 anos.
# só aceitar o dado se ele for válido.
mais18 = homens = mulheresmenos20 = 0
while True:
    sexo = ' '
    while sexo not in 'mMfF':
        sexo = input('Digite o sexo [M/F]: ')

    idade = int(input('Digite a idade: '))
    if idade > 18:
        mais18 += 1
    if sexo in 'mM':
        homens += 1
    else:
        if idade < 20:
            mulheresmenos20 += 1
    opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheresmenos20} mulher tem menos de 20 anos.')


