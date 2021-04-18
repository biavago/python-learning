#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
from random import randint
print('''Sou seu computador...
Vou pensar em um número de 0 a 10.
Será que você consegue adivinhar qual?''')
cont = 1
player = int(input('Qual seu palpite? '))
pc = randint(0,10)
while player != pc:
    if pc > player:
        print('Mais... Tente novamente!')
        player = int(input('Qual seu palpite? '))
        cont += 1
    if pc < player:
        print('Menos... Tente novamente!')
        player = int(input('Qual seu palpite? '))
        cont += 1
if player == pc:
    print('Acertou com {} tentativas. Parabéns!'.format(cont))
