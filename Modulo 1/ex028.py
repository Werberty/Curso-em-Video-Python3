from random import randint
from time import sleep
ai = randint(0, 5)
print('pensando...')
n = int(input('Qual o número que a maquina pensou de 0 a 5: '))
print('Processando...')
sleep(3)
if n == ai:
    print('Acertou!')
else:
    print('Errou! :(')
print('Maquina: Eu pensei no {}'.format(ai))