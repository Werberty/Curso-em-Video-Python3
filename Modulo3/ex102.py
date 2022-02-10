def fatorial(n, show=False):
    """
    ->:Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O valor faorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    print('-'*20)
    if show:
        for c in range(n, 0, -1):
            print(c, end=' x ')
        print(f'= {f}')
    else:
        print(f'{f}')


print(fatorial(5, show=True))
