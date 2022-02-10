print('---Digite dois números---\n')
n1 = int(input('\033[35m1° número: '))
n2 = int(input('\033[34m2° número: '))
if n1 > n2:
    print('O {} é maior'.format(n1))
elif n2 > n1:
    print('O {} é maior'.format(n2))
else:
    print('\033[32mOs dois são iguais')