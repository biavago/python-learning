# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a10 = a + (10 - 1)*r
c = a
while c < (a10 + r):
    print('{}'.format(c), end=' → ')
    c += r
print('Fim.')
