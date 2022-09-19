# leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: senior
# acima: master
from datetime import date

nascimento = int(input('Em que ano você nasceu? '))
hoje = date.today()
idade = hoje.year - nascimento

if idade < 10:
    print('Você tem {} anos e é da categoria MIRIM'.format (idade))
elif 15 > idade > 9:
    print('Você tem {} anos e é da categoria INFANTIL'.format(idade))
elif 20 > idade > 14:
    print('Você tem {} anos e é da categoria JUNIOR'.format(idade))
elif 21 > idade > 19:
    print('Você tem {} anos e é da categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e é da categoria MASTER'.format(idade))
