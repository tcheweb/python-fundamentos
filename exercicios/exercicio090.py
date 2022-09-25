# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário
# No final, mostre o conteúdo da estrutura na tela. >=7 aprovado, abaixo: reprovado. Para um aluno.
cadastro = {}
cadastro['aluno'] = str(input('Nome do Aluno: '))
cadastro['media'] = float(input('Digite a média:'))

if cadastro['media'] >= 7:
    cadastro['situacao'] = 'Aprovado'
elif cadastro['media'] >= 5:
    cadastro['situacao'] = 'Recuperação'
else:
    cadastro['situacao'] = 'Reprovado'

print(f'O aluno {cadastro["aluno"]} teve média {cadastro["media"]} e foi {cadastro["situacao"]}!')
