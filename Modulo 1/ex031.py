distancia = float(input('Distância percorrida em Km: '))
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print('O valor da passagem é R${:.2f}'.format(passagem))
