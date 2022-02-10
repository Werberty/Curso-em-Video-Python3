pares = list()
impares = list()
numeros = [pares,impares]
for n in range(0, 7):
    num = int(input(f'Digite o {n+1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
print('-'*40)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')
