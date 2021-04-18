from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
player = int(input('Qual a sua escolha? '))
if player == 0 or player == 1 or player == 2: #caso digite outro numero
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!')
    sleep(0.5)
    print('='*20)
    print('O computador escolheu {}'.format(itens[pc]))
    print('O jogador escolheu {}'.format(itens[player]))
    print('='*20)
    if pc == 0: #computador jogou pedra
        if player == 0:
            print('Deu empate!')
        elif player == 1:
            print('Você venceu!')
        elif player == 2:
            print('O computador venceu!')
        else:
            print('Opção inválida!')
    elif pc == 1: #computador jogou papel
        if player == 1:
            print('Deu empate!')
        elif player == 2:
            print('Você venceu!')
        elif player == 0:
            print('O computador venceu!')
        else:
            print('Opção inválida!')
    elif pc == 2: #computador jogou tesoura
        if player == 2:
            print('Deu empate!')
        elif player == 0:
            print('Você venceu!')
        elif player == 1:
            print('O computador venceu!')
        else:
            print('Opção inválida!')
else:
    print('Opção inválida.')
