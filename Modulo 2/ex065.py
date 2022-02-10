res = 'S'
cont = 0
somar = 0
maior = 0
menor = 0
while res != 'N':
    n = int(input('Digite um número: '))
    res = str(input('Deseja digitar outro valor [S/N]? ')).upper()[0]
    cont += 1
    somar = somar + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
media = somar/cont
print('A média entre os {} números digitados é {:.2f}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))