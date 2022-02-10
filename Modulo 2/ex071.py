banco = 'banco bet'
linha = '='*30
print(linha)
print(banco.upper().center(30))
print(linha)
c50 = 0
c20 = 0
c10 = 0
c1 = 0
valor = int(input('Quanto dinheiro você quer sacar? R$'))
if (valor // 50) >= 1:
    while True:
        valor -= 50
        c50 += 1
        if valor < 50:
            print(f'{c50} notas de 50')
            break
if (valor // 20) >= 1:
    while True:
        valor -= 20
        c20 += 1
        if valor < 20:
            print(f'{c20} notas de 20')
            break
if (valor // 10) >= 1:
    while True:
        valor -= 10
        c10 += 1
        if valor < 10:
            print(f'{c10} notas de 10')
            break
if (valor // 1) >= 1:
    while True:
        valor -= 1
        c1 += 1
        if valor < 1:
            print(f'{c1} notas de 1')
            break