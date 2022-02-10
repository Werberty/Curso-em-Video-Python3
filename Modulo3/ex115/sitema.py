from CursoEmVideo.Modulo3.ex115.ferramentas.visual import *
from CursoEmVideo.Modulo3.ex115.ferramentas.arquivos import *
from time import sleep

arq = 'dados.txt'
if not arquivoExistente(arq):
    criarArquivo(arq)
while True:
    op = menu(['Ver pessoas cadastradas',
               'Cadastrar novas pessoas', 'Sair do sistema'])
    if op == 1:
        lerArquivo(arq)
    elif op == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif op == 3:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
