soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
print('A soma de todos os números\n\033[32mimpares de 0 a 500 é {}'.format(soma))