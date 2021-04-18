#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a10 = a + (10 - 1)*r
for c in range(a,a10 + r,r):
    print('{}'.format(c),end=' → ')
print('Fim.')
