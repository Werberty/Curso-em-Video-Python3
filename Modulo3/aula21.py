def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função criada por Werberty
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)

# Parametros opcionais
def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por werberty
    """
    s = a + b + c
    print(f'A soma vale {s}')


soma(3, 2, 5)
soma(3, 2)
soma()
soma(c=3, a=2)

# Escopo de variaveis
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print()
# print(f'No programa principal, x vale{x}') da erro!

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print()

def teste2(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste2(a)
print(f'A fora vale {a}')
print()

# Retorno de valores
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 4)
r2 = somar(3, 2)
r3 = somar(6)
print(f'Os resultados das somas são: {r1} {r2} {r3}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'Fatorial = {fatorial(n)}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('É impar!')
