cont = 0
while True:
    n = int(input('Que ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    else:
        while True:
            cont += 1
            print(f'{n} x {cont} = {n*cont}')
            if cont == 10:
                print('-' * 30)
                cont = 0
                break
print('Tabuada encerrada')