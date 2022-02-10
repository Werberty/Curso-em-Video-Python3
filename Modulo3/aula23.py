try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou.')
except ZeroDivisionError:
    print('Não pode ser dividido por zero.')
except KeyboardInterrupt:
    print('O usuario preferio não informar os dados.')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Volte sempre!')