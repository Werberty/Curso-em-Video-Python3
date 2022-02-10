'''
Poderia ser declarado uma lista somente para
armazenar os codigos das cores, e assim para chamar
a cor so precisaria colocar seu lucar referente na lista cor[x]
'''


def biblioteca(comando):
    if comando != 'fim':
        escreva(f"Acessando o manual do comando {comando}", '\033[37;44m')
        print('\033[m', end='')
        print('\033[7m', end='')
        help(comando)
    return comando


def escreva(msg, cor):
    tam = len(msg) + 4
    print('\033[m', end='')
    print(f'{cor}~' * tam)
    print(f'  {msg}')
    print('~' * tam)


while True:
    escreva('SISTEMA DE AJUDA PyHELP', '\033[37;42m')
    c = biblioteca(str(input('\033[mFunção ou biblioteca > ')))
    if c == 'fim':
        escreva('ATÉ LOGO!', '\033[37;41m')
        break
