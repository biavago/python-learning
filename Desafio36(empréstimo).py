# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
trintasal = sal*0.3
parcela = valor/(anos*12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, parcela))
if parcela <= trintasal:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')