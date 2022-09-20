# leia nome, idade e sexo de 4 pessoas.
# no final mostre: a média de idade, o nome do homem mais velho, quantas mulheres tem menos de 20 anos.

somaidade = 0
homemmaisvelho = 0
nomemaisvelho = ''
mulhermenos20 = 0
for c in range(1, 5):
    nome = input('Digite o {}º Nome: '.format(c))
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M ou F)').upper()

    if sexo == 'M':
        if idade > homemmaisvelho:
            homemmaisvelho = idade
            nomemaisvelho = nome
    elif sexo == 'F' and idade < 20:
        mulhermenos20 = mulhermenos20 + 1
    somaidade = somaidade + idade


print('A média de idade das pessoas é de {} anos.'.format(somaidade / 4))
print('O nome do homem mais velho é {}'.format(nomemaisvelho))
print('Há {} mulheres abaixo dos 20 anos.'.format(mulhermenos20))


