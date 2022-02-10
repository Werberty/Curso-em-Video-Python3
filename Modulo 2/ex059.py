n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
print('-MENU-\n',
      '[1] Somar\n',
      '[2] Mutiplicar\n',
      '[3] Maior\n',
      '[4] Novos números\n',
      '[5] Sair do programa')
op = int(input('Opção: '))
while op == 4:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    print('-MENU-\n',
          '[1] Somar\n',
          '[2] Mutiplicar\n',
          '[3] Maior\n',
          '[4] Novos números\n',
          '[5] Sair do programa')
    op = int(input('Opção: '))
if op != 5:
    if op == 1:
        soma = n1 + n2
        print('{} + {} é igual a {}.'.format(n1, n2, soma))
    elif op == 2:
        mult = n1*n2
        print('{} X {} é igual a {}.'.format(n1 ,n2, mult))
    elif op == 3:
        if n1 > n2:
            print('{} é maior entre eles.'.format(n1))
        elif n2 > n1:
            print('{} é maior entre eles.'.format(n2))
        else:
            print('São iguais!')