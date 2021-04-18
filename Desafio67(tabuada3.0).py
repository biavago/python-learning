# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    else:
        for cont in range(0, 11):
            produto = num * cont
            print(f'{num} x {cont} = {produto}')
            cont += 1
print('Fim do programa.')
