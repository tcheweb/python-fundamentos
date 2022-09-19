#leia duas nootas de um aluno e calcule sua média. mostrando uma mensagem no final
# de acordo com a média atingida.
# média abaixo de 5.: reprovado
# media entre 5 e 6.9: recuperação
# media 7 ou superior: aprovado

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi {:.2f} e você foi REPROVADO'.format(media))
elif 6.9 >= media >= 5:
    print('Sua média foi {:.2f} e você ficou em RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi {:.2f} e você foi APROVADO'.format(media))

