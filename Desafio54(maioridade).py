#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anonasc = 0
contmaior = 0
contmenor = 0
anoatual = date.today().year
for c in range(1,8):
    anonasc = int(input('Em que ano a {}o pessoa nasceu?'.format(c)))
    idade = anoatual - anonasc
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('Desse grupo, {} são maiores de idade e {} não são.'.format(contmaior,contmenor))
