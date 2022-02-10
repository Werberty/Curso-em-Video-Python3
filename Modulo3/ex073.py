colocação = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Céara', 'Corinthians', 'Coritiba', 'Flamengo', 'Fluminense',
             'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'São Paulo', 'Vasco da Gama')
linha = '--'*40
print(linha)
print(f'Lista de times no Brasilerão: {colocação}')
print(linha)
print(f'Os cinco primeiros colocados são: {colocação[:5]}')
print(linha)
print(f'Os quatro ultimos são: {colocação[-4:]}')
print(linha)
print(f'Times em ordem alfabetica: {sorted(colocação)}')
print(linha)
print(f'O Flamengo está na {colocação.index("Flamengo")+1}º posição')