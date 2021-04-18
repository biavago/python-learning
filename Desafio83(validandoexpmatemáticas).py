#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expr = str(input('Digite uma expressão: '))
pilha = []
for símbolo in expr:
    if símbolo == '(': #cada vez que encontrar um parênteses aberto, adiciona na lista
        pilha.append('(')
    elif símbolo == ')': #se fort o parêntese fechado, e a lista já tem um aberto, remove um
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0: #se adicionou e excluiu todos, é pq tinha a quantidade correta de parênteses
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
