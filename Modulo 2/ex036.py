print('=+='*4)
print('Emprestimos')
print('=+='*4)
casa = float(input('Valor da casa R$'))
salario = float(input('Seu salário R$'))
anos = float(input('Em quantos anos vai pagar? '))
prestaçao = casa / (anos*12)
if prestaçao <= (salario*0.3):
    print('A prestação do emprestimo vai ser de R${:.2f}'.format(prestaçao))
else:
    print('Você não poderar financiar esta casa. \nTenha um Bom dia!')