lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar [S/N]? ')).upper().strip()
    if op == 'N':
        break
lista.sort(reverse=True)
print(f'Voçê digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')