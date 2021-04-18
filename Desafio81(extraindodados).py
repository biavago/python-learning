#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
# cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    # cont += 1
    r = str(input('Quer continuar? [S/N] ')).strip()
    if r in 'nN':
        break
print()
# print(f'Você digitou {cont} elementos.')
print(f'Você digitou {len(lista)} elementos.')
print()
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
print()
if 5 in lista:
    print('O valor 5 faz parte dessa lista.')
else:
    print('O valor 5 não faz parte dessa lista.')
