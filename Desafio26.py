frase = str(input('Digite a frase: ')).lower().strip()

print('A letra a aparece {} vezes.'.format(frase.count('a')))
print('A primeira vez que a letra a aparece é na posição {}.'.format(frase.find('a') +1))
print('A última vez que a letra a aparece é na posição {}.'.format(frase.rfind('a') +1))

