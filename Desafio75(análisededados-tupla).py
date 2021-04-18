# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores: {numeros}.')
# A) Quantas vezes apareceu o valor 9.
print(f'O valor 9 apareceu {numeros.count(9)}.')
# B) Em que posição foi digitado o primeiro valor 3.
print(f'O valor 3 apareceu na {numeros.index(3)+1}a posição.')
# C) Quais foram os números pares.
print(f'Os valores pares digitados foram: ', end = '')
for c in numeros:
    if c % 2 == 0:
        print(c, end=', ')
