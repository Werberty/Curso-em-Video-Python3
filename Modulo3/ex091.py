from time import sleep
from operator import itemgetter
from random import randint
jogadores = {}
print('Valores sorteados:')
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'    O {k} tirou {v} no dado')
    sleep(1)
print('Ranking dos jogadores:')
sleep(1)
ordenado = dict()
ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ordenado):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)