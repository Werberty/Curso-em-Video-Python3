exp = list(str(input('Digite um expressão: ')))
cont = 0
for p, e in enumerate(exp):
    if '(' in exp[p]:
        cont += 1
    if ')' in exp[p]:
        cont += 1
if cont % 2 == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')