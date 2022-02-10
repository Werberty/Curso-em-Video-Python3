import random
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
lista = [a1, a2, a3, a4]
seque = random.shuffle(lista)
print(f'A sequência da apresentação será: {lista}')