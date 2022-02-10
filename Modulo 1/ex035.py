print('-+-' * 11)
print('----Verificador de triângulo-----')
print('-+-' * 11)
l1 = int(input('Medida do lado 1: '))
l2 = int(input('Medida do lado 2: '))
l3 = int(input('Medida do lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Pode formar um triângulo!')
else:
    print('Não forma um triângulo!')
