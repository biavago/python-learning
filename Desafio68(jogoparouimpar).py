# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from time import sleep
from random import randint
cont = 0
teste = ''
while True:
    play = int(input('Diga um valor:'))
    pc = randint(0,11)
    soma = play + pc
    teste = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {play} e o computador jogou {pc}. O total é {soma} então deu ', end='')
    print('PAR.' if soma % 2 == 0 else 'ÍMPAR.')
    while teste not in 'PpIi':
        teste = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if soma % 2 == 0:
        if teste == 'P':
            print('Você venceu! Vamos jogar novamente...')
            print('=-' * 10)
            cont += 1
        elif teste == 'I':
            print('Você perdeu!')
            break
    if soma % 2 == 1:
        if teste == 'I':
            print('Você venceu! Vamos jogar novamente...')
            print('=-' * 10)
            cont += 1
        elif teste == 'P':
            print('Você perdeu!')
            break
sleep(0.5)
print('=-'*10)
print(f'GAME OVER! Você venceu {cont} vezes.')
print('=-'*10)
