linha = '-'*20
titulo = 'loja eletro'
print(linha)
print(titulo.upper().center(20))
print(linha)
total = 0
mais_1000 = 0
cont = 0
menorPre = 0
menorPro = ' '
while True:
    cont += 1
    produto = str(input('Nome do Produto: ')).lower().strip()
    preço = float(input('Preço: R$'))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    total += preço
    if preço > 1000:
        mais_1000 += 1
    if cont == 1:
        menorPre = preço
        menorPro = produto
    elif preço < menorPre:
        menorPre = preço
        menorPro = produto
    if op == 'N':
        break
fim = ' fim de programa '
print(fim.upper().center(40, '-'))
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {mais_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorPro} que custa R${menorPre:.2f}')