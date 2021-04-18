print('~~'*11)
print('SEQUÊNCIA DE FIBONACCI')
print('~~'*11)
n = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
c = 3
print('{} → {}'.format(a, b), end='')
while c <= n:
    f = a + b
    print(' → {}'.format(f), end='')
    a = b
    b = f
    c += 1
print('→ Fim.')
