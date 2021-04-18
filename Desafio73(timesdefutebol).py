#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport',
         'América-MG', 'Vitória', 'Paraná')
print(f'Lista dos times do Brasileirão:\n{times}')
print(f'Os primeiros 5 times são:\n{times[:5]}')
print(f'Os últimes 4 colocados são:\n{times[16:]}')
print(f'Os times em ordem alfabética:\n{sorted(times)}')
print(f'O time da Chapecoense está na posição {times.index("Chapecoense")+1}.')