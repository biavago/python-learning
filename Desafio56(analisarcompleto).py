#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
contsex = 0
nome = ''
age = 0
sexo = ''
maioridade = 0
velho = ''
soma = 0
media = 0
for c in range(1,5):
    print('-----{}o PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    soma += age
    if sexo in 'mM':
        maioridade = age
        velho = nome
        if age > maioridade:
            maioridade = age
            velho = nome
    if sexo in 'fF' and age > 20:
        contsex += 1
media = soma / 4
print('A média de idade desse grupo é {:.0f}.'.format(media))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contsex))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade,velho))
