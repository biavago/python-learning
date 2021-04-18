# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = float(input('Primeiro valor: '))
b = float(input('Segundo valor:'))
c = float(input('Terceiro valor:'))
# Verificando quem é menor. Assumir que o a é menor ou maior, elimina if a < b e a < c.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
