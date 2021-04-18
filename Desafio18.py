#Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(ang))
print('O seno de {} é {:.2f}.'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O cosseno de {} é {:.2f}.'.format(ang, cos))
tg = math.tan(math.radians(ang))
print('A tangente de {} é {:.2f}.'.format(ang, tg))
