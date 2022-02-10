time = list()
jogador = dict()
gols = list()
linha = '-='*40
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, quant):
        gols.append(int(input(f'Quantas gols na partida {p + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        op = str(input('Quer continuar? [S/N] '))
        if op in 'SNsn':
            break
        print('ERRO! Tente novamente.')
    if op in 'Nn':
        break
print(linha)
print(f'{"Cod":>3} {"Nome":<15}{"gols":<15}{"total":<15}')
print('-'*48)
for p, j in enumerate(time):
    print(f'{p:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*48)
while True:
    res = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if res == 999:
        break
    elif res > len(time) - 1:
        print(f'ERRO! Não exite jogador com codigo {res}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[res]["nome"]:}')
        for p, g in enumerate(time[res]["gols"]):
            print(f'   No jogo {p+1} fez {g} gols.')
    print('-'*48)
print('<< Volte Sempre >>')
