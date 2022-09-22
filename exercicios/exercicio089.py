#Faça um programa que leia nome e duas notas de vários alunos e guarde
#tudo em uma lista composta. no final, mostre um boletim contendo a média de
#cada um e permita que o usuário possa mostrar as notas de cada aluno invidualmente.
cad_alunos = list()
aluno = list()
codigo = 1
while True:
    nome = input('Nome do Aluno: ').upper()
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media = n1 + n2 / 2
    # grava os dados na lista aluno
    aluno.append(codigo)
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    cad_alunos.append(aluno[:])
    aluno.clear()
    codigo += 1
    resp = input('Deseja inserir outro aluno? [S/N]: ').upper().strip()
    if resp == 'N':
        break
# exibir o boletim da turma
print(f'{"BOLETIM ESCOLAR":=^30}')
print(f'|CODIGO|    NOME    |  MÉDIA |')
print(f'='*30)
for dado in cad_alunos:
    print(f'| {dado[0]:^4} | {dado[1]:^10} | {dado[4]:^6.1f} |')
print(f'='*30)

while True:
    op = int(input('Digite o código do aluno para consultar notas: '))
    for cod in cad_alunos:
        if cod[0] == op:
            print(f'O aluno {cod[1]} tirou {cod[2]} e {cod[3]} e sua média foi {cod[4]:.1f}')
    op2 = input('Deseja consultar outro aluno? [S/N]: ').upper().strip()
    if op2 == 'N':
        break