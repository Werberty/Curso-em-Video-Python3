from datetime import date
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-'*20)
ano = int(input('Ano de nascimento: '))
idade = (date.today().year) - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria mirim!')
elif idade > 9 and idade <= 14:
    print('Categoria infantil!')
elif idade > 14 and idade <= 19:
    print('Categoria junior!')
elif idade > 19 and idade <= 20:
    print('Categoria sênior!')
else:
    print('Categoria MASTER!')