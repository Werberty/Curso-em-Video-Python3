palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar')
for pos, nome in enumerate(palavras):
    print(f'Na palavra {nome.upper()} temos ', end='')
    for l in nome:
        if l in 'aeiou':
            print(l, end=' ')
    print('\n', end='')