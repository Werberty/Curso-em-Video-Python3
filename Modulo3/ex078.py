valores = list()
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
maior = max(valores)
menor = min(valores)
print('='*42)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, v in enumerate(valores):
    if maior == v:
        print(f'{p}... ', end='')
print(f'\nO valor menor digitado foi {menor} nas posições ', end='')
for p, v in enumerate(valores):
    if menor == v:
        print(f'{p}... ', end='')