from random import randint
from time import sleep


def sorteia(lst):
    for cont in range(0, 5):
        lst.append(randint(1,10))
    print(f'Sorteando 5 valores da lista: ', end='')
    pos = 0
    while pos < len(lst):
        print(f'{lst[pos]} ', end='')
        sleep(0.3)
        pos += 1
    print('PRONTO!')


def somaPar(lst):
    pos = contpar = 0
    for v in lst:
        if v % 2 == 0:
            contpar += v
    print(f'Somando os valores pares de {lst}, temos {contpar}.')


num = []
sorteia(num)
print()
somaPar(num)
