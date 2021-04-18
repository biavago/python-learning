# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = soma = total = 0
stop = 999
n = int(input('Digite um número [999 para parar]:'))
while n != stop:
    soma += n
    total += 1
    n = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e a soma entre eles é {}.'.format(total, soma))
