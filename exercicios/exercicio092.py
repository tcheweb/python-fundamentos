# Crie um programa que leia nome, ano de nascimento, e carteira de trabalho e cadastre-os(com idade)
# um um dicionário. se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além idade, com quantos anos a pessoa vai se aposentar.
# é pra guardar a idade e não o ano de nascimento. 35 anos de trabalho.
from datetime import date
cadastro = {}
cadastro['nome'] = input('Digite o nome: ')
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
cadastro['idade'] = ano_atual - ano_nasc
cadastro['ctps'] = int(input('Digite a Carteira de trabalho: '))
if cadastro['ctps'] != 0:
    cadastro['ano_contr'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário R$: '))
    tempo_trabalho = ano_atual - cadastro['ano_contr']
    if tempo_trabalho >= 35:
        cadastro['aposentadoria'] = 'Aposentado'
    else:
        cadastro['aposentadoria'] = f'Irá se aposentar com {(35 - tempo_trabalho) + cadastro["idade"]} anos.'
else:
    cadastro['ctps'] = 'Não informada'
    cadastro['aposentadoria'] = 'Sem informações disponíveis'

for k, v in cadastro.items():
    print(f'{k}: {v}')


