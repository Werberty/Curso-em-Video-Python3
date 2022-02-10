pessoa = dict()
lista = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break
print('-='*30)
print(f' - O grupo tem {len(lista)} pessoas.')
somaIdade = 0
for p in lista:
    somaIdade += p['idade']
mediaIdade = somaIdade / len(lista)
print(f' - A média de idade é de {mediaIdade:.2f} anos.')
print(' - As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print('\n - Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > mediaIdade:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')