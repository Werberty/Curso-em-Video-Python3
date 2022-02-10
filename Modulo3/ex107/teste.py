import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumenta(p, 10)}')
print(f'Diminuindo 13%, temos R${moeda.diminue(p, 13)}')