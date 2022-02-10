import math
angulo = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seu cosseno vale {cosseno:.2f}, \nO seu seno vale {seno:.2f} \nE a sua tangente vale {tangente:.2f}')