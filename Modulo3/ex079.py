valores = list()
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    if cont == 0:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        if valor in valores:
            print('Valor duplicado! Não vou adicionar...')
        else:
            valores.append(valor)
            print('Valor adicionado com sucesso...')
    op = str(input('Quer continuar [S/N]? ')).upper().strip()
    if op == 'N':
        break
    cont += 1
print('=-='*15)
valores.sort()
print(f'Você digitou os valores {valores}')
