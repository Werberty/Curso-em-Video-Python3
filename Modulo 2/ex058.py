from time import sleep
from random import randint
print('\033[32mQuero ver se advinha qual número\nentre 0 e 10 estou pensando\033[m')
sleep(1)
print('Vai!')
ia = randint(0, 10)
n = int(input('EU pensei no número... '))
cont = 1
while ia != n:
    if ia > n:
        print('Mais... tente novamente')
    elif ia < n:
        print('Menos.. tente novamente')
    n = int(input('Eu pensei no número... '))
    cont += 1
print('Acertou!!!\nPensei no {}'.format(ia))
print('Você fez {} palpites'.format(cont))