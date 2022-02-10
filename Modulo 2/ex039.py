from datetime import date
print('---Programa de alistamento militar---')
ano = int(input('Em que ano nasceu? '))
idade = (date.today().year) - ano
if idade >= 18 and idade <= 45:
    print('Esta na hora de se alistar!')
elif idade < 18:
    print('Você ainda vai se alistar daqui a {} anos.'.format(18 - idade))
else:
    print('Você ja passou {} anos do alistamento.'.format(idade - 45))