def leiaInt(pergunta='Digite um número: '):
    ok = False
    valor = 0
    while True:
        n = str(input(pergunta))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro valido.\033[m')
        if ok:
            break


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')