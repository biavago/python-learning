#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
contmil = cont = soma = menor = 0
nomemenor = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    if preco > 1000:
        contmil += 1
    if cont == 1 or preco < menor:# o or substitui o else pois os blocos de condições são iguais.
        menor = preco
        nomemenor = nome
    # else:
    #     if preco < menor:
    #         menor = preco
    #         nomemenor = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total da compra foi R${soma:.2f}.')
print(f'Temos {contmil} produtos custando mais que R$1000,00.')
print(f'O produto mais barato foi {nomemenor} que custa R${menor:.2f}.')
