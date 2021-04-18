# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10 #começando após os primeiros termos
while mais != 0: #digitar 0 para a execução do programa
    total += mais #quantos termos a mais vai mostrar de acordo com o que foi pedido
    while cont <= total: #enquanto o contador for menor que o total, ele vai contar. porém o contador começa com 0 e o mais com 10.
        print('{} → '.format(termo),end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos mais você quer?'))  #novos termos a serem calculados após o décimo termo
print('Progressão aritmética com {} termos mostrados.'.format(total))
