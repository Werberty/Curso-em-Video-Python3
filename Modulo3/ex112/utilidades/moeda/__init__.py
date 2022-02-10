def resumo(valor=0, aumento=0, redução=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analizado:":<20} {moeda(valor):<10}')
    print(f'{"Dobro do preço:":<20} {dobro(valor, True):<10}')
    print(f'{"Metade do preço:":<20} {metade(valor, True):<10}')
    print(f'{aumento}{"% de aumento:":<18} {aumenta(valor, aumento, True):<10}')
    print(f'{redução}{"% de redução:":<18} {diminue(valor, redução, True):<10}')
    print('-' * 30)


def metade(valor=0, formato=False):
    res = valor / 2
    if formato:
        return moeda(res)
    else:
        return res


def dobro(valor=0, formato=False):
    res = 2 * valor
    if formato:
        return moeda(res)
    else:
        return res


def aumenta(valor=0, porc=0, formato=False):
    res = valor * (porc / 100) + valor
    if formato:
        return moeda(res)
    else:
        return res


def diminue(valor=0, porc=0, formato=False):
    res = valor - valor * (porc / 100)
    if formato:
        return moeda(res)
    else:
        return res


def moeda(valor=0, sedula='R$'):
    return f'{sedula}{valor:.2f}'.replace('.', ',')
