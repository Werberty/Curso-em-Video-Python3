print('--FATORIAL--')
n = int(input('Digite um número: '))
cont = n
fator = n
print('Calculando {}! = {} '.format(n,n), end='')
while cont != 0:
    cont -= 1
    if cont != 0:
        print('x {} '.format(cont), end='')
    if cont != 0:
        fator = fator*cont
print('= {}'.format(fator))