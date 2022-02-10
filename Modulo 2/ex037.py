print('Conversor')
print('-'*9)
numb = int(input('Digite o número: '))
alt = int(input('Qual a base de conversão: \n -1 para binário\n -2 para octal\n -3 para hexadecimal\nSua oção: '))
if alt == 1:
    print('O noméro em binário é {}'.format(bin(numb)[2:]))
elif alt == 2:
    print('O número em octal é {}'.format(oct(numb)[2:]))
elif alt == 3:
    print('O número em hexadecimal é {}'.format(hex(numb)[2:]))
else:
    print('Tente mais tarde!')
