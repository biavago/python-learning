from time import sleep


def maior(* num):
    print('Analisando os valores passados...')
    pos = 0
    for pos in num:
        print(f'{pos} ', end='')
        sleep(0.3)
        pos += 1
    print()
    print(f'Foram informados {len(num)} valores ao todos.')
    print(f'O maior valor informado foi {max(num)}')
    line()


def line():
    print('~' * 30)


line()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
