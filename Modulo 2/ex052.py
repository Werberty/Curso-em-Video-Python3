print('-IDENTIFICADOR DE NÙMERO PRIMO-\n')
n = int(input('Digite o número: '))
x = 0
for c in range(2, n):
    if n%c == 0:
        x += 1
if x == 0:
    print('É um número PRIMO')
else:
    print('Não é PRIMO')