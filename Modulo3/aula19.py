pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade': 21}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*20)
del pessoas['Sexo']
pessoas['nome'] = 'Werberty'
pessoas['peso'] = 54
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*20)
# Dicionario dentro de uma lista
estado1 = {'uf': 'Rio de janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = list() # ou brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(estado2)
print(brasil[0])
print(brasil[0]['uf'])
print('-'*20)
# copiar para o dicionario
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(v, end=' - ')
    print()