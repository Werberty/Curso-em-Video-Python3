from random import choice
from time import sleep
print('---JOKENPÔ---')
joken = ['pedra', 'papel', 'tesoura']
pessoa = str(input('Jokeeeenpô: ')).lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
ia = choice(joken)
print('computador:',ia,'!')
if pessoa == ia:
    print('Jogue novamente...')
elif (pessoa == 'pedra' and ia == 'tesoura') or (pessoa == 'papel' and ia == 'pedra') or (pessoa == 'tesoura' and ia == 'papel'):
    print('Você ganhou!')
else:
    print('Perdeu!')