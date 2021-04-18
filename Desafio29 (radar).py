#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#  mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import emoji
from time import sleep
velocidade = float(input('Digite a velocidade do carro: '))
print('\033[1;30;46mProcessando...\033[m\n')
sleep(1)

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(emoji.emojize(':warning: \033[1;33mATENÇÃO! \033[m:warning: \nVocê excedeu o limite permitido de 80km/h. \033[4;31mVocê deve pagar uma multa de R${:.2f}.\033[m'.format(multa), use_aliases=True))
print('Tenha um bom dia! Dirija com segurança!')

# print('ATENÇÃO! Você excedeu o limite permitido de 80km/h.\n Você deve pagar uma multa de R${:.2f}.'.format(multa))