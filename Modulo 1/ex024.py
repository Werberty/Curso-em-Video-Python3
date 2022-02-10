cidade = str(input('Digite o nome da sua ciadede: ')).strip()
frase = cidade.split()
print('Sua começa com o nome Santo?','SANTO' in frase[0].upper())
# OU
print(cidade[:5].upper() == 'SANTO')