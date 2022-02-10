extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinto', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Trese', 'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = int(input('Digite um número entre 0  e 20: '))
while True:
    if n > 20 or n < 0:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {extenso[n]}')