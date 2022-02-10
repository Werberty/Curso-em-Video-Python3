lista = list()
listaImpar = list()
listaPar = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar [S/N]? ')).upper().strip()
    if op == 'N':
        break
for p, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.insert(p, v)
    else:
        listaImpar.insert(p, v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de impares é {listaImpar}')