n = int(input('Digite um número para ser sua tabuada: '))
print('_'*12)
print('TABUADA DO {}:'.format(n))
for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')