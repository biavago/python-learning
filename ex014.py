# Conversor de moedas

real = float(input('Quantos reais você tem na sua carteira?'))
dolar = real/5.52
print('O valor de R${:.2f} em dólares é US${:.2f}.'.format(real, dolar))