#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    # print('Os segmentos foram um triângulo ', end='') e depois printa somente os nomes dos triângulos.
    if a == b == c:
        print('Os segmentos formam um triângulo equilátero.')
    elif a == b or b == c or a == c:
        print('Os segmentos fomam um triângulo isóceles.')
    elif a != b and a != c and c != b:
        print('Os segumentos formam um triângulo escaleno.')
else:
    print('Os segmentos não formam um triângulo.')
