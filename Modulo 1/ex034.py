print('----Vamos lhe dar um aumento----')
salario = float(input('Qual o valor do seu salário: R$'))
if salario > 1250:
    aumento = salario*0.1 + salario
else:
    aumento = salario*0.15 + salario
print('Seu novo saláio é de R${:.2f}'.format(aumento))