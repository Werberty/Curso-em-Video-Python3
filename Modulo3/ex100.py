from random import randint
from time import sleep

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(0, 5):
        sorteados.append(randint(1, 10))
        print(sorteados[v], end=' ')
        sleep(0.5)
    print('PRONTO!')

def soma(valores):
    soma = 0
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {sorteados}, temos {soma}')


sorteados = []
sorteia()
soma(sorteados)

