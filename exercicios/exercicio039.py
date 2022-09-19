# leia o ano de nascimento de um jovem e informe de acordo com a idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento
# deve mostrar também o tempo que falta ou que passou do prazo.
from datetime import date

nascimento = int(input('Digite seu ano de nascimento com 4 digitos: '))
hoje = date.today()
idade = hoje.year - nascimento

print('Você tem {} ano(s).'.format(idade))
if idade == 18:
    print('É hora de se alistar!')
elif idade < 18:
    print('Ainda falta {} ano(s) para você se alistar.'.format(18 - idade))
else:
    print('Já pasou {} ano(s) do prazo de alistamento.'.format(idade - 18))
