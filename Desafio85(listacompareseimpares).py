# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = []
pares = []
impares = []
# numeros = [[],[]]

for c in range(1,8):
    n = int(input(f'Digite o {c}o. valor: '))
    if n % 2 == 0:
        # numeros[0].append(n)
        pares.append(n)
    else:
        # numeros[1].append()
        impares.append(n)
numeros.append(pares[:])
numeros.append(impares[:])
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')
