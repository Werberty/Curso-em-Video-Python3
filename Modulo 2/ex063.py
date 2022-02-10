n = int(input('Digite um número: '))
y = n - 2
n1 = 0
n2 = 1
if n >= 1:
    print(n1, end='')
if n >= 2:
    print(' - {}'.format(n2), end='')
if n >=3:
    while y != 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        print(' - {}'.format(n3), end='')
        y -= 1
print(' - FIM')