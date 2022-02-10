num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(3)
num.insert(1, 2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não tem número 4')
print(num)
print(f'Esta lista tem {len(num)} elementos')
print('\n', end='')

valores = []
valores.append(3)
valores.append(6)
valores.append(9)
for v in valores:
    print(f'{v}...', end='')
print('\n', end='')
for p, v in enumerate(valores):
    print(f'Na posição {p} encontreio o valor {v}')
print('FIM')

n = list()
for c in range(0, 3):
    n.append(int(input('Digite um valor: ')))
print(n)

# Peculiaridadeds do Python
# ao igualar uma na outra o Pytho liga uma na outra
a = [1, 2, 3, 4]
b = a
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Para fazer uma copia
c = [3, 5, 4]
d = c[:]
d[1] = 9
print(f'Lista C: {c}')
print(f'Lista D: {d}')

num = [[], []]
num[0].append(3)
num[1].append(4)
print(num)