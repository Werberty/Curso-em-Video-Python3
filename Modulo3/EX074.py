from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
maior = 0
menor = 0
for n in tupla:
    print(f' {n}',end='')
print('\n', end='')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')