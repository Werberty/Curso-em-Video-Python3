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