jogador = dict()
linha = '-='*40
jogador['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
for p in range(0, quant):
    gols.append(int(input(f'Quantas gols na partida {p + 1}? ')))
jogador['gols'] = gols[:]
total = 0
for g in gols:
    total += g
jogador['total'] = total
print(linha)
print(jogador)
print(linha)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(linha)
print(f'o jogador jogou {quant} partidas.')
for j, g in enumerate(gols):
    print(f'    => N partida {j + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')