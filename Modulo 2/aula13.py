for c in range(0,8,2):
    print(c)
    print('OI')
print('FIM')
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p):
    print(c)
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}'.format(s))