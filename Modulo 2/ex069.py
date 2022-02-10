
mais18 = 0
homens = 0
mulher = 0
while True:
    print('-' * 20)
    print('Cadastre uma pessoa:')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*20)
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if op == 'N':
        print('-' * 20)
        break
    print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')