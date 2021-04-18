# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

price = float(input('Preço das compras: R$'))
opt = str(input('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual a opção escolhida? '''))
if opt == '1':
    valor = price * 0.9
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, valor))
elif opt == '2':
    valor = price * 0.95
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, valor))
elif opt == '3':
    parcela = price / 2
    print('Sua compra será paga em duas parcelas de R${:.2f}.'.format(parcela))
elif opt == '4':
    parcela = int(input('Quantas parcelas?'))
    valor = price * 1.2
    valorparcela = valor / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcela, valorparcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price, valor))
else:
    print('Opção inválida!')
