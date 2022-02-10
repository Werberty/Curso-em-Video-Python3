from random import randint
from time import sleep
linha = '-'*33
titulo = 'joga na mega sena'
print(linha)
print(f'{titulo.upper():^33}')
print(linha)
jogos = list()
jogo = list()
num = int(input('Quantos jogos você quer que eu sortei? '))
sort = f' sorteando {num} jogos '
print(f'{sort.upper():=^33}')
for j in range(0, num):
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
        if len(jogo) >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for x, j in enumerate(jogos):
    sleep(1)
    print(f'Jogo {x+1}: {j}')
boa = '< boa sorte! >'
sleep(1)
print(f'{boa.upper():=^33}')