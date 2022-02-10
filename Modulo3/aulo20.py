def lin():
    print('-'*20)
def titulo(txt):
    print('-' * 20)
    print(txt)
    print('-' * 20)
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} que ao total são {tam} números.')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lin()
print('  CURSO EM VIDEO  ') # Programa principal
lin()
print('  APREDA PYTHON  ')
lin()
titulo('  CURSO EM VIDEO  ')
titulo('  APRENDA PYTHON  ')
soma(2, 8)
soma(7, 2)
soma(b=7, a=2)
contador(2, 3, 4, 6)
contador(8, 1)
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)