#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
contidade = contman = contfem = 0
while True:
    print('--'*10)
    print('CADASTRE UMA PESSOA')
    print('--' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        contidade += 1
    if sexo == 'M':
        contman += 1
    if sexo == 'F' and idade < 20:
        contfem += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo foram {contman} homens.')
print(f'E temos {contfem} mulheres com menos de 20 anos.')
