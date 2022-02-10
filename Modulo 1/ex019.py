from random import choice
aluno_1 = str(input('Nome do 1° aluno: '))
aluno_2 = str(input('Nome do 1° aluno: '))
aluno_3 = str(input('Nome do 3° aluno: '))
aluno_4 = str(input('Nome do 4° aluno: '))
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteado = choice(alunos)
print(f'Parabens {sorteado} você vai limpar o quadro!')