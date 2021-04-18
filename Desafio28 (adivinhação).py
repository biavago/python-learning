# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# from random import randint
import random
from time import sleep # faz o computador esperar alguns segundos
print('-==-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-==-'*20)
n = int(input('Em que número pensei? '))
print('Processando...')
sleep(2) # espera 2 segundos
escolhido = random.randint(0,5) # faz o computador escolher um número entre 0 e 5
if escolhido == n:
    print('Você acertou! Parabéns!')
else:
    print('Você errou! O número que eu pensei foi o {}!'.format(escolhido))

