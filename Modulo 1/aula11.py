print('\033[1;33mOla mundo\033[m')
nome = 'werberty'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;32m'}
print('Bem vindo {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))