#Faça um programa que leia a largura e a latura de uma parede
#em metros, calcule a quantidade de tinta necessária, sabendo que cada
#litro de tinda pinta uma área de 2m2

h = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
a = h * l
qt = a//2

print('A área a ser pintada é {:.2f} e a quantidade de tinta necessária é {}'.format(a, qt))
