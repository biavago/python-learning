def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a} m².')


def linha():
    print('~' * 23)


linha()
print(' Controle de Terrenos ')
linha()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
linha()
área(l, c)
