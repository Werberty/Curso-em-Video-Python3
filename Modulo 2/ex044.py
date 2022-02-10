print('---CAIXA---')
preço = float(input('Valor do produto: R$'))
print('Formas de pagamento: \n'
      '1 - avista/cheque \n'
      '2 - avista no cartão \n'
      '3 - em até 2x no cartão \n'
      '4 - 3x ou mais no cartão')
forma = int(input('Digite o número correspondente: '))
desconto = 0
if forma == 1:
    desconto = preço - preço*0.1
elif forma == 2:
    desconto = preço - preço*0.05
elif forma == 3:
    desconto = preço
elif forma == 4:
    desconto = preço + preço*0.2
print('O preço a ser pago é de R${:.2f}'.format(desconto))