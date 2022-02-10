lanche = ('Hambúrgue', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])
# Tuplas são imutaveis
# lanche[1] = 'refrigerante'
# print(lanche)
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu agora vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(2))
print(c.index(5, 1))
