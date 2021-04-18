from time import sleep


def line():
    print('~' * 30)


def cont(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(2)
    for valor in range(i, f + 1, p):
        print(f'{valor} ', end='')
        sleep(0.3)
    print('Fim!')


line()
cont(1, 10, 1)
line()
cont(10, 0, -2)
line()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início:   '))
fim = int(input('Fim:      '))
passo = int(input('Passo:    '))
line()
cont(inicio, fim, passo)
