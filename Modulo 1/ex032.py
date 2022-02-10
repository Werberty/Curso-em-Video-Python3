from datetime import date
ano = int(input('Digite um ano, coloque 0 para analizar o ano atual: '))
ax1 = ano % 4
ax2 = ano % 100
ax3 = ano % 400
if ano == 0:
    ano = date.today().year
if (ax1 == 0 and ax2 != 0) or (ax2 == 0 and ax3 == 0):
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))