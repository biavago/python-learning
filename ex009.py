#leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Digite o preço do produto: '))
novop = p*0.95

print('O preço do produto com desconto é {:.2f}.'.format(novop))
