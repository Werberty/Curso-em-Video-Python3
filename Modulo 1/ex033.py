print('----Digite 3 número----')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
if n1 > n2 and n1 > n3:
    print('O número {} é o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número {} é maior'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O número {} é maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor é {}'.format(n3))
# Poderia ter criado variaveis para MENOR e MAIOR e te escrito somente um print no final