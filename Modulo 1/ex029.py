velox = float(input('Qual a sua velociadade em Km/h: '))
if velox > 80:
    multa = (velox - 80) * 7
    print('Você foi multado em {:.2f}R$'.format(multa))
else:
    print('Está dentro do limite!')