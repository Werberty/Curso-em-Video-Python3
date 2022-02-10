matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
soma3c = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-'*30)
for x, l in enumerate(matriz):
    for y, c in enumerate(l):
        print(f'[{c:^5}]', end=' ')
        if c % 2 == 0:
            somaPar += c
        if y == 2:
            soma3c += c
    print('\n', end='')
print('-'*30)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')