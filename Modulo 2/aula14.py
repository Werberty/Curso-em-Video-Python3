c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar [S/N]? ')).lower()
print('Fim')

nu = 1
par = impar = 0
while nu != 0:
    nu = int(input('Digite um número: '))
    if nu != 0:
        if nu % 2 == 0:
            par += 1
        else:
            impar += 1
print('tem {} números pares e {} impares'.format(par, impar))