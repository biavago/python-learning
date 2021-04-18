#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
cont = 0
result = 0
n = int(input('Digite um número: '))
for c in range(0,11):
    result = n * c
    print(n,'x',c,'=',result)
