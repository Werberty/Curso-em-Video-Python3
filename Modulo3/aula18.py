test = list()
test.append('Werberty')
test.append(21)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)

pessoal = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoal[1])
print(pessoal[2][1])
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galerinha = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galerinha.append(dado[:])
    dado.clear()
print(galerinha)