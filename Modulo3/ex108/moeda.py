def metade(valor=0):
    return valor / 2


def dobro(valor=0):
    return valor * 2


def aumenta(valor=0, porc=0):
    av = valor * (porc / 100) + valor
    return av


def diminue(valor=0, porc=0):
    dv = valor - valor * (porc / 100)
    return dv


def moeda(valor=0, sedula='R$'):
    return f'{sedula}{valor:.2f}'.replace('.', ',')