def metade(valor):
    return valor / 2


def dobro(valor):
    return valor * 2


def aumenta(valor, porc):
    av = valor * (porc / 100) + valor
    return av


def diminue(valor, porc):
    dv = valor - valor * (porc / 100)
    return dv
