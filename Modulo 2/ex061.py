print('-+-'*8)
print('   GERADOR DE PA 2.0   ')
print('-+-'*8)
n = int(input('Primeiro termo da PA: '))
r = int(input('A sua razão: '))
y = 10
cont = 0
while y != 0:
    print('- {} '.format(n), end='')
    n = n + r
    y -= 1
    cont += 1
t = 1
while t != 0:
    t = int(input('\nQuer mostrar mais quantos termos? '))
    if t != 0:
        x = t
        while x != 0:
            print(' - {}'.format(n), end='')
            n = n + r
            x -= 1
            cont += 1
print('Progressão finalizada com {} termos'.format(cont))