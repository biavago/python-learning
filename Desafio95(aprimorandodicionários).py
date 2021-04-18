# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.
jogador = {}
time = []
gols = []
total = 0
while True:
    jogador.clear() # apaga o jogador para adicionar outro
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear() # apaga os gols para adicionar mais
    for c in range(1, partidas + 1):
        n = int(input(f'    Quantos gols na partida {c}?'))
        gols.append(n)
        total += n
    jogador['gols'] = gols #adiciona a lista gold dentro do dicio jogador
    jogador['total'] = total #adiciona o total de gols lidos no dicio jogador
    time.append(jogador.copy()) #cria uma cópia do dicio jogador na lista do time
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp in 'Nn':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys(): # printa o código do jogador de acordo com a key dele no dicio
    print(f'{i:<15}', end='') # printa o código com 15 alinhado a esquerda
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='') #printa informações que estão no dicio, de acordo com o index da lista
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999: #flag
        break
    if busca >= len(time):
        print(f'ERRO! Código inválido.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
        for i,g in enumerate(time[busca]['gols']): #busca as informações e printa de acordo com a lista
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< Volte sempre! >>')
