# faça um programa que tenha uma função chamada notas() que pode receber várias notas
# de alunos e vai retonar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função
def notas(*n, sit=False):
    parecer = dict()
    parecer['total'] = len(n)
    parecer['maior'] = max(n)
    parecer['menor'] = min(n)
    parecer['media'] = sum(n)/len(n)
    if sit is True:
        if parecer['media'] >= 8:
            parecer['situacao'] = 'ÓTIMA'
        elif 8 > parecer['media'] >= 6:
            parecer['situacao'] = 'BOA'
        elif parecer['media'] < 6 :
            parecer['situacao'] = 'RUIM'
    return parecer


teste = notas(6, 5.5, 6.3, 5.4, sit=True)
print(teste)


