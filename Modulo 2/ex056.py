soma_idade = 0
ref_id = 0
maior_idade = 'Ninguem'
quant_mulher = 0
for c in range(1,5):
    print('\033[35mPessoa {}:\033[m'.format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [M/F]: ')).lower()
    soma_idade += idade
    if sexo == 'm' and idade > ref_id:
        maior_idade = nome
        ref_id = idade
    if sexo == 'f' and idade < 20:
        quant_mulher += 1
print('\033[32mA média de idade é de {:.1f} anos'. format(soma_idade/4))
print('\033[33m{} é a(o) mais velho'.format(maior_idade))
print('\033[34mTem {} mulheres menores que 20 anos'.format(quant_mulher))