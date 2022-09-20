# ler o ano de nascimento de 7 pessoas
# mostre quantas não atingiram a maior idade e quantas atigiram (21 anos)
from datetime import date

demaior = 0
demenor = 0

for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = date.today().year - nascimento
    if idade >= 21:
        demaior += 1
    else:
        demenor += 1
print('Das 7 datas de nascimento lidas, {} pessoas tem maior idade e {} são de menor.'.format(demaior, demenor))
