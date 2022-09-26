# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
#a) Quantas pessoas foram cadastradas
#b) A média de idade do grupo
#c)Uma lista com todas as mulheres
#d)uma lista com todas as pessoas com idade acima da média.
ficha = {}
cadastro = []
total_idade = 0
while True:
    ficha['nome'] = str(input('Nome...: '))
    ficha['sexo'] = str(input('Sexo...: ')).upper().strip()
    ficha['idade'] = int(input('Idade..:'))
    total_idade += ficha['idade']
    cadastro.append(ficha.copy())

    resp = input('Inserir outra pessoa? [S/N]:').upper().strip()
    if resp == 'N':
        break

print(f'Quantidade de pessoas cadastradas: {len(cadastro)}')
print(f'A média de idade do grupo é: {total_idade / len(cadastro):.1f}')
print(f'Mulheres: ', end= ' ')
for c in cadastro:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ,', end='')

print(f'\nPessoas com idade acima da média: ', end=' ')
for c in cadastro:
    if c['idade'] > (total_idade / len(cadastro)):
        print(f'{c["nome"]}, ', end='')






