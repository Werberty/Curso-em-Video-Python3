print('\033[32m----CALCULO DE IMC----\033[m')
peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso/(altura*altura)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade mórbida!')
