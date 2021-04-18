n = int(input('\033[1mMe diga um número qualquer:\033[m '))
resultado = n % 2

if resultado == 1:
    print('O número {} é \033[4;32mímpar\033[m.'.format(n))
else:
    print('O número {} é \033[4;34mpar\033[m.'.format(n))