valores = list()
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > max(valores):
        valores.append(v)
        print('Adicionado ao final da lista...')
    elif v < min(valores):
        valores.insert(0, v)
        print('Adicionado na posição 0...')
    elif v > min(valores) and v < max(valores):
        if v > min(valores[1:3]) and v < max(valores[1:3]):
            valores.insert(2, v)
            print('Adicionado na posição 2...')
        else:
            valores.insert(1, v)
            print('Adicionado na posição 1...')
print(f'Os valores digitados em ordem foram {valores}')