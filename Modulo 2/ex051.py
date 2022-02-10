print('-+-'*7)
print('   GERADOR DE PA   ')
print('-+-'*7)
n = int(input('Primeiro termo da PA: '))
r = int(input('A sua razão: '))
y = n
print(n)
for c in range(0, 9):
    y = y + r
    print(y)