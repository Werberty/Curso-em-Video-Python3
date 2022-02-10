from random import randint
print('-=-'*10)
print('JOGO DO PAR OU IMPAR')
cont = 0
while True:
    print('-=-' * 10)
    n = int(input('Digite um valor: '))
    op = str(input('Par ou impar? [P/I] ')).upper().strip()[0]
    ia = randint(0, 10)
    res = n + ia
    print('-'*30)
    print(f'Você jogou {n} e o computador {ia}. Total de {res} ', end='')
    if res % 2 == 0:
        print('DEU PAR')
        print('-' * 30)
        if op == 'P':
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            break
    elif res % 2 != 0:
        print('DEU IMPAR')
        print('-' * 30)
        if op == 'I':
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            break
print('Você PERDEU!')
print('-=-' * 10)
print(f'GAME OVER! Você venceu {cont} vez.')

