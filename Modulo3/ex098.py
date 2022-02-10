from time import sleep
def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print('-='*16)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim > inicio:
        fim += 1
    elif inicio > fim:
        fim -= 1
        passo *= -1
    for v in range(inicio, fim, passo):
        print(v, end=' ')
        sleep(0.25)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-='*16)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('INICIO: '))
f = int(input('FIM:    '))
p = int(input('PASSO:  '))
contagem(i, f, p)
