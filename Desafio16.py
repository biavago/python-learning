#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''Método de fazer sem importar math:

num = float(input('Digite um número: ')
print('A porção inteira de {} é {}.'.format(num, int(num))'''


import math

num = float(input('Digite um número: '))
print('A porção inteira de {} é {}.'.format(num, math.trunc(num)))

