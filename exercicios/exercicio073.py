# crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de futebol., na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados
#os ultismo 4 colocados
# uma lista com os times em ordem alfabética
# em que posição na tabela está o time da chapecoense.
tabelabrasileiro = ('Palmeiras', 'Fluminense', 'Internacional', 'Flamengo', 'Corinthians', 'Athletico-PR',
                    'Atlético-MG', 'Goíás', 'Botafogo', 'Santos', 'Bragantino', 'São Paulo', 'Fortaleza',
                    'Ceará', 'Coritiba', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude')

print(f'CAMPEONATO BRASILEIRO 2022')
print(f'Os cinco primeiros colocados são {tabelabrasileiro[0:5]}')
print(f'Os lanternas da tabela são {tabelabrasileiro[-4:]}') # mostra os 4 últimos elementos.
print(f'Times em ordem alfabética {sorted(tabelabrasileiro)}')
print(f'O Internacional está na {tabelabrasileiro.index("Internacional")+1}ª posição da tabela')



