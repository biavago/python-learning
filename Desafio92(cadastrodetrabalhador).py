# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
anoatual = date.today().year
trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = anoatual - anonasc
trabalhador['ctps'] = int(input('Carteiro de trabalho (0 se não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - anoatual)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')
