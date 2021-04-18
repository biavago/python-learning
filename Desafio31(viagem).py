# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual é a distância da sua viagem? '))

if km <= 200:
    # preço = km * 0.5
    print('O preço da sua passagem será R${:.2f}.'.format(km*0.5))
else:
    # preço = km * 0.45
    print('O preço da sua passagem será R${:.2f}.'.format(km*0.45))
# preço = km * 0.5 if km <= 200 else km * 0.45

# print('O preço da sua passagem será R${:.2f}.'.format(preço))
