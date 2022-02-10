print('-'*9)
print('ESCOLINHA')
print('-'*9)
n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
media = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(media))
if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')