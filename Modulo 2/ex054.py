from datetime import date
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Qual seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Dessas sete pessoas\n{} atingil a maioridade\nE {} menores de idade.'. format(maior, menor))