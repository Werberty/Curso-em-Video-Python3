n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma = soma + n
    cont += 1
print('Você digitou {} números.'.format(cont - 1))
print('A soma de todos eles é {}'.format(soma - 999))