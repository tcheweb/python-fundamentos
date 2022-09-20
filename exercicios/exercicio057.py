# leia o sexo de uma pessoa. Só aceite M ou F.
# caso esteja errado, peça a ditigação novamente até ter o valor correto
sexo = 'M'
while sexo not in 'MF':
    sexo = input('Digite o sexo [M/F]:').upper().strip()[0]
print('O sexo é {}'.format(sexo))


