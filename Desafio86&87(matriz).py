# 86: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3col = maior = somapar = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        soma += matriz[linha][coluna]
print()

# 87: Aprimore o desafio anterior, mostrando no final:

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
        if matriz[linha][coluna] % 2 == 0: # A) A soma de todos os valores pares digitados.
            somapar += matriz[linha][coluna]
    print()

for linha in range(0,3): # B) A soma dos valores da terceira coluna.
    soma3col += matriz[linha][2]

for coluna in range(0,3): # C) O maior valor da segunda linha.
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print()
print(f'A soma de todos os valores é {soma}.')
print(f'A soma de todos valores pares é {somapar}.')
print(f'A soma dos valores da 3a coluna é {soma3col}.')
print(f'O maior valor da 2a linha é {maior}.')
