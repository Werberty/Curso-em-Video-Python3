sexo = str(input('Qual é seu sexo [M/F]? ')).strip().upper()[0]
while sexo not in 'MF':
    print('Entrada invalida, tente novamente!')
    sexo = str(input('Qual é seu sexo [M/F]? ')).strip().upper()[0]
print('Registrado com suscesso!')