from time import sleep

def maior(* num):
    print('-='*12)
    print('Analizando valores passados...')
    cont = 0
    maiorV = 0
    while cont < len(num):
        print(num[cont], end=' ')
        sleep(0.5)
        if cont == 0:
            maiorV = num[cont]
        else:
            if num[cont] > maiorV:
                maiorV = num[cont]
        cont += 1
    tam = len(num)
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maiorV}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()