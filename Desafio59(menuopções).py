from time import sleep
opt = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opt != 5:
    print('''        [1] Soma
        [2] Multiplicação
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    opt = int(input('Qual a sua opção? '))
    if opt == 1:
        soma = n1 + n2
        print('A soma de n1 + n2 é {}'.format(soma))
    elif opt == 2:
        produto = n1 * n2
        print('O resultado de n1 x n2 é {}.'.format(produto))
    elif opt == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é {}.'.format(n1,n2,maior))
    elif opt == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*10)
    sleep(1)
sleep(1)
print('Fim do programa.')
