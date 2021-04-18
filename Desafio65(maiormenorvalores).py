#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = media = maior = menor = cont = 0
resposta = 'S'
while resposta in 'sS':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n
    resposta = str(input('Quer continuar [s/n]? ')).strip().upper()[0]
media = soma / cont
print(f'Você difitou {cont} e a média foi {media}.')
# print('Você digitou {} números e a média foi {}.'.format(cont, media))
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
# print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
