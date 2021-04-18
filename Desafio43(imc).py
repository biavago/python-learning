# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

weight = float(input('Qual seu peso?(kg) '))
height = float(input('Qual sua altura?(m) '))
imc = weight / (height ** 2)
print('O IMC dessa pessoa é {:.1f} e ela está '.format(imc),end='')
if imc < 18.5:
    print('abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('no peso ideal.')
elif 25 <= imc < 30:
    print('no sobrepeso.')
elif 30 <= imc < 40:
    print('em obesidade.')
else:
    print('em obesidade mórbida.')
