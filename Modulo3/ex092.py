from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de nascimento: '))
hoje = date.today()
dados['Idade'] = hoje.year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    ano_aposento = dados['Contratação'] + 35
    dados['Aposentadoria'] = ano_aposento - nasc
print('-'*20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')