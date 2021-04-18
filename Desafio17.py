#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

''' Método sem importar
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co,ca)

print('A hipotenusa vai medir {:.2f}.'.format(hi))

