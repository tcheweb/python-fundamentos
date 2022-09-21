# leia o sexo de uma pessoa. Só aceite M ou F.
# caso esteja errado, peça a ditigação novamente até ter o valor correto
control = 1
while control ==1:
    sexo = input('Digite o sexto [ M/F]').upper()
    if sexo in 'MF':
        control = 0

print('O sexo é {}'.format(sexo))


