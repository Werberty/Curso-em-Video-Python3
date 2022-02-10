lista = list()
aluno = list()
notas = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    lista.append([nome,[n1, n2], media])
    notas.clear()
    aluno.clear()
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
print('-='*20)
print(f'{"Nº":<4}{"NOME":<13}{"MÉDIA":>6}')
print('-'*23)
for p, d in enumerate(lista):
    print(f'{p:<4}{d[0]:<13}{d[2]:>6.1f}')
while True:
    print('-' * 23)
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if op == 999:
        print('Finalizando...')
        break
    if op <= len(lista) - 1:
        print(f'Notas de {lista[op][0]} são {lista[op][1]}')
print('<'*3, 'VOLTE SEMPRE', '>'*3)