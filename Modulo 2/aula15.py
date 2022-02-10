s = 0
while True:
    n = int(input('Digitte um número: '))
    s += n
    if n == 0:
        break
print(f'A soma de todos eles é {s}')
nome = 'José'
idade = 33
salario = 998.5984
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')