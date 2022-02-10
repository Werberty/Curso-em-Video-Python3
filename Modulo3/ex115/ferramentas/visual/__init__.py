cor = ['\033[m', '\033[31m', '\033[32m', '\033[34m']


def leiaInt(pergunta):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(pergunta))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro válido!\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '-'*tam


def titulo(msg):
    print(linha())
    print(f'{msg.center(42)}')
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    for p, c in enumerate(lista):
        print(f'{cor[2]}{p+1} - {cor[3]}{c}{cor[0]}')
    print(linha())
    op = leiaInt(f'{cor[2]}Sua opção: {cor[0]}')
    return op
