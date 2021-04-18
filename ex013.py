distancia = float(input('Digite a distância em metros: '))
km = distancia/1000
hm = distancia/100
dam = distancia/10
dm = distancia*10
cm = distancia*100
mm = distancia*1000

print('A medida de {} corresponde a: '.format(distancia))
print('Em km: {}\nEm hm: {}\nEm dam: {}\nEm dm: {}\nEm cm: {}\nEm mm: {}'.format(km, hm, dam, dm, cm, mm))

