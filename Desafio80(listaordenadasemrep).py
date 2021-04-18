# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numeros = []
maior = menor = 0
for cont in range(0,6):
    n = int(input('Digite um valor:'))
    if cont == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print()
print(f'Os valores digitados em ordem foram: {numeros}')
