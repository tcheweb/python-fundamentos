# Escreva um programa que tenha uma função chamada voto que vai receber como
# parâmetro o ano de nascimento de uma pessoa. retornando um valor literal indicando
# se uma pessoa tem voto negado, opcional ou obrigatório nas eleições
# maior de 65 é opcional

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade >= 65:
        print(f'Com {idade} anos, você não é obrigado a votar.')
    elif idade < 65 and idade >= 18:
        print(f'Com {idade} anos, você é obrigado a votar.')
    elif idade < 18 and idade >= 16:
        print(f'com {idade} anos, o voto é opcional.')
    else:
        print(f'Com {idade} você não tem direito a votar.')


ano_nasc = int(input("Digite o ano de nascimento [AAAA]: "))
voto(ano_nasc)


