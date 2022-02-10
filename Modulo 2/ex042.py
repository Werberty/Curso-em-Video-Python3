print('-+-' * 11)
print('----Verificador de triângulo-----')
print('-+-' * 11)
l1 = int(input('Medida do lado 1: '))
l2 = int(input('Medida do lado 2: '))
l3 = int(input('Medida do lado 3: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    if l1 == l2 == l3:
        print('Pode formar um triângulo EQUILÁTERO!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Pode formar um triângulo ISÓCELES')
    elif l1 != l2 != l3:
        print('Pode formar um triângulo ESCALENO')
else:
    print('Não forma um triângulo!')