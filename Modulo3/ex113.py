def leiaInt(pergunta):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input('Digite um inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro válido!\033[m')
            continue
        else:
            return n


def leiaFloat(pergunta):
    ok = False
    valor = 0
    while True:
        try:
            n = float(input('Digitem um real: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo úsuario.\033[m')
            return 0
        else:
            return n


numInt = leiaInt('Digite um inteiro: ')
numReal = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {numInt} e o real foi {numReal}')
