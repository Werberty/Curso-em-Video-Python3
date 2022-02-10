from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = sqrt(ca**2 + co**2)
print(f'O comprimento da hipotenusa vale {h:.2f}')