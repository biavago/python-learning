# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
from random import randint
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# Depois disso, mostre a listagem de números gerados
print('Os valores sorteados foram: ', end='')
for c in t:
    print(f'{c}', end=' ')
# e também indique o menor e o maior valor que estão na tupla.
print(f'\nO maior valor foi {max(t)}')
print(f'O menor valor foi {min(t)}')
