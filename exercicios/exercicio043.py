# desenvolva uma lógica que leio o peso e a altura de uma pessoa.
# calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5 = abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2
if imc < 18.5:
    print('Seu IMC é de {:.1f} e você está abaixo do peso.'.format(imc))
elif imc < 26 and imc >= 18.5:
    print('Seu IMC é de {:.1f} e você está no peso ideal.'.format(imc))
elif imc >=25 and imc <= 30:
    print('Seu IMC é de {:.1f} e você está com sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de {:.1f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.1f} e você está com Obesidade Mórbida.'.format(imc))
