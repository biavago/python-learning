# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

opção = str(input('''[M] MASCULINO
[F] FEMININO
Escolha a opção do sexo: '''))

if opção == 'M':
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    ano = nasc + 18
    if idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(ano))
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para seu alistamento.'.format(saldo))
        print('Seu alistamento será em {}.'.format(ano))
    elif idade == 18:
        print('Você tem {} anos e deve ser alistar imediamente.'.format(idade))
else:
    print('Você não precisa se alistar.')
