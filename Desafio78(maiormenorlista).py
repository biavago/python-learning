# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
# valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    # if c == 0:
    #     maior = menor = valores[c]
    # else:
    #     if valores[c] > maior:
    #         maior = valores[c]
    #     elif valores [c] < menor:
    #         menor = valores[c]
maior = max(valores)
menor = min(valores)
print()
print(f'Você digitou os valores: {valores}')
print()
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f' {i} ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i} ', end='')
