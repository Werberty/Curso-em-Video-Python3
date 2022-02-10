
print('-DETECTOR DE PALINDROMO-')
frase = str(input('Digite a frase: ')).strip().lower()
frase = frase.replace(' ', '')
inverso = ''
n = len(frase) - 1
for letra in range(n, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')