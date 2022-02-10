def area(x, y):
    a = x*y
    print(f'A área de um terreno {x}x{y} é de {a}m2.')


print('Controle de terrenos')
print('----------------------')
altura = float(input('LARGURA (m): '))
comprimento = float(input('ALTURA (m): '))
area(comprimento, altura)