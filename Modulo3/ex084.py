pessoas = list()
dados = list()
maiorPeso = menorPeso = 0
pessoas_maior = list()
pessoas_menor = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        menorPeso = maiorPeso = dados[1]
    elif dados[1] >= maiorPeso:
        maiorPeso = dados[1]
    elif dados[1] <= menorPeso:
        menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar [S/N]? ')).strip().lower()[0]
    if op == 'n':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0], end=', ')
print(f'\nO menor peso foi de {menorPeso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0], end=', ')