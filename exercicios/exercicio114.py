# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import requests

url = 'http://www.pudim.com.br'

try:
    teste = requests.get(url)

except :
    print(f'O site {url} não está acessível!')

else:
    print(f'O site {url} está no ar!')
